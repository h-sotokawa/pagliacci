import json
import os
import boto3
from botocore.exceptions import ClientError

# DynamoDBテーブル名を環境変数から取得
TABLE_NAME = os.environ.get('TABLE_NAME')

# DynamoDBリソースを作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # パスパラメータからIDを取得
        item_id = event['pathParameters']['id']

        # DynamoDBからアイテムを削除
        table.delete_item(
            Key={'ID': item_id},
            ConditionExpression='attribute_exists(ID)'
        )

        # レスポンスの作成
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Item deleted successfully'})
        }

    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Item not found'})
            }
        else:
            # その他のエラー
            return {
                'statusCode': 500,
                'body': json.dumps({'message': 'Internal server error'})
            }
    except Exception as e:
        # エラーハンドリング
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
