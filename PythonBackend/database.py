import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

orderitem_table = dynamodb.Table('order')
if orderitem_table == 0:
    orderitem_table = dynamodb
    (
    TableName='order',
    KeySchema=[
        {
            'AttributeName': 'order_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName':  'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'order_id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
    )

print("Table status:", orderitem_table.table_status)