import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('FlaskAppTable')

    # Example event contains user_id
    user_id = event['user_id']

    # Fetch user from DynamoDB
    response = table.get_item(Key={'user_id': user_id})
    
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({"message": "User not found"})
        }
