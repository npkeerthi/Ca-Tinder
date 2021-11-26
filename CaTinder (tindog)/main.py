from flask import Flask,render_template

import datetime
currentday=datetime.date.today()
currentyear=currentday.year
print(datetime.datetime.now(),"\n",currentday,"\n",currentyear)

import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("TinDog Start Here/index.html",year=currentyear)
