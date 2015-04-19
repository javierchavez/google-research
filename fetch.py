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


# init google play store api
ps = googleplaystore.PlayStore(cookie=cookie)
# init hamming 
hamming = compare.Hamming()

# holder for app objects
apps_array = []
# search and get the results
apps = ps.search('twitter', 1).get_results()
# iterate through the apps populate
# populate apps fields and convert to dict           
for app in apps:
    app.populate_fields()
    apps_array.append(app.to_dict())

# turn the permissions into boolean matrix 
hamming.bin_transform(apps_array, 'permissions')
# show the hamming distance for 10 apps
print(hamming.hamming_dist(10))
# tally all the permissions usage and map to names
mapd_sums = hamming.map_names(hamming.sums())
# show is nicely in json
print(json.dumps(mapd_sums, indent=4))

