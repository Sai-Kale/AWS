# AWS
Simple_Lambda_Function(S3->Lambda->DynamoDB)

The logic contains the below steps.
1) Upload a Json file to S3
2) S3 triggers the lambda function and processes the object.
3) Lambda function calls the Dynamo DB and makes an entry into the DynamoDB.
