#main heldler
import json

def handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!'
    }