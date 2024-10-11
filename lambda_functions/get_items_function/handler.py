import json
import os
import boto3

# DynamoDBテーブル名を環境変数から取得
TABLE_NAME = os.environ.get('TABLE_NAME')

# DynamoDBリソースを作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # DynamoDBテーブルをスキャン
        response = table.scan()
        items = response.get('Items', [])

        # レスポンスの作成
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }

    except Exception as e:
        # エラーハンドリング
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
