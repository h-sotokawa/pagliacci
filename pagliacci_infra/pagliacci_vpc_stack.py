from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class PagliacciVpcStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPCを作成（CIDR: 192.168.0.0/16）
        vpc = ec2.Vpc(
            self, 
            "pagliacci_vpc",
            cidr="192.168.0.0/16",
            max_azs=1,  # 利用するアベイラビリティゾーンの数
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="pagliacci_public_sub",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24  # 64 IPアドレス
                ),
                ec2.SubnetConfiguration(
                    name="pagliacci_private_sub",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24  # 64 IPアドレス
                ),
            ]
        )
