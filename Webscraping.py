#!python3
import requests, re, sys, os
from bs4 import BeautifulSoup
from selenium import webdriver

req= requests.get('http://www.bradley.edu/academic/undergradcat/20152016/')
soup=BeautifulSoup(req.content,'lxml')
soup.find_all('a')
Collegelinx=[]
Collegepagez=[]
Collegefiles=open(r'c:\users\lamine\pyscripts\collegefiles','a')
for link in soup.find_all('a'):
	y=link.get('href')
	Collegelinx.append(y)
regex=re.compile(r'.*courses\.dot')
for i in Collegelinx:
	match=regex.search(i)
	if match==None: continue
	Collegepagez.append(match.group(0))
	#print(z)
for ext in Collegepagez:
	req2=requests.get('http://www.bradley.edu/academic/undergradcat/20152016/'+ext)
	soup2=BeautifulSoup(req2.content,'lxml')
	for paragraph in soup2.find_all('p'):
		print (paragraph.text)
		os.system('pause')
		Collegefiles.write(link.text)











