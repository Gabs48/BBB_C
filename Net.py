#!/usr/bin/env python

import httplib
import socket
from PIL import Image

def streamGet(host, port, query):
	"Gets the video file from the specified host, port and location"
	try:
		h = httplib.HTTP(host, port)
		h.putrequest('GET', query)
		h.putheader('Host', host)
		h.putheader('User-agent', 'python-httplib')
		h.putheader('Content-type', 'image/jpeg')
		h.endheaders()
	except (httplib.HTTPException, socket.error) as ex:
		print "Error: %s" % ex
		f = open("includes/No_stream2.jpeg")
		return f.read()
	
	(returncode, returnmsg, headers) = h.getreply()
	if returncode != 200:
		print returncode, returnmsg
		f = open("includes/No_stream2.jpeg")
		return f.read()
		
	f = h.getfile()
	return f.read()

