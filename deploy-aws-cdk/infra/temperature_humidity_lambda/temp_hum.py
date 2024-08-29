from build_response import buildResponse
from datetime import datetime,UTC
import logging

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def collectData(requestBody):
    try:
        body={**requestBody,"collectAt":str(datetime.now())}
        logging.info(body)
        return buildResponse(201,body)
    except:
        logger.exception("Unknow Error!")
    