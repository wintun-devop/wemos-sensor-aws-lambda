#main heldler
import json,logging
from custom_encoder import CustomEncoder
from api_paths_methods import api_requests,api_paths

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == api_requests['get'] and path == api_paths['health']:
        response = buildResponse(200,{"message":"API is healthly and working ok."})
    else:
        response= buildResponse(404,{"message":"Not Found"})
    return response
    # response = {"test":"test"}
    # return response

#Response Build 
def buildResponse(statusCode,body=None):
    response = {
        "statusCode":statusCode,
        "headers":{
            "Content-Type": "application/json",
            "Accesss-Control-Allow-Origin": "*"
        }
    }
    if body is not None:
        response["body"]=json.dumps(body,cls=CustomEncoder)
    return response