from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
)
from constructs import Construct

class PagliacciApiGatewayStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, functions, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        api = apigw.RestApi(
            self, "ItemsApi",
            rest_api_name="Items Service",
            description="This service serves items."
        )

        items = api.root.add_resource("items")
        item = items.add_resource("{id}")

        methods = {
            "POST": functions["create_item_function"],
            "GET": functions["get_items_function"]
        }

        for method, func in methods.items():
            items.add_method(
                method,
                apigw.LambdaIntegration(func),
                api_key_required=True
            )

        methods_item = {
            "GET": functions["get_item_function"],
            "PUT": functions["update_item_function"],
            "DELETE": functions["delete_item_function"]
        }

        for method, func in methods_item.items():
            item.add_method(
                method,
                apigw.LambdaIntegration(func),
                api_key_required=True
            )

        plan = api.add_usage_plan(
            "UsagePlan",
            name="Basic",
            throttle=apigw.ThrottleSettings(
                rate_limit=100,
                burst_limit=200
            )
        )

        key = api.add_api_key("ApiKey")
        plan.add_api_key(key)
        plan.add_api_stage(
            stage=api.deployment_stage
        )