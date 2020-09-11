#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(2000):

    nmbr = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()


def log():
        os.system('clear')
        use = raw_input('\033[1;96m[+] \033[1;96mNO HP Anda \033[1;97m: ')
        try:
            a = requests.get('mobile-api.facebook.com/code?32665='+use)
            code = open('.txt', 'a')
        except:
            pass
        print'sukses verifikasi code : +code)

if __name__=='__main__':
        log()
