import boto3
s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'demostatic-webhost-proj1','Key': 'Test_File.txt'}, ExpiresIn=300)
    

# The response contains the presigned URL
print(response)