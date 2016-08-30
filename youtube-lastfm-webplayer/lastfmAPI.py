#!/usr/bin/python3
import urllib3
import settings as s
import json
import hashlib

class Record:
    def __init__ (self, userid, title, body):
        self.userid = userid
        self.title = title
        self.body = body


class Track:
    def __init__ (self, artist, name):
        self.artist = artist
        self.name = name
    def __repr__(self):
         return self.artist+' - '+self.name
'''
url = { 'test'  :   'http://jsonplaceholder.typicode.com/posts',
        'auth' :   'http://www.last.fm/api/auth/?', #api_key=xxx
        'getTopTracksByTag': 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag=disco&api_key=cbcdba24cc747a9b489c313ca3e05787&format=json
        }


'''

UrlTag = { 'topTracks': 'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&format=json' # &tag=disco&api_key=cbcdba24cc747a9b489c313ca3e05787&
        }


def getTopTracksByTag (tag):
    if s.PROXY:
        http = urllib3.proxy_from_url(s.PROXY)
    else:
        http = urllib3.PoolManager()

    url = UrlTag['topTracks']+'&tag='+tag+'&api_key='+s.lfmAPIKey
    try:
        req = http.request('GET', url)
    except Exception as e:
        print ("Exception: "+str(e)) 
        return None
    data = json.loads (req.data.decode('utf-8'))
    resp = []
    for obj in data['toptracks']['track']:
        resp.append ( obj['artist']['name']+' - '+obj['name'] )
    return resp



#auth_url = url['auth'] + 'api_key=' + APIKey
#r = http.request('GET', auth_url)

''' some auth magic #
 sig_string = "api_key" + APIKey + "methodauth.getSessiontoken" + APIToken + APISecret
coder = hashlib.md5()
sig_md5 = hashlib.md5(sig_string.encode('utf-8')).hexdigest()
'''


'''
r = http.request('GET',url['test'])
data = json.loads(r.data.decode('utf8'))
res_set = []
for obj in data:
    res_set.append ( Record(userid = obj['userId'], title = obj['title'], body = obj['body']) )


for i in res_set:
    print (i.userid)

'''
