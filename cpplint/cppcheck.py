import os
import sys

program_name = 'cpplint.py'
dir_path = 'E:/aISP/Code/aisp_sw_2.0/aisp/src/obc/'

fileter = '--filter=-whitespace/braces'

extensions = ('.cpp', '.h', '.hpp', '.cc')

filelist = []

# print type(extensions)

for file_name in os.listdir(dir_path):
    if file_name.endswith(extensions):
        filelist.append(dir_path + file_name)

sys.argv = [program_name] + [fileter] + filelist

# print filelist
	
execfile(program_name)
