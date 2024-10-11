import json
import os
from datetime import datetime, timezone
import boto3

# DynamoDBテーブル名を環境変数から取得
TABLE_NAME = os.environ.get('TABLE_NAME')

env = AWS_ACCOUNT_ID=692859952029

# DynamoDBリソースを作成
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # パスパラメータからIDを取得
        item_id = event['pathParameters']['id']

        # リクエストボディをパース
        body = json.loads(event.get('body', '{}'))

        # 更新可能なフィールド
        update_fields = {}
        if 'Name' in body:
            update_fields['Name'] = body['Name']
        if 'Description' in body:
            update_fields['Description'] = body['Description']

        if not update_fields:
            return {
                'statusCode': 400,
                'body': json.dumps({'message': 'No fields to update'})
            }

        # UpdatedAtの更新
        update_fields['UpdatedAt'] = datetime.now(timezone.utc).isoformat()

        # 更新式の構築
        update_expression = 'SET ' + ', '.join(f"{k} = :{k}" for k in update_fields)
        expression_values = {f":{k}": v for k, v in update_fields.items()}

        # DynamoDBのアイテムを更新
        response = table.update_item(
            Key={'ID': item_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_values,
            ReturnValues='ALL_NEW'
        )

        updated_item = response.get('Attributes')

        # レスポンスの作成
        return {
            'statusCode': 200,
            'body': json.dumps(updated_item)
        }

    except Exception as e:
        # エラーハンドリング
        return {
            'statusCode': 500,
            'body': json.dumps({'message': 'Internal server error'})
        }
