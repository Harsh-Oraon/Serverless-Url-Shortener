import json
import boto3
import random
import string
import os

# boto3 is AWS's official Python library — it lets your code talk to AWS services like DynamoDB
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])  # table name comes from an environment variable, not hardcoded

def generate_short_code(length=6):
    # picks random letters and numbers to build something like "aZ3xK9"
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def lambda_handler(event, context):
    # Lambda functions always receive two arguments: event (the input data) and context (runtime info, rarely used)

    try:
        body = json.loads(event['body'])  # API Gateway sends the request body as a JSON string, so we parse it
        long_url = body.get('url')

        if not long_url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing "url" in request body'})
            }

        short_code = generate_short_code()

        # Save the mapping into DynamoDB
        table.put_item(Item={
            'short_code': short_code,
            'long_url': long_url
        })

        return {
            'statusCode': 200,
            'body': json.dumps({
                'short_code': short_code,
                'message': 'Short link created successfully'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
