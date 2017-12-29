#!/usr/bin/python

import subprocess


#.call is a thin wrapper around Popen. the main difference is that 
# call will wait for the process to finish before it returns whereas
# Popen can continue doing other things while the subprocess is running
#subprocess.call(['ps', 'aux'])

dirRaw = subprocess.check_output(['ls'])


dirList = dirRaw.split('\n')
dirList.remove('')
#for item in dirList:
#	print item	


handle = subprocess.Popen("ls", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

handle.stdout.read()
