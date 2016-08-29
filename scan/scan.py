#!/usr/bin/python3

from datetime import datetime
import socket
import sane
import os

''' settings '''

PORT		= 9823
IMG_DIR		= '/tmp/Scan/'
RESOLUTION	= 300

''' subs '''

def uniq_filename (scan_opt):
	dt = datetime.utcnow()	
	timestamp = dt.strftime('%Y%m%d_%H%M%S') 
	ext = '.jpg' if scan_opt['color'] else '.tif'
	fn = IMG_DIR+'_'.join((scan_opt['objid'], '0001', timestamp, scan_opt['objtype']))+ext
	return fn

def scan (conn, query):
	scan_opt = { 'objid': query[1], 'objtype': query[2], 'color': int(query[6])+1 } # int(q[6])+1: -1|0 + 1 = 0|1 -> boolean
	scanner.mode = 'Color' if scan_opt['color'] else 'Gray'
	scanner.resolution = RESOLUTION
	fn = uniq_filename(scan_opt)
	im = scanner.scan()
	im.save(fn)
	os.chmod(fn, 0o777)
	conn.send(b'SAVE_SCAN_OK\n')

handler = {	 'GET_VERSION': lambda conn, query: conn.send(b'200\n'),
			'SCAN':	lambda conn, query: scan(conn, query),
			'QUIT': lambda conn, query: conn.send(b'QUIT_OK\n')	}

''' here we go  '''

print ('SANE Initialization...')
sane.init()
devs = sane.get_devices()
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
	scanner = sane.SaneDev(devs[0][0])
	sock.bind(('',PORT))
except IndexError:
	print ("No scanner found.")
except OSError:
	print ("Can't bind to "+str(PORT))
else:
	print  ('Using '+' '.join(devs[0]))
	sock.listen(1)
	print ('Listening on '+str(PORT)) 

	while True:
		conn, addr = sock.accept()
		while True:
			data = conn.recv(1024)
			if not data:
				break
			query = data.decode('utf-8').split()
			handler[query[0]](conn, query)
	conn.close()
