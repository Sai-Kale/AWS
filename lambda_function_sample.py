import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_filename = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=json_filename)
    jsonfilereader = json_object['Body'].read()
    jsondict = json.loads(jsonfilereader)
    table =  dynamodb.Table('employees')
    table.put_item(Item=jsondict)
    return 'Hello from Lambda Saikumar Kale'import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
def lambda_handler(event, context):
    # TODO implement
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_filename = event['Records'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,Key=json_filename)
    jsonfilereader = json_object['Body'].read()
    jsondict = json.loads(jsonfilereader)
    table =  dynamodb.Table('employees')
    table.put_item(Item=jsondict)
    return 'Hello from Lambda Saikumar Kale'
