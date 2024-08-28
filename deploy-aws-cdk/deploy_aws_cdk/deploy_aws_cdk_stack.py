from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda
)
from constructs import Construct
import os

class DeployAwsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Define the Lambda function
        cwd = os.getcwd()
        temperature_humidity = _lambda.Function(
            self, 'TemperatureHumidity',
            runtime=_lambda.Runtime.PYTHON_3_12,
            handler='lambda_function.handler',
            code=_lambda.Code.from_asset(os.path.join(cwd, "infra/temperature_humidity_lambda")),
            # Customize the Lambda function name
            function_name='TemperatureHumidityLambda'
        )
        """ 
        # example resource
        # queue = sqs.Queue(
        #     self, "DeployAwsCdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        """