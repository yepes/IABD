import json
import boto3
import decimal

ddb = boto3.resource('dynamodb', region_name='us-east-1') # 

films_collection = ddb.Table('films')

with open("datosPeliculas.json") as ficheroJSON:
    films = json.load(ficheroJSON, parse_float=decimal.Decimal)
    for film in films:
        year = int(film['year'])
        info = film['info']
        title = film['title']

        films_collection.put_item(
            Item={
                'year': year,
                'title': title,
                'info': info,
            }
        )
