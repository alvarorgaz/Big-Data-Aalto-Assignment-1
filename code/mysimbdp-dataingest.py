import pymongo
import pandas as pd

mongo_client = pymongo.MongoClient('mongodb+srv://alvarorgaz:XLao4jEcoIz3kFXH@big-data-a1-j25ko.gcp.mongodb.net/admin?retryWrites=true&w=majority')
database = mongo_client["google_play_store"]
table = database["apps"]

data = pd.read_csv('./data/googleplaystore.csv')

for i in data.index:
	row_to_ingest = data.loc[[i],:]
	row_to_ingest_json = row_to_ingest.to_dict(orient='records')		
	id = row_to_ingest.index[0]
	app = row_to_ingest.App[id]
	table.insert(row_to_ingest_json)
	print("Ingested app:", ascii(app), "(row "+str(id)+")")