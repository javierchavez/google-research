# If module is laoded then reload it otherwise
# catch the exception and import the module
try:
    googleplaystore
    compare
    reload(compare)
    reload(googleplaystore)
except NameError:
    from utils import compare
    from storeapi import googleplaystore
else:
    print("problem with gps module")
    
import json
import os


default_value = ''
# get the vars defined in bashrc
cookie = {
    "PLAY_PREFS": os.getenv('PLAY_PREFS', default_value),
    "NID": os.getenv('NID', default_value),
    "_gat": os.getenv('GAT', default_value),
    "_ga":os.getenv('_GA', default_value)
}

# fp = open('dt.json', 'w')
# # init google play store api
# ps = googleplaystore.PlayStore(cookie=cookie)

# # holder for app objects
# apps_array = []
# # search and get the results
# apps = ps.search('twitter', 1).get_results()
# # iterate through the apps populate
# # populate apps fields and convert to dict           
# for app in apps:
#     app.populate_fields()
#     apps_array.append(app.to_dict())

# # # output as json
# fp.write(json.dumps(apps_array, indent=4))
# fp.close()


# app = ps.get_app('com.vivitylabs.android.braintrainer')
# app.populate_fields()
# print(json.dumps(app.to_dict(), indent=4))

fp = open('dt.json', 'r')
fp_out = open('dt_out.json', 'w')
# parse json into object
android_app_array = json.load(fp)
# new hamming class
hamming = compare.Hamming()
# convert all the android app's permissions into a boolean list
apps = hamming.bin_transform(android_app_array, 'permissions' , fp_out)
# apps=android_app_array

# generate the sums of all the permissions 
sums = hamming.sums()

# map the string value to the int bool value
kv = hamming.map_names(android_app_array[0]['permissions'])

# print(json.dumps(kv,indent=4))
# print(json.dumps(sums,indent=4))
print(hamming.hamming_dist(10))
