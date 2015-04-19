# If module is laoded then reload it otherwise
# catch the exception and import the module
try:
    compare
    reload(compare)
except NameError:
    from utils import compare

import json
import os

fp = open('datasets/2k13_all_by_term.json', 'r')
android_apps = json.load(fp)
fp.close()

hamming = compare.Hamming()
 
hamming.bin_transform(android_apps['facebook'], 'permissions')
print(hamming.hamming_dist(10))

# mapd_sums = hamming.map_names(hamming.sums())

# print(json.dumps(mapd_sums, indent=4))



