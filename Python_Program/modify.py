#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a plugin program about modify files content under specific rules
__author__ = 'liyang'
__date__ = '2019-5-28'

import os
import re

# get current file path
myPath = os.path.abspath(__file__)
mydir = os.path.dirname(myPath)

# cause this program can't read '.c' file, so change file font to '.txt' to read and modify, at last back to '.c' font export;
fileExt = ('.c', '.txt')

# put all modify rule in this array
replaceRule = ['GTCHAR', 'const GTCHAR', '[] =', '[] __attribute__((section(".rodata_STR_DATA"))) =', '[]=', '[] __attribute__((section(".rodata_STR_DATA"))) = ', '#pragma _section C=STR_DATA', '#pragma _section C', 'GResString']
pattern = [r'^\*\**\/', 'GSimpleFont']

# count the number of modify files
count = 0

# export　path
exportDir = os.path.join(mydir, 'export')

class modify(object):
	# function init
	def __init__(self):
		# make export file directory
		if not os.path.exists(exportDir):
			os.mkdir('export')
		self.getFiles()
		
	# get all files in current path
	def getFiles(self):
		global count
		files = os.listdir(mydir)
		for name in files:
			if name.endswith(fileExt[0]) and replaceRule[8] in name:
				count += 1
				replaceName = name.split('.')[0] + fileExt[1]
				# because this program can't read .c file, so change file font to .txt to read and modify, at last back to .c font export;
				os.rename(os.path.join(mydir, name), os.path.join(mydir, replaceName))
				self.addModify(name, replaceName)
				# back source file ext to original
				os.rename(os.path.join(mydir, replaceName), os.path.join(mydir, name))
				print('=== Modifing file ', os.path.join(mydir, name), '===')
				
	# modify string
	def addModify(self, name, replaceName):
		exportFile = os.path.join(exportDir, replaceName)
		sourceFile = os.path.join(mydir, replaceName)
		
		if os.path.exists(os.path.join(exportDir, name)):
			os.remove(os.path.join(exportDir, name))

		with open(sourceFile, 'r') as f:
			with open(exportFile, 'w') as f1:
				while True:
					line = f.readline()
					if re.match(pattern[0], line):
						newLine = line + replaceRule[6]
					elif pattern[1] in line:
						newLine = line.replace(replaceRule[4], replaceRule[5])
					else:
						newLine = line.replace(replaceRule[0], replaceRule[1]).replace(replaceRule[2], replaceRule[3])
					f1.writelines(newLine)
					# while reach the file end
					if not line:
						f1.writelines(replaceRule[7])
						break
		# back file ext to original
		os.rename(exportFile, os.path.join(exportDir, name))

if __name__ == "__main__":
	try: 
		string = modify()
		print('\n=== Success! Under the rule Total', count, 'file modified done ===\n\n=== Export path at:', exportDir, '===\n')
	except Exception as e:
		print('---Error---\n', e)
	finally:
		os.system('pause')