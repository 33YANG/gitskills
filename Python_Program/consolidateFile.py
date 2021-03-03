#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a plugin program about consolidate folder file to one file, please put this file in your project root folder and run
__author__ = '33YANG'
__date__ = '2020-5-29'

import os
import re
import time

mydir = os.getcwd() # get current directory
# mydir = os.path.abspath(os.path.join(os.getcwd(), '..')) # get superior directory

print('please put this file in your project root folder and run!\n')

# ignore part of files, directories
ignoreFile = ('yarn-error.log', 'yarn.lock')
ignoreRegExp = (r'^.*.png$', r'^.*.jpg$')
ignoreFolder = ('node_modules', 'dist', '.vscode', '.git', 'export')

# the export file location
exportFolder = os.path.join(mydir, 'export')
exportFile = os.path.join(exportFolder, 'consolidateFile.txt')

# count the all handled files
count = 0
beginTime = time.time()

class Consolidate():

  allFilePath = []
  
  # init, filter ignore and consolidata project files
  def __init__(self):
    files = filter(self.filterDirectory, os.listdir(mydir))
    self.getAllFiles(files, mydir)
    self.allFilePath = filter(self.filterFile, self.allFilePath)
    self.consolidateAllFiles()

  # filter ignore directories
  def filterDirectory(self, arg):
    if arg in ignoreFile or arg in ignoreFolder:
      return False
    else:
      return True

  # filter ignore files
  def filterFile(self, arg):
    if re.match(ignoreRegExp[0], arg) or re.match(ignoreRegExp[1], arg):
      return False
    else:
      return True

  # recursive get all files path
  def getAllFiles(self, files, currentPath):
    for name in files:
      current = os.path.join(currentPath, name)
      print('\r --- waiting... cost', round(time.time() - beginTime, 2), 's ---', end='')
      if os.path.isdir(current):
        newCurrentPath = current
        self.getAllFiles(os.listdir(newCurrentPath), newCurrentPath)
      else:
        self.allFilePath.append(current)
    return

  # open files one by one, and concat to one file
  def consolidateAllFiles(self):
    global count
    if not os.path.exists(exportFolder):
      os.mkdir(exportFolder)
    if os.path.exists(exportFile):
      os.remove(exportFile)
    with open(exportFile, 'w', encoding='utf-8', errors='ignore') as ef:
      ef.write('cwd ' + mydir + '\n\n')
      for filePath in self.allFilePath:
        print('\r --- waiting... cost', round(time.time() - beginTime, 2), 's ---', end='')
        with open(filePath, 'r', encoding='utf-8', errors='ignore') as fp:
          ef.write('File ' + filePath.replace(mydir, '') + ' start...\n')
          ef.write(fp.read())
          ef.write('\nFile ' + filePath.replace(mydir, '') + ' end...\n')
          count += 1

if __name__ == "__main__":
	try:
		Consolidate()
		print('\n\nSuccessful, consolidate', count, 'files in total')
		print('\nexportFile = ', exportFile, '\n')
	except Exception as e:
		print('\n---Error---\n', e)
	finally:
		os.system('pause')

