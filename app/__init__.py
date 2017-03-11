from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "$hh!"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

# Location where image uploads will be stored
UPLOAD_FOLDER = './app/static/uploads'

# Allowed image upload extensions
#IMAGES = set(['png', 'jpg', 'jpeg', 'gif'])


db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views, models
