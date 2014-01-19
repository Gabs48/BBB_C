#!/usr/bin/env python

import httplib
import socket
import pickle
from PIL import Image

def get_video_stream(host, port, query):
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

class NetToolClient:
	"Tools used for string and object transfer over internet"
	BUF = 1024
	
	def __init__(self, host_='10.193.242.75', port_=50007):
		"Class initialization"
		self.host = host_;
		self.port = port_;
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		
	def set_host(self, host_, port_):
		"Set the hostname and the port of the server"
		self.host = host_;
		self.port = port_;
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		
	def connection(self):
		"Connect the client to the server"
		try:
			self.s.connect((self.host, self.port));
		except (socket.error) as ex:
			print "Error: %s" % ex
			return -1
	
	def send_str(self, msg):
		"Send a string message to the server"
		self.s.send(msg);
	
	def receive_str(self):
		"Receive a string message from to the server"
		msg = self.s.recv(self.BUF);
		return msg;
	
	def send_obj(self, obj):
		"Send a generic object obj to the server"
		msg = pickle.dumps(obj);
		self.s.send(msg);
		
	def receive_obj(self):
		"Receive a generic object obj from the server"
		msg = self.s.recv(self.BUF);
		return pickle.loads(msg)
		
	def deconnection(self):
		"Deconnect the socket"
		self.s.close();


class NetToolServer:
	"Tools used for string and object transfer over internet"
	BUF = 1024
	
	def __init__(self, port_=50007):
		"Class initialization"
		self.port = port_;
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		self.s.bind(('', self.port))
		self.addr = []
		
	def set_host(self, host_, port_):
		"Set the hostname and the port of the server"
		self.host = host_;
		self.port = port_;
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		self.s.bind(('', self.port))
		
	def wait_conn(self):
		"Wait for one (and just one) connection"
		self.s.listen(1)
		self.conn, self.addr = self.s.accept()
	
	def get_addr(self):
		"Return the string adress of the connected client if exists"
		if addr:
			return self.addr
		else:
			return -1
		
	def send_str(self, msg):
		"Send a string message to the server"
		self.conn.send(msg);
	
	def receive_str(self):
		"Receive a string message from to the server"
		msg = self.conn.recv(self.BUF);
		return msg;
	
	def send_obj(self, obj):
		"Send a generic object obj to the server"
		msg = pickle.dumps(obj);
		self.conn.send(msg);
		
	def receive_obj(self):
		"Receive a generic object obj from the server"
		msg = self.conn.recv(self.BUF);
		return pickle.loads(msg)
		
	def deconnection(self):
		"Deconnect the socket"
		self.s.close();
		self.conn.close();
		self.addr = []