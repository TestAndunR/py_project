let AWS = require('aws-sdk')
const ddb = new AWS.DynamoDB.DocumentClient();
const cognito_idp = new AWS.CognitoIdentityServiceProvider();
const s3 = new AWS.S3();

exports.handler = function (event, context, callback) {

    ddb.put({
        TableName: 'py_table',
        Item: { 'id': '1', 'name': 'bbb' }
    }).promise()
        .then((data) => {
            //your logic goes here
            let response = {
                "isBase64Encoded": true,
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "*"
                },
                "body": data
            }
            callback(null, response);
        })
        .catch((err) => {
            //handle error
        });

    
}