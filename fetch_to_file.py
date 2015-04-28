# If module is laoded then reload it otherwise
# catch the exception and import the module
try:
    googleplaystore
except NameError:
    from storeapi import googleplaystore
else:
    print("problem with gps module")
    
import json
import os


__author__ = 'Javier Chavez'
__email__ = 'javierc@cs.unm.edu'

fp = open('apps.out.json', 'w')

default_value = ''
# get the vars defined in bashrc
cookie = {
    "PLAY_PREFS": os.getenv('PLAY_PREFS', default_value),
    "NID": os.getenv('NID', default_value),
    "_gat": os.getenv('GAT', default_value),
    "_ga":os.getenv('_GA', default_value)
}

search_term = 'google'

# init google play store api
ps = googleplaystore.PlayStore(cookie=cookie)

# holder for app objects
apps_array = []
# search and get the results
apps = ps.search(search_term, 1).get_results()
# iterate through the apps populate
# populate apps fields and convert to dict

for app in apps:
    app.populate_fields(exclude=['reviews'])
    apps_array.append(app.to_dict())


search_term_obj = {
    search_term: apps_array
}

fp.write(json.dumps(search_term_obj, indent=4))
