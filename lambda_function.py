import boto3
import json
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.query(
        ProjectionExpression='TournamentId,#n',
        KeyConditionExpression=Key('PK').eq('Tournament'),
        ExpressionAttributeNames = {'#n': 'Name'}
    )
    tournaments = response['Items']
    for tournament in tournaments:
        tournament['tournamentId']=int(tournament['tournamentId'])
    return {'statusCode': 200, 'body':json.dumps(tournaments)}