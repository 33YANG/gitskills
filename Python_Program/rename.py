#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = '33YANG'

import os

renameFolder = 'IT2_test_log'; # rename file folder
renameRule = ['(0)', ''];      # input replace rule [0] ===> [1]

myPath = os.path.abspath(__file__);
mydir = os.path.dirname(myPath);
renameFolder = os.path.join(mydir, renameFolder);
count = 0;

def fileRename(folder, rule):
	global count;
	files = os.listdir(folder);
	for name in files:
		if os.path.isdir(os.path.join(folder, name)):
			fileRename(os.path.join(folder, name), rule);
		newName = name.replace(rule[0], rule[1]);
		if name != newName:
			print(name, '===>', newName);
			os.rename(os.path.join(folder, name), os.path.join(folder, newName));
			count += 1;
		
if __name__ == "__main__":
	try:
		fileRename(renameFolder, renameRule);
		print('=== Success! Under the rule Total', count, 'file rename done ===');
	except Exception as e:
		print('Error:', e);
	finally:
		os.system('pause');