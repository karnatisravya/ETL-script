import json


# read file
#/Users/varmamaryala/Downloads/yelp_academic_dataset_business.json
with open('/Users/varmamaryala/Downloads/yelp_academic_dataset_business.json', 'r') as myfile:
	data=myfile.read()
categories = {'test'}
# parse file
objs = json.loads(data)

count = 0
#temp2 = {}
area_zip = set({})
plumbersFile = "plumbersFile.json"
lightsFile = "lightsFile.json"
electriciansFile = "electriciansFile.json"
cabinetsFile = "cabinetsFile.json"
countertopsFile = "countertopsFile.json"
paintersFile = "paintersFile.json"
appliancesFile = "appliancesFile.json"
floorsFile = "floorsFile.json"
totalObjsFile = "totalObjsFile.json"
electricians = []
cabinets = []
countertops = []
plumbers = []
lights = []
painters = []
appliances = []
floors = []
contractors = []
totalObjs = []
index = 1
for obj in objs:
	temp = {
		'id': '',
		'listingId': '',
		'name': '',
		'address': '',
		'city': '',
		'postal_code': '',
		'stars': 0.0,
		'review_count': 0,
		'is_open': 1,
		'hours': {},
		'categories': '',
		'categoryId': 0
	}
	if 'categories' not in obj:
		continue
	if obj['categories'] and obj['state'] == "WA" and "Plumbing" in obj['categories']:
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 1
		
		plumbers.append(temp)
		totalObjs.append(temp)
	if obj['categories'] and obj['state'] == "WA" and "Lighting Fixtures & Equipment" in obj['categories']:
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 2

		lights.append(temp)
		totalObjs.append(temp)
	if obj['categories'] and obj['state'] == "WA" and "Electricians" in obj['categories']:
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 3

		electricians.append(temp)
		totalObjs.append(temp)
	if obj['categories'] and obj['state'] == "WA" and ("Cabinets" in obj['name'] or "Cabinetry" in obj['categories']):
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 4
	
		cabinets.append(temp)
		totalObjs.append(temp)
		
	if obj['categories'] and obj['state'] == "WA" and ("Countertops" in obj['name'] or "Countertop Installation" in obj['categories']):
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 5
	
		countertops.append(temp)
		totalObjs.append(temp)
		
	if obj['categories'] and obj['state'] == "WA" and ("Painters" in obj['name'] or "Painters" in obj['categories']):
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 6

		painters.append(temp)
		totalObjs.append(temp)

	if obj['categories'] and obj['state'] == "WA" and ("Appliances" in obj['name'] or "Appliances" in obj['categories']):
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 7

		appliances.append(temp)
		totalObjs.append(temp)
		
	if obj['categories'] and obj['state'] == "WA" and ("Flooring" in obj['categories'] or "Tiling" in obj['categories']):
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 8

		floors.append(temp)
		totalObjs.append(temp)
		
	if obj['categories'] and obj['state'] == "WA" and ("Contractors" in obj['categories']):
		temp['id'] = str(index)
		index += 1
		temp['listingId'] = obj['business_id']
		temp['name'] = obj['name']
		temp['address'] = obj['address']
		temp['city'] = obj['city']
		temp['state'] = obj['state']
		temp['postal_code'] = obj['postal_code']
		temp['stars'] = obj['stars']
		temp['review_count'] = obj['review_count']
		temp['is_open'] = obj['is_open']
		temp['hours'] = obj['hours']
		temp['categories'] = obj['categories']
		temp['categoryId'] = 9
		count += 1
		contractors.append(temp)
		totalObjs.append(temp)
	
with open(plumbersFile, 'w', encoding='utf-8') as outfile:
	json.dump(plumbers, outfile, ensure_ascii=False, indent=4)
with open(lightsFile, 'w', encoding='utf-8') as outfile:
	json.dump(lights, outfile, ensure_ascii=False, indent=4)
with open(electriciansFile, 'w', encoding='utf-8') as outfile:
	json.dump(electricians, outfile, ensure_ascii=False, indent=4)
with open(cabinetsFile, 'w', encoding='utf-8') as outfile:
	json.dump(cabinets, outfile, ensure_ascii=False, indent=4)
with open(countertopsFile, 'w', encoding='utf-8') as outfile:
	json.dump(countertops, outfile, ensure_ascii=False, indent=4)
with open(paintersFile, 'w', encoding='utf-8') as outfile:
	json.dump(painters, outfile, ensure_ascii=False, indent=4)
with open(appliancesFile, 'w', encoding='utf-8') as outfile:
	json.dump(appliances, outfile, ensure_ascii=False, indent=4)
with open(totalObjsFile, 'w', encoding='utf-8') as outfile:
	json.dump(totalObjs, outfile, ensure_ascii=False, indent=4)
#print(objs[0])
#obj['postal_code'] == '98005' 
print(count)
print(len(totalObjs))
print(len(plumbers))
print(len(appliances))
print(len(painters))
print(len(countertops))
print(len(cabinets))
print(len(electricians))
print(len(lights))
print(len(floors))
print(len(contractors))



#print(temp2)
#print(area_zip)