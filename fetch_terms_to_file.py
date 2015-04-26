from storeapi import googleplaystore    
import json
import os
import logging


logging.basicConfig(level=logging.DEBUG)


__author__ = 'Javier Chavez'
__email__ = 'javierc@cs.unm.edu'

fp = open('terms.out.json', 'w')
ft = open('datasets/search_terms.json', 'r')

term_obj = json.load(ft)
terms = term_obj['terms']

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


# search and get the results
term_obj_out = {}

for term in terms:
    # holder for app objects
    apps_array = []
    
    apps = ps.search(term, 1).get_results()
    # iterate through the apps populate
    # populate apps fields and convert to dict
    for app in apps:
        app.populate_fields()
        apps_array.append(app.to_dict())

    logging.debug("Added %s apps" % str(len(apps_array)))
    term_obj_out[term] = apps_array


logging.debug("Searches complete writing to file")
fp.write(json.dumps(term_obj_out, indent=4))
