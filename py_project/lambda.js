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
        })
        .catch((err) => {
            //handle error
        });

    callback(null, { "message": "Successfully executed" });
}