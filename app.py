from flask import Flask, render_template, redirect, request, url_for, flash, session
import requests
import json
import model
import config
import os

app = Flask(__name__)

env = os.environ['ENV']
if env == 'PROD':
	app.secret_key = os.environ['FLASK_KEY']
else:
	app.secret_key = config.FLASK_KEY

@app.route("/")
def index():
	tory = {}
	nathan = {}
	tory["time"] = model.get_tory_time()
	nathan["time"] = model.get_nathan_time()
	tory["temp"] = model.get_tory_temp()
	nathan["temp"] = model.get_nathan_temp()
	return render_template("altindex.html", tory=tory, nathan=nathan)





if __name__ == "__main__":
	app.run(debug = True)