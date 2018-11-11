import json
def handler(event, context):
	response = {
		'statusCode': 200,
		'body': json.dumps('Hello Python')
	}
	return response
