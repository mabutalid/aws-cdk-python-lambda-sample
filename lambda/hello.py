import json

print('Loading function')


def sayHi(event, context):
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello Marco'
    }
