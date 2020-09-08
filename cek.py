#!/usr/bin/python
import smtplib
import time
import os
import requests
import sys
import random
os.system('rm -rf .txt')
for n in range(1):

    cod = random.randint(111111, 999999)
    
    sys.stdout = open('.txt', 'a')

    print(cod)

    sys.stdout.flush()

nom = []

numer = ["0", "1", "2", "3","4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22" "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]

def get_one_random_kode(cod):
        cod = ('.txt')
        for line in open(cod,"r").readlines():
                return cod[random.randint(0, len(cod)-1)]

def get_one_random_number(nom):
        return nom[random.randint(0, len(nom)-1)]

def cek():
    for i in range(0,1):
         one_number = str(get_one_random_number(nom))
         one_kode = str(get_one_random_kode(cod))         
         print(one_number + " => "  + one_kode)

def main():                
    cek()

os.system('clear')
os.system('figlet CEK FB')
nom = raw_input("\033[1;93mNOMOR HP \033[1;97m: ")

if __name__=='__main__':
	main()
