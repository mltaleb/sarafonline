from flask_wtf import FlaskForm
from wtforms import StringField,FileField,DateField,HiddenField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length
class MessageForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField(
        'Description', validators=[DataRequired(), Length(max=140)])
    

class DevWebForm(FlaskForm):
    title = StringField("cloud",validators=[DataRequired()])
    description = StringField("Description",validators=[DataRequired()],widget=TextArea())
    img = FileField("img",validators=[DataRequired()])
    mimetype = StringField("MIMEType")

# def choice_query():
#     return DeveloppementWeb.query().all()

class ServiceForm(FlaskForm):
    description=StringField("Description",validators=[DataRequired()], widget=TextArea())
    phone_number = StringField("Phone Number",validators=[DataRequired()])
    date_return=DateField('Date de livraison', format='%Y-%m-%d',validators=[DataRequired()])
    date_interview=DateField('Date de conversation',format='%Y-%m-%d',validators=[DataRequired()])