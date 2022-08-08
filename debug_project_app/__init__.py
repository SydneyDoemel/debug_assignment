from flask import Flask
from config import Config
from flask_migrate import Migrate
# Import for Flask Login
from flask_login import LoginManager
# Import for Flask Db and Migrator
from flask_sqlalchemy import SQLAlchemy


# Import for Flask Mail
from flask_mail import Mail, Message



# Create flask app variable
app = Flask(__name__, template_folder='templates')
app.config.from_object(Config)

db = SQLAlchemy(app)

mail = Mail(app)

# Login Config
login = LoginManager()
login.login_view = 'login' # Specify what page to load for NON-authenticated Users


db.init_app(app)
migrate = Migrate(app, db)
login.init_app(app)


login.login_view = 'auth.logMeIn'

from debug_project_app import routes,models
