from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app=Flask(__name__)
app.config['SECRET_KEY']='mysecret'                                  
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICTIONS']=False   

app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'static/uploads')
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024

db = SQLAlchemy(app)   
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from Recipe_book import views,models