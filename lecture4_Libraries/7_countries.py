# did it from scratch, no spoon feeding. YAY!

import sys
import json
import requests

if len(sys.argv)!=2:
    sys.exit("wrong set of arguments")
region=sys.argv[1]
response=requests.get(f"https://restcountries.com/v3.1/region/{region}?fields=name,capital,population")
res=response.json()
for country in res:
    print(f"{country['name']['common']} - Capital: {country['capital']} - Population: {country['population']}")