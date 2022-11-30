import boto3

# Opción 1
print('Buckets mediante resource:')
s3resource = boto3.resource('s3', region_name='us-east-1')
buckets = s3resource.buckets.all()
for bucket in buckets:
    print(f'\t{bucket.name}')

# Opción 2
print('Buckets mediante el cliente:')
s3client = boto3.client('s3')
response = s3client.list_buckets()
for bucket in response['Buckets']:
    print(f'\t{bucket["Name"]}')
