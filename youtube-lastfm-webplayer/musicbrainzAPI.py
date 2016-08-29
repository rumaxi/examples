import musicbrainzngs as mb
 
 
 
mb.set_useragent('tubeplayer', '0.1.0', 'http://www.rumaxi.net/ burov.ilya@gmail.com')
mb.set_format('xml')
 
artist_id = "c5c2ea1c-4bde-4f4d-bd0b-47b200bf99d6"
#try:
result = mb.get_artist_by_id(artist_id)
#except Exception as e: 
#     print ("belkin whoooy: "+str(e))

