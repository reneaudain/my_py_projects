import boto3

s3 = boto3.client('s3')
with open('Test_File.txt', 'rb') as f:
    s3.put_object(Bucket='', Key='Test_File.txt', Body=f, ContentType='txt/plain')


