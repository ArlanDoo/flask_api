from flask import Flask, jsonify, request
from model.User import User
from model.Post import Post

from create_db import connection_to_db, create_tables, add_request_str

create_tables()

app = Flask(__name__)
cursor = connection_to_db()
DEF_HOME_URL = "/flask_bloger/api/v1.0"
# @app.route('/ping', methods = ['GET'])
# def ping():
#     return jsonify({
#         'name': 'John'
#     })

@app.route(f"{DEF_HOME_URL}/")
def get_api_version():
    return jsonify({
        "API_VERSION" : "V1.0"
    })

@app.route(f"{DEF_HOME_URL}/new_user", methods = ["POST"])
def add_new_user():
    
    user_json = request.get_json()
    new_user = User(user_json["firstname"],
                    user_json["lastname"],
                    user_json["age"],
                    user_json["email"])
    
    cursor.execute(add_request_str())

if __name__ == '__main__':
    app.run(debug=True)