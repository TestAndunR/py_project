import boto3
import botocore
s3 = boto3.client("s3")

def handler(event, context):
    print(event)
    try:
        data = dynamodb.put_item(
            TableName='py_table', 
            Item={'id':{'S':'2'},'name':{'S':'bbbb'}}
            )
        print (data)
    
    except Exception as e:
        print (e)
    
    
    try:
        data = s3.put_object(
            Body="testpy.txt",
            Bucket="aws-amplify-hotspaces",
            Key="Hello world",
            ServerSideEncryption="AES256",
            ACL="public-read"
        )
        response = {
            "isBase64Encoded": 'true',
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": str(data)
        }
        return response
    except BotoCoreError as e:
        print(e)
        response = {
            "isBase64Encoded": 'true',
            "statusCode": 502,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*"
            },
            "body": str(e)
        }
        return response


    # try:
    #     data = s3.put_object(
    #         Body="Hellow",
    #         Bucket="aws-amplify-hotspaces",
    #         Key="testpy.txt"
    #     )
        
    # except Exception as e:
    #     print(e)

    # file = "HappyFace5.png"
    
    # try:
    #     print (file)
    #     data = s3.get_object(
    #         Bucket="aws-amplify-hotspaces",
    #         Key=file
    #     )
    #     print (data)
    #     response = {
    #         "isBase64Encoded": 'true',
    #         "statusCode": 200,
    #         "headers": {
    #             "Access-Control-Allow-Origin": "*",
    #             "Access-Control-Allow-Methods": "*"
    #         },
    #         "body": str(data)
    #     }
    #     return response

        
    # except Exception as e:
    #     print(e)
    
    #     response = {
    #         "isBase64Encoded": 'true',
    #         "statusCode": 502,
    #         "headers": {
    #             "Access-Control-Allow-Origin": "*",
    #             "Access-Control-Allow-Methods": "*"
    #         },
    #         "body": str(e)
    #     }
    #     return response
