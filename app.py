from flask import Flask, Response, request
import pymongo
import json

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host="localhost",
        port=27017,
        serverSelectionTimeoutMS=1
    )
    db = mongo.company
    mongo.server_info()
except:
    print("Error - Cannot connect to db")


@app.route("/users", methods=['POST'])
def create_user():
    try:
        user = {"name": request.form['name'],
                "lastName": request.form['lastName']}
        dbResponse = db.users.insert_one(user)
        # print(dbResponse.inserted_id)
        return Response(response=json.dumps({"message": "user created", "id": f"{dbResponse.inserted_id}"}),
                        status=200,
                        mimetype='application/JSON'
                        )
    except Exception as ex:
        print("************")
        print(ex)
        print("************")


@app.route('/getsu')
def getSomeUsers():
    try:
        data = db.users.find()
        return data
    except Exception as ex:
        print("************")
        print(ex)
        return Response(response=json.dumps({"message": "Cannot read Users"}),
                        status=500,
                        mimetype='application/json')


if __name__ == '__main__':
    app.run(port=20,
            debug=True,
            host='localhost'
            )
