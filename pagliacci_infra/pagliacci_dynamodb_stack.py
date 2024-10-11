from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class PagliacciDynamoDBStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.table = dynamodb.Table(
            self, "ItemsTable",
            table_name="Items",
            partition_key=dynamodb.Attribute(
                name="ID",
                type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            encryption=dynamodb.TableEncryption.AWS_MANAGED
        )
