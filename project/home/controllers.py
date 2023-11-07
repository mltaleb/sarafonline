#################
#### imports ####
#################
from flask import flash, redirect, url_for, render_template,Blueprint,request
from flask_login import login_required,current_user
from project.models import *
from flask import request,render_template
import stripe
# from io import BytesIO
home_blueprint = Blueprint(
    'home',__name__,
    template_folder='templates'
)
import os

######################## 
#STRIPE
####################"###"
YOUR_DOMAIN = 'https://127.0.0.1:5000'
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
##########################
#### helper functions ####
##########################

stripe.api_key=os.environ.get('STRIPE_SECRET_KEY')
# def login_required(test):
#     @wraps(test)
#     def wrap(*args, **kwargs):
#         if 'logged_in' in session:
#             return test(*args, **kwargs)
#         else:
#             flash('You need to login first.')
#             return redirect(url_for('users.login'))
#     return wrap


################
#### routes ####
################

@home_blueprint.route('/payment',methods=['GET','POST'])
@login_required
def payment():  
    if request.method == 'POST':
        try:
            amount= int(request.form.get('amount'))
        except:
            flash('Elige una cantidad de dinero!',category='error')
            return redirect(url_for('home.home'))
        try:
            checkout_session=stripe.checkout.Session.create(
                line_items = [
                              {'price':'price_1O7L9JD42mBmGGA4mI6yAr5j' ,'quantity':amount}
                              ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel'
            )
            
        except stripe.error.CardError as e:
            return redirect(url_for('home.error'))
        return redirect(checkout_session.url,code=303)
   

@home_blueprint.route("/success")
@login_required
def success():
    return render_template('success.html',user=current_user)
@home_blueprint.route("/error")
def error():
    return "Payment not successful"
# def checkout():
#     print(STRIPE_PUBLIC_KEY)
#     try:
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
#                     'price': 'price_1O7LCDD42mBmGGA4sS1VqbKw',
#                     'quantity': 1,
#                 },
#             ],
#             mode='payment',
#             success_url=url_for('home.thanks',_external=True)+'?session_id={CHECKOUT_SESSION_ID}',
#             cancel_url=url_for('home.checkout',_external=True),
#             automatic_tax={'enabled': True},
#         )
#     except Exception as e:
#         return str(e)
#     # return redirect(checkout_session.url, code=303)
#     return render_template('welcome.html',checkout_session_id=checkout_session['id'],chekout_public_key=STRIPE_PUBLIC_KEY )  # render a template
# @home_blueprint.route('/thanks',methods=['GET','POST'])
# @login_required
# def thanks():
#     return('thanks')
@home_blueprint.route('/',methods=['GET','POST'])
def home():
    return render_template('welcome.html',public_key=STRIPE_PUBLIC_KEY,user=current_user)