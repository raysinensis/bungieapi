import requests
import re
import json
##to work on python 2.x
import sys
reload(sys)  
sys.setdefaultencoding('UTF-8')

##login information
login_url = "https://www.bungie.net/en/User/SignIn/Xuid?bru=%252f"
LOGINAPI = 'c00c63ace9b8419b8238f699d04076f1'
xboxuser = raw_input("enter user name: ")
xboxcode = raw_input("enter password: ")
session1 = requests.Session()

##requesting login
instance1 = session1.get(login_url)

##retrieving links
pattern_urlpost = r'urlPost:\'(https://.*?)\''
pattern_ppft = r'<input type="hidden" name="PPFT" id=".*" value="(.*?)"/>'
post_url = re.findall(pattern_urlpost, instance1.content.decode())[0]
ppft = re.findall(pattern_ppft, instance1.content.decode())[0]
LOGINALL = { 'login': xboxuser, 'passwd': xboxcode, 'PPFT': ppft }
instance2 = session1.post(post_url, data = LOGINALL)

##organizing cookie
LOGINheaders = {'X-API-Key': LOGINAPI, 'x-csrf': session1.cookies.get_dict()['bungled']}
instance3 = session1.get('https://www.bungie.net/Platform/User/GetCurrentBungieAccount/', headers=LOGINheaders)

##get IDs
pattern_membID = 'membershipId\":\"(.*?)\"'
pattern_charID = 'characterId\":\"(.*?)\"'
membID = re.findall(pattern_membID, instance3.content.decode())[0]
charID = re.findall(pattern_charID, instance3.content.decode())[0]
char_gs_url = "https://www.bungie.net/platform/Destiny/1/MyAccount/Character/" + charID + "/Vendor/570929315/"
instance4 = session1.get(char_gs_url, headers=LOGINheaders)

##check with vendor
destiny_url = "https://www.bungie.net/platform/Destiny/"
LOGIN = {"X-API-Key":'c00c63ace9b8419b8238f699d04076f1'}
for list1 in instance4.json()['Response']['data']['saleItemCategories']:
	if list1['categoryTitle']=='Armsday Delivery':
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
			except KeyError:
				item_type = "???"
			try:
				item_tier = namedata.json()['Response']['data']['inventoryItem']['tierTypeName']
			except KeyError:
				item_tier = "???"
			print (item_tier + " " + item_type + "\n""-------------------------------------------")
