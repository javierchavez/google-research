# Comparing permissions #

Uses **Python 3.4**

###Note:

I am aware the file `all_by_term.json` is not valid json. I am using it to
persist data as serialized objects to be read back into memory. The structure makes it
easier to locate serch terms and the apps that belong, especially when
trying to compute average hamming distance.

###Useage

######getting a single app

This assumes you know the exact package id
```python
app = ps.get_app('com.some.name')
# suggest leaving out reviews its a lot of data
app.populate_fields(exclude=['reviews'])
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
apps = ps.search('google', 1).get_results()
# iterate through the apps populate
# populate apps fields and convert to dict
for app in apps:
    app.populate_fields(exclude=['reviews'])
    apps_array.append(app.to_dict())
    hamming.accumulate([app])

    
# turn the permissions into boolean matrix 
hamming.bin_transform_inplace(apps_array, key='permissions')

# show the hamming distance for n apps
print(hamming.hamming_dist(apps_array, 20))
```

######hamming sum with keys

cont. from above

```python
# tally all the permissions usage and map to names
mapd_sums = hamming.map_names(hamming.sums())
# show is nicely in json
print(json.dumps(mapd_sums, indent=4))
```

**Note to myself (and others).**
somthing interesting about counting permissions, I ran into a huge 'bug'
where I thought my program was missing permissions and failing to
account for a permission in a given app. for some reason you, like I
did, may have duplicate permissions with in the app instance, it caused me to go
insane thinking my `Hamming class` was garbage.
