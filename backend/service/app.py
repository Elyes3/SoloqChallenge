from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import json_util
from bson.objectid import ObjectId
import os

load_dotenv()  # Load environment variables from .env file
# Read MongoDB environment variables
mongo_url = str(os.getenv('MONGO_URL'))
db_name = str(os.getenv('DB_NAME'))

# Connect to MongoDB
client = MongoClient(mongo_url, server_api=ServerApi('1'))
db = client[db_name]

# Check MongoDB connection
try:
    client.server_info()  # Attempt to access server information
    print("Connected to MongoDB")
except Exception as e:
    print("Failed to connect to MongoDB:", str(e))

# Flask app init
app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route('/summoners')
def get_summoners():

    # Select a collection
    collection = db['summoners']

    # Fetch documents from the collection
    documents = collection.find()

    # Convert documents to a list and rename ids
    documents_list = []
    for doc in documents:
        temp = {}
        temp['id'] = str(doc['_id'])
        if not doc['status']:
            continue
        if doc['status'] == 'OK':
            temp = doc
            temp.pop("_id")
        if doc['status'] == 'PENDING':
            temp = {'id': str(doc['_id']), 'summoner': doc['summoner'], 'status': 'PENDING'}
        documents_list.append(temp)
    # Return the documents as JSON
    return json_util.dumps(documents_list)

@app.route('/summoner-names')
def get_summoner_names():
    # Select a collection
    collection = db['summoners']

    # Fetch documents from the collection
    documents = collection.find()

    # Convert documents to a list and rename ids
    documents_list = []
    for doc in documents:
        temp = {'id': str(doc['_id']), 'summoner': doc['summoner']}
        documents_list.append(temp)

    # Return the documents as JSON
    return json_util.dumps(documents_list)


@app.route('/register/<summoner_name>', methods=['POST'])
def register_summoner(summoner_name):
    # Select a collection
    collection = db['summoners']
    try:
        collection.insert_one({'summoner': summoner_name, 'status': 'PENDING'})
    except Exception:
        return "Error", 500
    return "Inserted", 200


@app.route('/update/<oid>', methods=['POST'])
def update_summoner(oid):
    # Select a collection
    collection = db['summoners']
    object_id = ObjectId(oid)
    payload = request.json
    try:
        update_query = {'$set': {'tier': payload.get('tier', 'N/A'),
                                 'lp': payload.get('lp', 0),
                                 'wins': payload.get('wins', 0),
                                 'losses': payload.get('losses', 0),
                                 'games': payload.get('games', 0),
                                 'winrate': payload.get('winrate', 0),
                                 'status': payload.get('status', 'ERROR')
                                 }
                        }
        collection.update_one({'_id': object_id}, update_query)
    except Exception as e:
        return "Error", 500
    return "Inserted", 200
