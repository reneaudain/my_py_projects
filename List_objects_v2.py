import boto3
s3 = boto3.client('s3')

#response = s3.list_objects_v2(Bucket='demostatic-webhost-proj1', Prefix='Bop/')
#for content in response['Contents']:
#    print(content['Key'])

#using an if statement to search for specific objects    
#response = s3.list_objects_v2(Bucket='demostatic-webhost-proj1')
#for content in response['Contents']:
#    if('.txt' in content['Key']):
 #       print(content['Key'])

#response = s3.list_objects_v2(Bucket='demostatic-webhost-proj1')
#for content in response['Contents']:
#    if('.txt' in content['Key'][-4]):#this is to get .txt as only the suffix
#        print(content['Key'])

def filter_objects_extention(client, bucket, extention): 
    keys = []
    response = s3.list_objects_v2(Bucket=bucket)
    for content in response['Contents']:
        if('.txt' in content['Key'][-(len(extention)):]):
            keys.append(content['Key'])
    return keys

s3 = boto3.client('s3')
extention = ".txt"

#response = filter_objects_extention(s3, 'demostatic-webhost-proj1', '.txt')
#print(response)

def list_objects_keys(client, bucket, prefix=''): 
    keys = []
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    for content in response['Contents']:
        keys.append(content['Key'])
    return keys


response = list_objects_keys(s3, 'demostatic-webhost-proj1','/')
print(response)   
response = filter_objects_extention(s3, 'demostatic-webhost-proj1', '.txt')
print(response)