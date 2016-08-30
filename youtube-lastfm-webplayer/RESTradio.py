#!/usr/bin/python3


from flask import Flask, render_template
import lastfmDAO as lastfm
import youtubeDAO as youtube
import radioDAO as radio
import random

app = Flask (__name__)
app.config.update(DEBUG = True)


@app.route('/')
def RESTroot():
#    bg = random.randint(1,5)
    bg = 5
    return render_template('index.html', bg=bg)

@app.route ('/randomvideo')
def RESTrandomvideo():
        return radio.randomVideoId()

@app.route ('/json/ambient')
def RESTjsonAmbient():
    return radio.randomAmbient()


'''
@app.route('/toptracksbytag/<tag>')
def RESTgetTopTracksByTag(tag):
    if not tag: 
        tag = 'rock'
#    tracks = lastfm.getTopTracksByTag(tag)
    resp =  lastfm.getTopTracksByTag(tag)
#    return lastfm.getTopTracksByTag(tag)
    return "<br>".join(resp)
'''
'''
@app.route ('/youtubesearch/<query>')
def RESTyoutubeSearch(query):
    resp = youtube.search (query)
    return resp
'''
#@app.route ('/getYoutubeUrl/<track>')
#def RESTgetYoutubeUrl(track):
'''
@app.route ('/tag/<tag>')
def RESTtag(tag):
    return radio.getVideoByTag(tag)
'''
'''
@app.route ('/random')
def RESTrandom():
        video = radio.randomVideo()
        return render_template('index.html', video=video)
'''






if __name__ == "__main__":
    app.run()
