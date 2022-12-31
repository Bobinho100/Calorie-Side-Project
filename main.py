from flask.views import MethodView
from wtforms import form, StringField, SubmitField
from flask import Flask, render_template, request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')