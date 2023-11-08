#################
#### imports ####
#################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
from dotenv import load_dotenv
load_dotenv()

################
#### config ####
################
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object("config.stripeconfig")

app.config.from_object("config.ConfigCapatcha")


db = SQLAlchemy(app)

migrate=Migrate(app,db)
#Login_manager

    
# register blueprints

from project.home.controllers import home_blueprint
from project.users.controllers import users_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(users_blueprint)

# flask_login machinery
from project.models import User

login_manager = LoginManager()
# login_manager.login_view = 'users.login'
login_manager.init_app(app)
# login_manager.init(app)
@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(user_id)

   