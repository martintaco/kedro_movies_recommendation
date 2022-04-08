import json
import os


def lambda_handler(event, context):
    print(event)
    message = "to do okey"
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }