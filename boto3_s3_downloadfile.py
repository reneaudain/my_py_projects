import boto3
s3 = boto3.resource('s3')
s3.meta.client.download_file('demostatic-webhost-proj1', 'Test_File.txt', 'Test_File.txt')