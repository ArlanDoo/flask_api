from flask import Flask, jsonify, request
import json

from model.twit import Twit

twits = []

app =  Flask(__name__)

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Twit):
            return {'body': obj.body, 'author': obj.author}
        else:
            return super().default(obj)

app.json_encoder = CustomJSONEncoder

@app.route('/ping', methods = ['GET'])
def ping():
    return jsonify({
        'name': 'John'
    })

@app.route('/twit', methods=['POST'])
def create_twit():
    
    twit_json = request.get_json()
    new_twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(new_twit)
    
    return jsonify({
        'status': 'success'
    })

@app.route('/get_twits', methods=['GET'])
def show_twits():
    return jsonify({'twits': twits})

if __name__ == '__main__':
    app.run(debug=True)