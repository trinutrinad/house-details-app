from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# DynamoDB table
table = dynamodb.Table('FlaskAppTable')

@app.route('/')
def index():
    return "Welcome to the Flask AWS App"

# Endpoint to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user_id = data['user_id']
    user_name = data['user_name']
    
    table.put_item(
        Item={
            'user_id': user_id,
            'user_name': user_name
        }
    )
    return jsonify(message="User added successfully")

# Endpoint to fetch a user
@app.route('/get_user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    response = table.get_item(Key={'user_id': user_id})
    if 'Item' in response:
        return jsonify(response['Item'])
    else:
        return jsonify(message="User not found"), 404

if __name__ == '__main__':
    app.run(debug=True)
