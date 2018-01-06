from flask import Flask,g, jsonify
from flask_pymongo import PyMongo
from database import importData
import os
import json
app = Flask(__name__)


# CONFIGURATIONS
app.config.from_object('config')
#Add database
# Check if the collection exists. If no then call the database function

# ESTABLISH & INJECT DB CONNECTION
mongo = PyMongo(app)

@app.before_request
def before_request():
	if not mongo.db.hospitalList.count():
		importData()
	g.db = mongo.db

@app.route('/')
def index():
	return jsonify({'message': 'howdy'})
# Before req@uest
# Afterrequest teardown
# route( root)

# filterHospital and send
