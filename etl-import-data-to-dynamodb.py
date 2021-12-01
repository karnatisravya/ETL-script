import json  # module for converting Python objects to JSON
# decimal module support correctly-rounded decimal floating point arithmetic.
from decimal import Decimal
import boto3  # import Boto3
import sys

def load_data(data, dynamodb=None):
	dynamodb = boto3.resource(
		'dynamodb')

	listings_table = dynamodb.Table('business-listings-table-dev')
	# Loop through all the items and load each
	count = 0
	for obj in data:
		Id = (obj['id'])
		# Print device info
		print("Loading listing Data:", Id)
		listings_table.put_item(Item=obj)
		count += 1
	print(count)

if __name__ == '__main__':
	print(sys.version)
	# open file and read all the data in it
	with open("totalObjsFile.json") as json_file:
		listings_list = json.load(json_file, parse_float=Decimal)
	load_data(listings_list)