#!/usr/bin/python
import os
while True:
	print ("1: interact")
	print ("0: exit")
	action= input("choose an option \n")
	if action == "1":
		name= input("enter the file name here \n")
		print ("1: create / edit file")
		print ("2: remove file")
		check= input("choose one option \n")
		if check == "1":
			filename= os.path.exists(name)
			if filename == True:
				file=open(name , "a")
			else:
				file= open(name , "x")
			write= input("enter something you want to save \n")
			file.write(write)
	
			file.close()

		else:
			os.remove(name)
	else:
		exit()
