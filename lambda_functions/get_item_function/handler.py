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
        # パスパラメータからIDを取得
        item_id = event['pathParameters']['id']

        # DynamoDBからアイテムを取得
        response = table.get_item(Key={'ID': item_id})

        item = response.get('Item')

        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Item not found'})
            }

        # レスポンスの作成
        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }

    except Exception as e:
        # エラーハンドリング
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
