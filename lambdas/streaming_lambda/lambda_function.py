import json
from invoke_openai import InvokeOpenai

def lambda_handler(event, context):
    body = json.loads(event["body"])
    request = body["query"]
    connectionId = event["requestContext"]["connectionId"]
    ivk = InvokeOpenai(connectionId)
    ivk.call_openai(request)

    return {
        "statusCode": 200,
        "body": "Success"
    }