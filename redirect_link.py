import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    try:
        short_code = event['pathParameters']['code']

        response = table.get_item(Key={'short_code': short_code})

        if 'Item' not in response:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Short link not found'})
            }

        long_url = response['Item']['long_url']

        return {
            'statusCode': 302,
            'headers': {
                'Location': long_url
            },
            'body': ''
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }