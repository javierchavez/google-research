

# normalize permissions
# add permissions to model


# require preservation of object
# add app to model

# add images to app
# add comments to app


# associate permissions to app
# maybe we can get or create permission instance here
# instad of getting permissions first


try:
    compare
    reload(compare)
except NameError:
    from utils import compare

import json
import os
import operator
import sqlite3

__author__ = 'Javier Chavez'
__email__ = 'javierc@cs.unm.edu'

fp = open('datasets/2k13_all_by_term.json', 'r')
db = 'app/google_play/db.sqlite3'
android_apps = json.load(fp)
fp.close()

acc = []
for search_term in android_apps.keys():
    for app in android_apps[search_term]:
        acc.append(app)


conn = sqlite3.connect(db)
cursor = conn.cursor()        
