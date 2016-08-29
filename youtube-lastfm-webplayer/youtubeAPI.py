#!/usr/bin/python3
#import urllib3
import requests
import settings as s
#import json

URL = { 'search': 'https://www.googleapis.com/youtube/v3/search?part=id', #&q=... &key={YOUR_API_KEY}

        }


http = requests.Session()
def getVideo (query):
    if s.PROXY:
        http.proxies = {'http'  : s.PROXY,
                        'https' : s.PROXY
                }
    url =   URL['search']                 + \
            '&q='     + query             + \
            '&key='   + s.ytAPIKey        + \
            '&order=' + 'viewCount'       + \
            '&videoEmbeddable=' + 'true'  + \
            '&videoSyndicated=' + 'true'  + \
            '&type='            + 'video' + \
            '&videoDuration='   + 'medium'
#            '&videoDefinition=high'

    # TODO: videoDefinition = high / standard / any
    r = http.get (url)
    data = r.json()
    results = data['items']
    if results:
        resp = results[0]['id']['videoId']
        return resp 
    print ("No video :(")
    return None

