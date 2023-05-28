from flask import Flask, jsonify, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
from bson import json_util
from bson.objectid import ObjectId
import os
from flask_cors import CORS, cross_origin
import recalculate_stats


app = Flask(__name__)
cors = CORS(app)
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


@app.route('/challenge')
@cross_origin()
def get_challenge_details():

    # Select a collection
    collection = db['challenge']

    # Fetch documents from the collection
    details = collection.find_one({}, {'_id': False})
    return json_util.dumps(details)


@app.route('/summoners')
@cross_origin()
def get_summoners():

    # Select a collection
    collection = db['summoners']

    # Fetch documents from the collection
    documents = collection.find()

    # Convert documents to a list and rename ids
    documents_list = []
    for doc in documents:
        temp = {'id': str(doc['_id'])}
        status = doc.get('status', False)
        if not status or status == "NOT_FOUND":
            continue
        if status == 'OK':
            temp = doc
            temp.pop("_id")
        if status == 'PENDING':
            temp = {'id': str(doc['_id']), 'summoner': doc['summoner'], 'status': 'PENDING'}
        documents_list.append(temp)
    # Return the documents as JSON
    return json_util.dumps(documents_list)


@app.route('/summoner/<summoner_id>')
@cross_origin()
def get_summoner(summoner_id):

    # Select a collection
    collection = db['summoners']

    # Fetch documents from the collection
    doc = collection.find_one({'summoner_id': summoner_id})
    temp = {'id': str(doc['_id'])}
    print(doc)
    status = doc.get('status', False)
    if not status or status == "NOT_FOUND":
        return json_util.dumps({'err': 'summoner not found'})
    if status == 'OK':
        temp = doc
        temp.pop("_id")
    if status == 'PENDING':
        temp = {'id': str(doc['_id']), 'summoner': doc['summoner'], 'status': 'PENDING'}
    # Return the document as JSON
    return json_util.dumps(temp)


@app.route('/summoner-names')
@cross_origin()
def get_summoner_names():
    # Select a collection
    collection = db['summoners']

    # Fetch documents from the collection
    documents = collection.find()

    # Convert documents to a list and rename ids
    documents_list = []
    for doc in documents:
        temp = {'id': str(doc['_id']), 'summoner': doc['summoner'], 'summoner_id': doc.get('summoner_id', '')}
        documents_list.append(temp)

    # Return the documents as JSON
    return json_util.dumps(documents_list)


@app.route('/register/<summoner_name>', methods=['POST'])
@cross_origin()
def register_summoner(summoner_name):
    # Select a collection
    collection = db['summoners']
    try:
        collection.insert_one({'summoner': summoner_name, 'status': 'PENDING'})
    except Exception:
        return "Error", 500
    return "Inserted", 200


@app.route('/update/<oid>', methods=['POST'])
@cross_origin()
def update_summoner(oid):
    # Select a collection
    collection = db['summoners']
    object_id = ObjectId(oid)
    payload = request.json
    try:
        update_query = {'$set': {'tier': payload.get('tier', ''),
                                 'icon_url': payload.get('icon_url', ''),
                                 'level': payload.get('level', 0),
                                 'summoner_id': payload.get('summoner_id', ''),
                                 'division': payload.get('division', 0),
                                 'lp': payload.get('lp', 'ERROR'),
                                 'tier_image_url': payload.get('tier_image_url', ''),
                                 'border_image_url': payload.get('border_image_url', ''),
                                 'win': payload.get('win', 0),
                                 'lose': payload.get('lose', 0),
                                 'games': payload.get('games', 0),
                                 'is_hot_streak': payload.get('is_hot_streak', False),
                                 'series': payload.get('series', False),
                                 'last_updated_at': payload.get('last_updated_at', 0),
                                 'status': payload.get('status', 'ERROR'),
                                 }
                        }
        collection.update_one({'_id': object_id}, update_query)
    except Exception as e:
        return "Error", 500
    return "Inserted", 200


@app.route('/matches/<summoner_id>', methods=['POST'])
@cross_origin()
def post_matches(summoner_id):
    # Select a collection
    collection = db['matches']

    payload = request.json
    payload.reverse()
    try:
        for match in payload:
            exists = collection.find_one({'id': match['id']})
            if exists:
                continue
            if match == payload[-1]:
                # if this is the latest match and it was inserted
                db['summoner'].update_one({'summoner_id': summoner_id}, {'$set': {
                    'last_fetched_game': match['id'],
                    'last_fetched_game_played_at': match['created_at'],
                }})
            match['summoner_id'] = summoner_id
            collection.insert_one(match)
            stats = recalculate_stats(db, summoner_id)
            db['stats'].update_one({'summoner_id': summoner_id}, {'$set': stats}, upsert=True)
    except Exception as e:
        return "Error", 500
    return "Inserted", 200
