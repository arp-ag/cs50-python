# rough practice 5:-

# APIs (application programming interface)
# requests package (make web req, internet requests, http, https)

# https://itunes.apple.com/search?entity=song&limit=1&term=weezer : made with ref to apple's API doc
# this gives a standard text format called json
# entity- what to search, limit- how much data(song), term- artist/band
# THIS IS API : A mechanism by which I can access data on someone else's server
# and somehow integrate it into my own program.

# JSON (java script object notation)  

import json
import requests
import sys
if len(sys.argv)!=2: # file name + band name
    sys.exit()
response=requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ sys.argv[1])

""" print(response.json()) # converts into dict. """

# import json
""" print(json.dumps(response.json(), indent=2)) """ 
# dumps= dump string [pretty prints]
# indent=2 [named parameter]

# check image attached
o=response.json() # stores the json response
for result in o['results']:
    print(result["trackName"])