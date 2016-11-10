import requests
import json

LOGIN = {"X-API-Key":'c00c63ace9b8419b8238f699d04076f1'}
destiny_url = "https://www.bungie.net/platform/Destiny/"
gunsmith_url = "https://www.bungie.net/Platform//Destiny/Vendors/570929315/"
print ("looking for the Gunsmith..." + "\n...")
gsdata = requests.get(gunsmith_url, headers=LOGIN)
error_stat = gsdata.json()['ErrorStatus']
print ("Retrieving data: " + error_stat)
##f = open('output.txt', 'w')
##f.write(json.dumps(res.json(), indent=4))

for list1 in gsdata.json()['Response']['data']['saleItemCategories']:
    list2 = list1['saleItems']
    print("-------------------------------------------")
    for item in list2:
        hashID = str(item['item']['itemHash'])
        hashReqString = destiny_url + "Manifest/" + "6" + "/" + hashID + "/"
        namedata = requests.get(hashReqString, headers=LOGIN)
        item_name = namedata.json()['Response']['data']['inventoryItem']['itemName']
        print (item_name)
        item_type = namedata.json()['Response']['data']['inventoryItem']['itemTypeName']
        item_tier = namedata.json()['Response']['data']['inventoryItem']['tierTypeName']
        print (item_tier + " " + item_type + "\n")

LOGIN = {"X-API-Key":'c00c63ace9b8419b8238f699d04076f1'}
destiny_url = "https://www.bungie.net/platform/Destiny/"
outfit_url = "https://www.bungie.net/Platform//Destiny/Vendors/134701236/"
print ("looking for the Outfitter..." + "\n...")
ofdata = requests.get(outfit_url, headers=LOGIN)
error_stat = ofdata.json()['ErrorStatus']
print ("Retrieving data: " + error_stat)
##f = open('output.txt', 'w')
##f.write(json.dumps(res.json(), indent=4))

for list1 in ofdata.json()['Response']['data']['saleItemCategories']:
    list2 = list1['saleItems']
    print("-------------------------------------------")
    for item in list2:
        hashID = str(item['item']['itemHash'])
        hashReqString = destiny_url + "Manifest/" + "6" + "/" + hashID + "/"
        namedata = requests.get(hashReqString, headers=LOGIN)
        item_name = namedata.json()['Response']['data']['inventoryItem']['itemName']
        print (item_name)
        item_type = namedata.json()['Response']['data']['inventoryItem']['itemTypeName']
        item_tier = namedata.json()['Response']['data']['inventoryItem']['tierTypeName']
        print (item_tier + " " + item_type + "\n")

k=input("all done")
