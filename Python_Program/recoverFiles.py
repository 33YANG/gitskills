#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a plugin program about recover one txt file to original directory, please put this file in the consolidateFile.txt folder and run
# This is a mirror file of the consolidateFile.py file
__author__ = 'liyang'
__date__ = '2020-12-15'

import os
import re

consolidateFilePath = os.path.join(os.getcwd(), 'consolidateFile.txt')

regexp = [r'(File\s).*(\sstart...)', r'(File\s).*(\send...)', r'(?<=File\s\\).*(?=\sstart...)']
print(consolidateFilePath)

def readFile(path):
  with open(path, 'r', encoding='utf-8') as rf:
    isStart, isEnd = False, False
    curDir = None
    while True:
      fileline = rf.readline()
      if not fileline:
        break
      if re.match(regexp[0], fileline) != None:
        curDir = re.search(regexp[2], fileline).group()
        isStart = True
      elif re.match(regexp[1], fileline) != None:
        isEnd = True
        curDir = None
      else:
        isStart, isEnd = False, False
      if curDir != None and not isStart and not isEnd:
        fullDir = os.path.join(os.getcwd(), curDir)
        if not os.path.exists(os.path.dirname(fullDir)):
          os.makedirs(os.path.dirname(fullDir))
        with open(fullDir, 'a', encoding='utf-8') as wf:
          wf.write(fileline)

if __name__ == "__main__":
  try:
    print('Waiting...')
    readFile(consolidateFilePath)
    print('Recover Successful!')
  except:
    print('Error occur!')
  finally:
    os.system('pause')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a plugin program about recover one txt file to original directory, please put this file in the consolidateFile.txt folder and run
# This is a mirror file of the consolidateFile.py file
__author__ = 'liyang'
__date__ = '2020-12-15'

import os
import re

consolidateFilePath = os.path.join(os.getcwd(), 'consolidateFile.txt')

regexp = [r'(File\s).*(\sstart...)', r'(File\s).*(\send...)', r'(?<=File\s\\).*(?=\sstart...)']
print(consolidateFilePath)

def readFile(path):
  with open(path, 'r', encoding='utf-8') as rf:
    isStart, isEnd = False, False
    curDir = None
    while True:
      fileline = rf.readline()
      if not fileline:
        break
      if re.match(regexp[0], fileline) != None:
        curDir = re.search(regexp[2], fileline).group()
        isStart = True
      elif re.match(regexp[1], fileline) != None:
        isEnd = True
        curDir = None
      else:
        isStart, isEnd = False, False
      if curDir != None and not isStart and not isEnd:
        fullDir = os.path.join(os.getcwd(), curDir)
        if not os.path.exists(os.path.dirname(fullDir)):
          os.makedirs(os.path.dirname(fullDir))
        with open(fullDir, 'a', encoding='utf-8') as wf:
          wf.write(fileline)

if __name__ == "__main__":
  try:
    print('Waiting...')
    readFile(consolidateFilePath)
    print('Recover Successful!')
  except:
    print('Error occur!')
  finally:
    os.system('pause')

