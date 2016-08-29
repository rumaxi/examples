import youtubeAPI
import redisCache as cache


def getVideo(query):
    cacheSearch = cache.getVideo(query)
    if cacheSearch:
         return cacheSearch
    data = youtubeAPI.getVideo(query)
    cache.setVideo(query, data)
    return data

