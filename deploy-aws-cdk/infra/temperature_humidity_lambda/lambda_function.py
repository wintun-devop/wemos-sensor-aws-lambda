#main heldler
import logging,json
from api_paths_methods import api_requests,api_paths
from build_response import buildResponse
from temp_hum import collectData

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    logger.info(event)
    httpMethod = event['httpMethod']
    path = event['path']
    if httpMethod == api_requests['get'] and path == api_paths['health']:
        response = buildResponse(200,{"message":"API is healthly and working ok."})
    elif httpMethod == api_requests['post'] and path == api_paths['dht_sensor']:
        response = collectData(json.loads(event["body"]))
    else:
        response= buildResponse(404,{"message":"Not Found"})
    return response

