import boto3

ficheroUpload = "datosPeliculas.json"
nombreBucket = "iabd-boto3"

# Opción 1 - resource
s3r = boto3.resource('s3', region_name='us-east-1')

# 1.1 mediante upload_file
bucket = s3r.Object(nombreBucket, 'datosSubidosR1.txt')
bucket.upload_file(ficheroUpload)

# 1.2 mediante put
object = s3r.Object(nombreBucket, 'datosSubidosR2.txt')
object.put(Body=b'Ejemplo de datos binarios')

# Opción 2 - cliente
s3c = boto3.client('s3')

# 2.1 mediante upload_file
response = s3c.upload_file(ficheroUpload, nombreBucket, "datosSubidosC1.json")

# 2.2 mediante upload_fileobj
with open(ficheroUpload, "rb") as f:
    s3c.upload_fileobj(f, nombreBucket, "datosSubidosC2.json")

# Cliente: Ejemplo de como crear un objeto y añadirle contenido desde Python
s3c.put_object(Body=b'Ejemplo de datos binarios',
               Bucket=nombreBucket, Key="datosSubidosC3")

