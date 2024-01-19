import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()
bucket = response['Buckets']
for bucket in buckets:
    print(Buckets['Name'])
