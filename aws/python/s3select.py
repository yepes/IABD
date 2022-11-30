import boto3

s3 = boto3.client('s3')

# 1.- Realizamos la consulta mediante S3Select
resp = s3.select_object_content(
    Bucket='iabd-boto3',
    Key='TMDb_updated.csv',
    ExpressionType='SQL',
    Expression="SELECT s.title, s.overview, s.vote_count, s.vote_average FROM s3object s WHERE cast(s.vote_count as int)> 10000",
    InputSerialization={'CSV': {"FileHeaderInfo": "USE",
                                'AllowQuotedRecordDelimiter': True},
                        'CompressionType': 'NONE'},
    OutputSerialization={'CSV': {}},
)


# 2.- Unimos los datos que vamos recibiendo en streaming
registros = ["title,overview,vote_count,vote_average\n"]
for evento in resp['Payload']:
    if 'Records' in evento:
        print(evento['Records']['Payload'].decode())
        registros.append(evento['Records']['Payload'].decode())

# 3.- Generamos el contenido en un String
file_str = ''.join(registros)

# 4.- Creamos un nuevo objeto en S3
s3.put_object(Body=file_str, Bucket='iabd-boto3',
              Key="TMDb_filtered.csv")
