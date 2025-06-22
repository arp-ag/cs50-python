# rough practice 5:-

# APIs (application programming services)
# requests package (make web req, internet requests, http, https)

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

o=response.json()
for result in o['results']:
    print(result["trackName"])