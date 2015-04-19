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

fp = open('datasets/2k13_all_by_term.json', 'r')
android_apps = json.load(fp)
fp.close()

hamming = compare.Hamming()

# get single search term
# hamming.bin_transform(android_apps['facebook'], 'permissions')
# print(hamming.hamming_dist(10))

# mapd_sums = hamming.map_names(hamming.sums())
# print(json.dumps(mapd_sums, indent=4))

stats = {}
# show all search terms
for key in android_apps.keys():
    hamming.bin_transform(android_apps[key], 'permissions')
    stats[key] = hamming.hamming_dist(10)

sl = sorted(stats.items(), key=operator.itemgetter(1), reverse=True)

# top 10 search that show most sparatic use of permissions
for stat in sl[:10]:
    print(stat[0] + ": %.2f" % stat[1])
