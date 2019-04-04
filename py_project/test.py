import boto3
import botocore
s3 = boto3.client("s3")

def handler(event, context):

    file = "HappyFace5.pn"
    
    try:
        print (file)
        data = s3.get_object(
            Bucket="aws-amplify-hotspaces",
            Key=file
        )
        print (data)
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

        
    except Exception as e:
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
