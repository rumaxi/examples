import lastfmAPI as lastfm
import redisCache as cache

def getTopTracksByTag(tag):
    cacheSearch = cache.getTopTracksByTag(tag)
    if cacheSearch:
        return cacheSearch
#    while data == None:
    data = lastfm.getTopTracksByTag(tag)
    if data:
        cache.setTopTracksByTag(tag, data)
        return data
    return None

