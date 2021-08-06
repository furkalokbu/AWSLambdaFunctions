import boto3
import os
import time

AWS_DEFAULT_REGION = 'eu-west-1'
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION

bucketname = "lambda.created.me.at." + str(time.time())
myS3 = boto3.resource('s3')

try:
    results = myS3.create_bucket(
                            Bucket = bucketname,
                            CreatebucketConfiguration=['LocationConstraint': AWS_DEFAULT_REGION]
                                )
    print("<h1><font color=green>S3 Bucket Created successfully!</font></h1><br><br>" + str(results))
except:
    print("<h1><font color=red>Error!</font></h1><br><br>")