from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://dbuser:msl110918@119.29.96.50:5432/testmodel'
db = SQLAlchemy(app)