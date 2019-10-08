import pandas as pd
import requests

server_address = "http://35.228.191.152/"

data = pd.read_csv('../data/googleplaystore.csv')
row_to_ingest = data.sample()
row_to_ingest_json = row_to_ingest.to_dict(orient='records')

request = requests.post(server_address+"ingestion", json=row_to_ingest_json)
print("Request status:", request.reason)