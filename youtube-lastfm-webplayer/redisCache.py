import redis

'''
REDIS DATABASES:
    0 - TopTracksByTag
    1 - YoutubeVideo
    2
    3
    4
    5
    6
    7
    8
'''

_TopTracksByTagDb   = redis.Redis(host='localhost', port=6379, db = 0)
_YoutubeVideoDb     = redis.Redis(host='localhost', port=6379, db = 1)

def getTopTracksByTag (tag):
    cacheSize = _TopTracksByTagDb.llen(tag)
    resp = []
    if cacheSize:
        for i in range(cacheSize):
            resp.append (_TopTracksByTagDb.lindex(tag,i).decode('utf-8'))
    return resp 

def setTopTracksByTag (tag, tracks):
    for track in tracks:
        _TopTracksByTagDb.lpush(tag, track)
    return True


def getVideo(query):
    resp = _YoutubeVideoDb.get(query)
    if resp:
        resp = resp.decode('utf-8')
    return resp


def setVideo(query, url):
    _YoutubeVideoDb.set(query, url)

