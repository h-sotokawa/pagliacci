#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pagliacci_infra.pagliacci_dynamodb_stack import DynamoDBStack
from pagliacci_infra.pagliacci_lambda_stack import LambdaStack
from pagliacci_infra.pagliacci_apigateway_stack import ApiGatewayStack


app = cdk.App()

dynamodb_stack = DynamoDBStack(app, "DynamoDBStack")
lambda_stack = LambdaStack(app, "LambdaStack", table=dynamodb_stack.table)
api_gateway_stack = ApiGatewayStack(app, "ApiGatewayStack", functions=lambda_stack.functions)

app.synth()
