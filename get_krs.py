from urllib.request import urlretrieve
import json

for page in range(1, 200+1):
    url = 'https://rejestr.io/api/search.json?page={}&perPage=10000&app=krs'.format(page)
    fname = 'krs_dump/page_{}.json'.format(page)
    urlretrieve(url, fname)
    print("\r{}".format(page), end="")
