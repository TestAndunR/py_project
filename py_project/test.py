import boto3
import botocore
s3 = boto3.client("s3")

def handler(event, context):

    try:
        data = s3.put_object(
            Body="Hellow",
            Bucket="aws-amplify-hotspaces",
            Key="testpy.txt"
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


    file = "HappyFace5.png"
    
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
