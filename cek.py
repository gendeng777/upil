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


class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

nom = []

numer = ["0", "1", "2", "3","4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22" "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90"]

def get_one_random_domain(domains):
        return domains[random.randint( 0, len(domains)-1)]

def get_one_random_number(numer):
        return numer[random.randint(0, len(numer)-1)]

def em():
    for i in range(0,50):
         one_number = str(get_one_random_number(numer))
         one_domain = str(get_one_random_domain(domains))         
         print(nama + one_number  + "@" + one_domain)

def main():                
    randomemails()

os.system('clear')
os.system('figlet CEK FB')
nom = raw_input("\033[1;93mNOMOR HP \033[1;97m: ")
codlist = ('.txt')
	for line in open(codlist,"r").readlines():
		cod.append(line.strip())
except IOError:
	print ("[!] File Not Found")
	raw_input("\n[ Back ]")
	menu()


if __name__=='__main__':
	main()
