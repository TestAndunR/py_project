import boto3
import botocore
s3 = boto3.client("s3")

def handler(event, context):

    file = "HappyFace5.png"
    # try:
    #     data = s3.list_objects(
    #         Bucket='aws-amplify-hotspaces',
    #         MaxKeys=10,
    #         Prefix=''
    #     )

    #     print (data)
    
    # except BotoCoreError as e:
    #     print(e)
    # try:
    #     data = s3.get_object(
    #     Bucket="aws-amplify-hotspaces",
    #     Key="HappyFace5.p"
    #     )
    #     print(data)
    # except Exception as e:
    #     print(e)
    
    try:
        print (file)
        data = s3.get_object(
            Bucket="aws-amplify-hotspaces",
            Key=file
        )
        print (data)
        
    except Exception as e:
        print(e)
    
    return {"message": "Successfully executed"}
