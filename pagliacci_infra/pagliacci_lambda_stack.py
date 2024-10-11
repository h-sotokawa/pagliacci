from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    Duration,
)
from constructs import Construct

class PagliacciLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, table, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        self.functions = {}

        role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )

        role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )

        table.grant_full_access(role)

        function_names = [
            "create_item_function",
            "get_items_function",
            "get_item_function",
            "update_item_function",
            "delete_item_function",
        ]

        for name in function_names:
            lambda_function = _lambda.Function(
                self, f"{name}_function",
                function_name=f"{name}_function",
                runtime=_lambda.Runtime.PYTHON_3_12,
                handler="handler.lambda_handler",
                code=_lambda.Code.from_asset(f"lambda_functions/{name}"),
                environment={
                    "TABLE_NAME": table.table_name
                },
                role=role,
                timeout=Duration.seconds(30),
                memory_size=256
            )

            self.functions[name] = lambda_function