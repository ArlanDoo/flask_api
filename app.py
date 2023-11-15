from flask import Flask, jsonify, request
from handlers.json_encoder import UserEncoder, PostEncoder
from model.User import User
from model.Post import Post

import datetime
import json

from create_db import connection_to_db, create_tables, add_request_str

create_tables()

app = Flask(__name__)
cursor = connection_to_db()
DEF_HOME_URL = "/flask_bloger/api/v1.0"

users = []
posts = []

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
    
    # cursor.execute(add_request_str("users", [
    #     {user_json["firstname"]},
    #     {user_json["lastname"]},
    #     {user_json["age"]},
    #     {user_json["email"]}
    # ]))
    
    users.append(new_user)
    # return json.dumps(new_user, cls = UserEncoder)


@app.route(f"{DEF_HOME_URL}/new_post", methods = ["POST"])
def add_new_post():
    
    post_json = request.get_json()
    new_post = Post(post_json["post_id"],
                    post_json["author"],
                    post_json["description"])
    
    posts.append(new_post)
    
    return jsonify({
        "result": "Post is added"
    })
    
@app.route(f"{DEF_HOME_URL}/update_post", methods = ["PUT"])
def add_new_post():
    
    post_json = request.get_json()
    for i in range(len(posts)):
        if (posts[i]["post_id"] == post_json["post_id"] 
            & posts[i]["author"] == post_json["author"]):
            
            current_date = datetime.datetime.now()
            
            posts[i]["description"] = post_json["description"]
            posts[i]["date_update"] = str(datetime.timedelta(current_date))
            
            return jsonify({
                "result": "Post is update"
            })
            
    
    return jsonify({
        "result": "Post is not found"
    })
    
    
@app.route(f"{DEF_HOME_URL}/get_post")
def get_post():
    
    result = []
    
    for p in posts:
        if p.post_id == request.args["post_id"]:
            print(p.post_id)
            # result.append({
            #     "post_id": p.post_id,
            #     "author": p.author,
            #     "description": p.description
            # })
            result.append(p)            
            
    if result:
        return json.dump(result)
    else:
        return jsonify({
            "target_posts": "Post is not found"
        })


if __name__ == '__main__':
    app.run(debug=True)