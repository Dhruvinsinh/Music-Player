import socket
import thread
import time
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.bind(('127.0.0.1',1234))
so.listen(5)
c_o=[]
address=[]
music_server=['payback.mp3']

	
def musicsend(a,b):
	def searchinpeer(a,b,music_requested):
		global c_o,address
		status=0
		address1=0
		for i in c_o:
			if i!=a:
				index=c_o.index(i)
				address1,port=address[index]
				request_broad=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
				request_broad.connect(('127.0.0.1',4000))
				len1=len(music_requested)
				request_broad.send(str(len1))
				request_broad.recv(100)	
				request_broad.send(music_requested)
				resp=request_broad.recv(100)
				if(resp.strip()=="true"):
					status=1
					break
		return status,address1
		status=0
	global music_server
	len1=len(music_server)
	s=""
	for i in range(0,len1):
		s=s+music_server[i]
		s=s+","
	print(s)
	len1=len(s)
	a.send(str(len1))
	a.recv(100)
	a.send(s)
	while True:
		status=0
		size1=a.recv(100)
		print(size1)
		size1=size1.strip()
		if(size1=="cl"):
			break
		a.send("ok")
		music_requested=a.recv(int(size1))
		if(music_requested.strip() in music_server):
				status=1
		if(status==1):
			a.send("true")
			a1=open(music_requested,"r")
			a2=a1.read()
			print(len(a2))
			len1=len(a2)
			len1=str(len1)
			a.send(len1)
			a.recv(100)
			for i in range(0,len(a2)-1,(len(a2)//5)):
				time.sleep(3)
				a.send(a2[i:i+((len(a2)//5))])
				print(([i+((len(a2)//5))]))
			a.send("bye")
			
		

		else:
			a.send("false")
			a.recv(100)
			status,address1=searchinpeer(a,b,music_requested)
			if(status==1):
				a.send("true")
				a.recv(100)
				a.send(str(len(address1)))
				a.recv(100)
				a.send(address1)
			else:
				a.send("false")
		
while True:
	a,b=so.accept()
	c_o.append(a)
	address.append(b)
	t1=thread.start_new_thread(musicsend,(a,b))	


                                                                                                                                                                
