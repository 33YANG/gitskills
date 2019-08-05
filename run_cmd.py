#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

try:
	p = os.popen('cd C:\WinAMS\BIN')
	q = os.popen('SSTManager.exe')
	print(p, q)
except Exception as e:
	print(e)
finally:
	os.system('pause')

# def runCommand():