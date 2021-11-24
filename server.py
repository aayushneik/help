
from os import system
system("pip install  amino.fix")
import aminofix
import requests
from threading import Thread as t
clint=aminofix.Client()
clint.login(email="q7tfudy5@wwjmp.com",password="pagal0")
headers=clint.headers
x=clint.get_from_code(code="http://aminoapps.com/p/jslh9c")
com=[]
x1=clint.get_from_code(code="http://aminoapps.com/c/Btsarmy")
comId=x.path[1:x.path.index('/')]
chatId=x.objectId
subclint=aminofix.SubClient(comId=comId,profile=clint.profile)
subclin=aminofix.SubClient(comId=x1.path[1:x1.path.index('/')],profile=clint.profile)
userI=[]
s=0
size=100
while (s!=1500):
		user=subclin.get_all_users(start=s,size=size).profile.userId
		for o in user:
			userI.append(o)
		s+=100
		size+=100
print(userI)
def lag():
	for i in range(100):
			try:
				subclint.edit_chat(chatId=chatId,coHosts=userI)
			except:
				print("Invite....Cohost")
def all():
	while True:
		t(target=lag).start()
all()
