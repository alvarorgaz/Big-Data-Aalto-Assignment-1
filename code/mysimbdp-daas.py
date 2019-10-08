import pymongo
from flask import Flask, request

mongo_client = pymongo.MongoClient('mongodb+srv://alvarorgaz:XLao4jEcoIz3kFXH@big-data-a1-j25ko.gcp.mongodb.net/admin?retryWrites=true&w=majority')
database = mongo_client["google_play_store"]
table = database["apps"]

app = Flask(__name__)

@app.route('/ingestion', methods=['POST'])
def ingestion():
	table.insert(request.json)
	return ""

app.run(host="0.0.0.0", port=80)