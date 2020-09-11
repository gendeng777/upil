#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib
os.system('rm -rf .txt')
for n in range(1):

    kode = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')

    print(kode)

    sys.stdout.flush()


def log():
        os.system('clear')
        print
        use = raw_input('\033[1;96m[+] \033[1;96mNO HP Anda \033[1;97m: ')
        code = open('.txt', 'a'),use
        
        print'sukses verifikasi kode :' + use + code

if __name__=='__main__':
        log()
