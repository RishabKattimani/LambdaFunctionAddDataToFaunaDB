import json
import re
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(secret="YOUR_SECRET_HERE")
allusers = client.query(
    q.paginate(
    q.match(q.index('YOU_INDEX')))
 )

def lambda_handler(event, context):
    # TODO implement
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

client.query(
   q.create(
     q.collection("YOUR_COLLECTION"),
     {"data": {"Temp": event}}
   ))
