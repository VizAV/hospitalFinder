from flask import Flask,g, jsonify,request
from flask_pymongo import PyMongo
from database import importData

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

@app.route('/filterData', methods=['POST','GET'])
def filterData():
	lat=request.form['lat']
	lon=request.form['lon']
	city=request.form['city']
	services=request.form['services']
	specializations=request.form['specializations']

	filteredHospitals = g.db.hospitalList.find({"$and":[{"city":city},{"specializations":specializations}]})

	return jsonify(list(filteredHospitals))


# Afterrequest teardown
# route( root)

# filterHospital and send
