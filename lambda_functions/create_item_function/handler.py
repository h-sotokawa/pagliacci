import json
import os
import uuid
from datetime import datetime, timezone
import boto3

# DynamoDBテーブル名を環境変数から取得
TABLE_NAME = os.environ.get('TABLE_NAME')

# DynamoDBリソースを作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # リクエストボディをパース
        body = json.loads(event.get('body', '{}'))

        # 必須フィールドの検証
        name = body.get('Name')
        description = body.get('Description')

        if not name or not description:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'Name and Description are required.'})
            }

        # UUIDの生成
        item_id = str(uuid.uuid4())

        # 現在のUTCタイムスタンプ
        timestamp = datetime.now(timezone.utc).isoformat()

        # アイテムデータの作成
        item = {
            'ID': item_id,
            'Name': name,
            'Description': description,
            'CreatedAt': timestamp,
            'UpdatedAt': timestamp
        }

        # DynamoDBにアイテムを保存
        table.put_item(Item=item)

        # レスポンスの作成
        return {
            'statusCode': 201,
            'body': json.dumps(item)
        }

    except Exception as e:
        # エラーハンドリング
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
