from flask import Flask,jsonify,request,render_template,Response,flash,redirect,url_for
from Game import Game

app = Flask(__name__)

app.config.update(dict(
	SECRET_KEY="powerful secretkey",
	WTF_CSRF_SECRET_KEY="a csrf secret key"
))
