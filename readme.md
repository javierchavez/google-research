# Comparing permissions #

###Useage

######getting a single app

This assumes you know the exact package id
```python
app = ps.get_app('com.some.name')
app.populate_fields()
print(json.dumps(app.to_dict(), indent=4))
```

######searching

Example searching the playstore for 'twitter'
```python
apps = ps.search('twitter', 1).get_results()
```

######hamming distance

```python
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
```

######hamming sum with keys

cont. from above
```python
# tally all the permissions usage and map to names
mapd_sums = hamming.map_names(hamming.sums())
# show is nicely in json
print(json.dumps(mapd_sums, indent=4))
```
