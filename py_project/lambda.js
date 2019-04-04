let AWS = require('aws-sdk')
const cognito_idp = new AWS.CognitoIdentityServiceProvider();
const s3 = new AWS.S3();

exports.handler = function (event, context, callback) {
    s3.getObject({
        'Bucket': "aws-amplify-hotspaces",
        'Key': "HappyFace.+@{type}"
    }).promise()
        .then(data => {
            console.log(data);           // successful response
            /*
            data = {
                AcceptRanges: "bytes", 
                ContentLength: 3191, 
                ContentType: "image/jpeg", 
                ETag: "\\"6805f2cfc46c0f04559748bb039d69ae\\"", 
                LastModified: <Date Representation>, 
                Metadata: {...}, 
                TagCount: 2, 
                VersionId: "null"
            }
            */
        })
        .catch(err => {
            console.log(err, err.stack); // an error occurred
        });
    cognito_idp.listUsers({
        UserPoolId: "us-east-1_mcdTV1jKi",
        Filter: `aa${count}`,
        Limit: "10"
    }, function (error, data) {
        if (error) {
            // implement error handling logic here
            throw error;
        }
        // your logic goes within this block
    });

    callback(null, { "message": "Successfully executed" });
}