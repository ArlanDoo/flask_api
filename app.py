from flask import Flask, jsonify, request, render_template
import random

from app_config import MAIN_PATH_API
from postgres.create_db import create_tables
from model.post import Post
from model.user import User


app = Flask(__name__)
# create_tables()

@app.route(f"{MAIN_PATH_API}/ping", methods = ["GET"])
def ping_app():
    return render_template('index.html')


@app.route(f"{MAIN_PATH_API}/newuser", methods = ["POST"])
def add_user():
    
    user_json = request.get_json()
    
    new_user = User(random.randrange(1, 1024),
                    user_json["firstname"],
                    user_json["lastname"],
                    user_json["age"],
                    user_json["email"])
    
    return jsonify(new_user.add_user())


@app.route(f"{MAIN_PATH_API}/add_post", methods = ["POST"])
def add_post():
    
    post_json = request.get_json()
    
    new_post = Post(random.randrange(1, 1024),
                    post_json["author"],
                    post_json["description"],
                    post_json["rating"],
                    post_json["added"],
                    post_json["updated"])
    
    return jsonify(new_post.add_post())


@app.route(f"{MAIN_PATH_API}/update_post", methods = ["PUT"])
def update_post():
    
    post_json = request.get_json()
    
    new_post = Post(post_json["id"], "",
                    post_json["description"],
                    post_json["rating"], "", "")
    
    return jsonify(new_post.update_post())


@app.route(f"{MAIN_PATH_API}/del_post", methods = ["DELETE"])
def del_post():
    
    post_json = request.get_json()
    post_id = post_json["id"]
    post = Post(post_id, "", "", 0, "", "")
    
    return jsonify(post.delete_post())


@app.route(f"{MAIN_PATH_API}/posts", methods = ["GET"])
def get_posts():
    
    post_id = request.args["post_id"]
    post_author = request.args["author"]
    
    post = Post(post_id, post_author, "", 0, "", "")
    
    return jsonify(post.get_post())


if __name__ == "__main__":
    app.run(debug=True)