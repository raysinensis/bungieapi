import requests
import json

LOGIN = {"X-API-Key":'c00c63ace9b8419b8238f699d04076f1'}
destiny_url = "https://www.bungie.net/platform/Destiny/"
vdestiny_url = "https://www.bungie.net/platform/Destiny/vendors/"
vendor_dict = { 'gunsmith':"570929315/", 'outfitter':"134701236/",'shipwright':"459708109/"}
for vname, vID in vendor_dict.items():
	print ("looking for the " + vname + "\n...")
	url = vdestiny_url + vID
	vdata = requests.get(url, headers=LOGIN)
	error_stat = vdata.json()['ErrorStatus']
	print ("Retrieving data: " + error_stat)
	for list1 in vdata.json()['Response']['data']['saleItemCategories']:
    		list2 = list1['saleItems']
    		print("-------------------------------------------")
   		for item in list2:
        		hashID = str(item['item']['itemHash'])
        		hashReqString = destiny_url + "Manifest/" + "6" + "/" + hashID + "/"
        		namedata = requests.get(hashReqString, headers=LOGIN)
        		item_name = namedata.json()['Response']['data']['inventoryItem']['itemName']
        		print (item_name)
        		try:
				item_type = namedata.json()['Response']['data']['inventoryItem']['itemTypeName']
			except KeyError,e:
				item_type = "???"
				f = open('strange.txt', 'w')
				f.write(json.dumps(namedata.json(), indent=4))
        		try:
				item_tier = namedata.json()['Response']['data']['inventoryItem']['tierTypeName']
			except KeyError,e:
				item_tier = "???"
        		print (item_tier + " " + item_type + "\n"-------------------------------------------")

k=input("-------------------------------------------\nall done")
