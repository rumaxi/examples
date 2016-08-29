import lastfmDAO    as lastfm
import youtubeDAO   as youtube
import random
import tags
import json



#def getVideoByTag (tag):
#    trackno = random.randint(0,49)
#    track = lastfm.GetTopTracksByTag (tag)[trackno]
#    video = "http://www.youtube.com/watch?v="+youtube.search (track)
#    return video

'''
def randomVideo ():
    trackno = random.randint(0,49)
    tag = tags.tags[random.randint(0, len(tags.tags)-1)]
    print (tag)
    track = lastfm.getTopTracksByTag (tag)[trackno]
    video = youtube.getVideo(track)
    url = "http://www.youtube.com/embed/"+video+'?autoplay=1&controls=0&showinfo=0&rel=0'
    return url
'''


def randomVideoId ():
    video = None
    while video == None:
        trackno = random.randint(0,49)
        tag = tags.tags[random.randint(0, len(tags.tags)-1)]
        print ("TAG: %s" % tag)
        tracks = lastfm.getTopTracksByTag(tag)
        if tracks:
            track = tracks[trackno]
            video = youtube.getVideo(track)
            return video


def randomAmbient():
#    trackRes = Track()
    trackRes = {}
    video = None
    tag = tags.tags[random.randint(0, len(tags.tags)-1)]
    trackRes['tag'] = tag
    print ("TAG: %s" % tag)
    while video == None:
        trackno = random.randint(0,49)
        tracks = lastfm.getTopTracksByTag(tag)
        if tracks:
            track = tracks[trackno]
            video = youtube.getVideo(track)
            trackRes['video'] = video
            trackRes['title'] = track
            res = json.dumps(trackRes)
            print (res)
            return res
