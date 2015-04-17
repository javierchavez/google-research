# If module is laoded then reload it otherwise
# catch the exception and import the module
try:
    googleplaystore
    reload(googleplaystore)
except NameError:
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

# init google play store api
ps = googleplaystore.PlayStore(cookie=cookie)

# # holder for app objects
# apps_array = []
# # search and get the results
# apps = ps.search('twitter', 1).get_results()
# # iterate through the apps populate
# # populate apps fields and convert to dict           
# for app in apps:
#     app.populate_fields()
#     apps_array.append(app.to_dict())

# # output as json
# print json.dumps(apps_array, indent=4)


app = ps.get_app('com.vivitylabs.android.braintrainer')
app.populate_fields()
print(json.dumps(app.to_dict(), indent=4))
