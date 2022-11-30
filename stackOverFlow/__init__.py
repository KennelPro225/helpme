from flask import Flask
import pymongo

app = Flask(__name__)
app.config['SECRET KEY'] = '04293911c5c5e7947afa3342ef59d6b6'


try:
    mongo = pymongo.MongoClient(
        host='localhost',
        port=27017,
        serverSelectionTimeoutMS=1000
    )
    db = mongo.stack
    mongo.server_info()
except:
    print("Error - Cannot connect to database")

from stackOverFlow import routes