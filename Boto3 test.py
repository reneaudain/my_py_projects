import boto3

s3 = boto3.client('s3')
response = s3.create_bucket(
    Bucket='RA-boto3-test-1162023'
)
print(response)