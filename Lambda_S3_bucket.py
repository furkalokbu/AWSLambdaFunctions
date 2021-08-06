import boto3
import os

myS3 = boto3.client('s3')
try:
    results = myS3.list_buckets()
    print(results)
    output = ""
    for bucket in results['Buckets']:
        output = output + bucket['Nmame'] + "\n"
    print("<h1><font color=green>S3 Buckets List:</font></h1><br><br>" + output)
except:
    print("<h1><font color=green>Error!</font></h1><br><br>")

