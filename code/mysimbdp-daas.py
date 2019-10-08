from flask import Flask, request

app = Flask(__name__)

@app.route('/ingestion', methods=['POST'])
def ingestion():
	print(request.json)
	return ""

app.run(host="0.0.0.0", port=80)