import sys
from threading import *
import thread
import socket
import time
intermediate_socket=[]
intermediate_address=[]
s111=0
music_list=['b.mp3']
def givemusic(a):
	size=a.recv(100)
	a.send("ok")
	music_send=a.recv(int(size))
	f1=open(music_send.strip(),"r")
	f2=f1.read()
	len1=len(f2)
	a.send(str(len1))
	a.recv(100)
	for i in range(0,len(f2)-1,(len(f2)//5)):
			time.sleep(3)
			a.send(f2[i:i+((len(f2)//5))])
			print(([i+((len(f2)//5))]))
	a.send("bye")
def send():
	so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	so.bind(('10.30.7.108',5000))
	so.listen(5)
	while True:
		a,b=so.accept()
		thr=thread.start_new_thread(givemusic,(a,))
def newconn(address,music_request):
	def m1():
		import subprocess
		subprocess.call(['mpg123','0.mp3'])
		
		
	so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	so.connect((address,5000))
	so.send(str(len(music_request)))
	so.recv(100)
	so.send(music_request)
	len1=so.recv(100)
	len1=int(len1)
	so.send("ok")
	ans=so.recv(int(len1//5))
	n=open('0.mp3','w+')
	i=0
	while ans!="bye":
				n.write(ans)
				print(i+((len1//5)))	
				if(i==0):		
					t1=Thread(target=m1,args=())		
					t1.start()
					i+=1
				ans=so.recv((len1//5))
	
	
	print("written")
def req():
	global s111
	so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	so.connect(('10.30.7.109',1234))
	k=0
	server_music=[]
	def m1():
		import subprocess
		subprocess.call(['mpg123','0.mp3'])
		
	
	size=so.recv(100)
	print(size)
	size=int(size)
	so.send("ok")
	total_music=so.recv(size)
	print("server music's")
	print(total_music)	
	while(True):
		n=open("0.mp3","w+")
		music_request=raw_input("enter request music")
		if(music_request.strip()=="close"):
				s111=1	
				so.send("cl")
				sys.exit()		
		len1=len(music_request)
		so.send(str(len1))
		so.recv(100)
		so.send(music_request)
		response_of_requested_music=so.recv(100)
		if(response_of_requested_music.strip()=="true"):
			size=so.recv(100)
			size=int(size)
			so.send("ok")			
			ans=so.recv(int(size//5))
			i=0
			t1=Thread(target=m1,args=())
			while ans!="bye":
					n.write(ans)
					print(i+((size//5)))	
					if(i==0):		
		
						t1.start()
						i+=1
					ans=so.recv((size//5))
	
			
			print("written")
			while t1.isAlive():
				continue
		else:
			so.send("ok")
			ans=so.recv(100)
			if(ans.strip()=="true"):
				so.send("ok")
				ans=so.recv(100)
				ans=int(ans)
				so.send("ok")
				address=so.recv(ans)
				thre=thread.start_new_thread(newconn,(address,music_request))
				
			else:
				print("music not found")
def music_available(a,b):
	global music_list
	len1=a.recv(100)
	a.send("ok")
	search=a.recv(int(len1))
	if(search.strip() in music_list):
		a.send("true")
	else:
		a.send("false")		
def res():
	so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	so.bind(('10.30.7.108',4000))#change to 1
	so.listen(5)
	while True:
		a,b=so.accept()
		t11=thread.start_new_thread(music_available,(a,b))
t1=thread.start_new_thread(req,())
t2=thread.start_new_thread(res,())
t3=thread.start_new_thread(send,())
while s111==0:
	continue
