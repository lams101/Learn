#!python3
import re,sys,os
regexobject=re.compile(r'(.*)(Prerequisite:.*)(\w\w\w \d\d\d)|(\w\w\w \d\d\d.*)|(\(.*\))')
keys=['Course Name','Credit Hours','Descritpion','Prereqs']
dick=dict()
i=0
fhand=open(r'c:\users\lamine\pyscripts\collegefiles')
for line in fhand: 
	MO=regexobject.search(line)
	if len(MO.group(0)) < 45:
		dick[keys[i]]=MO.group(0)
		i=i+1
		print (dick)
		os.system('pause')
	elif len(MO.group(0)) > 45
		print(MO.group(0))
		print(MO.group(1))
		print(MO.group(2))	
		print(MO.group(3))

	# dick[keys[i]]=MO.group(0)
	# i=i+1
	# print(dick)


#	if len(MO)> 40:


	# if MO==None: 
	# 	print (line,'\n')
	# 	x=line
	# 	continue
	# print (MO.group(0),'\n',MO.group(1),'\n',MO.group(2),'\n',MO.group(3),'\n')
	




