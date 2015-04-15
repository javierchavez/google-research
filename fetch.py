from storeapi import googleplaystore
import json
import os

default_value = ''

# cookie = {"SSID":os.getenv('SSID', default_value),
#           "SID":os.getenv('SID', default_value),
#           "SAPISID":os.getenv('SAPISID', default_value),
#           "PREF":os.getenv('PREF', default_value),
#           "PLAY_PREFS": os.getenv('PLAY_PREFS', default_value),
#           "PLAY_ACTIVE_ACCOUNT": os.getenv('PLAY_ACTIVE_ACCOUNT', default_value),
#           "NID": os.getenv('NID', default_value),
#           "HSID": os.getenv('HSID', default_value),
#           "APISID": os.getenv('APISID', default_value),
#           "_gat": os.getenv('GAT', default_value),
#           "_ga":os.getenv('_GA', default_value)
#           }



#token = os.getenv('TOKEN', default_value)

cookie = {
    "PLAY_PREFS": os.getenv('PLAY_PREFS', default_value),
    "NID": os.getenv('NID', default_value),
    "_gat": os.getenv('GAT', default_value),
    "_ga":os.getenv('_GA', default_value)
}

ps = googleplaystore.PlayStore(cookie=cookie)

# Use the keywords to search for apps

#f = open('apps.json', 'a')

apps_array = []

#for index in range(0, 100):

#for page in range(1, 3):
    
    # get all the apps in the page
apps = ps.search('twitter', 1).get_page()
for app in apps:

        # use att
        # apps_array.append({ "search-term": 'twitter',
        #                     "name": app.name,
        #                     "package-id":app.app_id,
        #                     "perm": app.get_permissions() })
    app.populate_fields()
    apps_array.append(app.to_dict())
    break
        #print apps_array
            # f.write("\t" + apps.get_all_app_titles()[app].encode('ascii', 'ignore') + "(" + apps.get_all_app_ids(apps.get_all_app_urls())[app] + ")\n")
            # for x in apps.get_permissions(apps.get_all_app_urls()[app]):
                # print "\t\t" + x
                # f.write("\t\t" + x+"\n")

    # add to database

print json.dumps(apps_array, indent=4)

exit()





