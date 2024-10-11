#!/usr/bin/env python3
import os

import aws_cdk as cdk

from pagliacci_infra.pagliacci_dynamodb_stack import PagliacciDynamoDBStack
from pagliacci_infra.pagliacci_lambda_stack import PagliacciLambdaStack
from pagliacci_infra.pagliacci_apigateway_stack import PagliacciApiGatewayStack
from pagliacci_infra.pagliacci_vpc_stack import PagliacciVpcStack


app = cdk.App()

dynamodb_stack = PagliacciDynamoDBStack(app, "PagliacciDynamoDBStack")
lambda_stack = PagliacciLambdaStack(app, "PagliacciLambdaStack", table=dynamodb_stack.table)
api_gateway_stack = PagliacciApiGatewayStack(app, "PagliacciApiGatewayStack", functions=lambda_stack.functions)
PagliacciVpcStack(app, "PagliacciVpcStack")

app.synth()
