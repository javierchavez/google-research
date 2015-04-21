# If module is laoded then reload it otherwise
# catch the exception and import the module
try:
    compare
    reload(compare)
except NameError:
    from utils import compare

import json
import os
import operator


__author__ = 'Javier Chavez'
__email__ = 'javierc@cs.unm.edu'

fp = open('datasets/2k13_all_by_term.json', 'r')
android_apps = json.load(fp)
fp.close()

hamming = compare.Hamming(key='permissions')

# get single search term
# hamming.bin_transform(android_apps['facebook'], 'permissions')
# print(hamming.hamming_dist(10))

# mapd_sums = hamming.map_names(hamming.sums())
# print(json.dumps(mapd_sums, indent=4))


# get all the permissions for every app (bin_transform_accumulate)
# and convert all th permissions to a bool matrix.
for search_term in android_apps.keys():
    hamming.accumulate(android_apps[search_term])
    
# hamming is now completly filled with all known permissions
# you can see them all by uncommenting next line
# print(json.dumps(hamming.get_permission_list(), indent=4))

# now transform each permission
for search_term in android_apps.keys():
    hamming.bin_transform(android_apps[search_term])

# compute the avg hamming distance for any given search term
stats = {}
for search_term in android_apps.keys():
    stats[search_term] = hamming.hamming_dist(android_apps[search_term],
                                              threshhold=None)
    
sl = sorted(stats.items(), key=operator.itemgetter(1), reverse=True)

# top 10 searches that show most sporadic use of permissions
for stat in sl[:10]:
    print(stat[0] + ": %.2f" % stat[1])

print('------------------')

# top 10 searches that use mostly the same permissions
for stat in sl:
    print(stat[0] + ": %.2f" % stat[1])


# create a list of all apps....
acc = []
for search_term in android_apps.keys():
    for app in android_apps[search_term]:
        acc.append(app)


# get the sums of all the permissions
mapd_sums = hamming.map_names(hamming.sums(acc, key='permissions'))        

# show is nicely in json
print(json.dumps(mapd_sums, indent=4))
