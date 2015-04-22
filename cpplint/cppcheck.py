import os
import sys

program_name = 'cpplint.py'
dir_path = 'E:/aISP/Code/aisp_sw_2.0/aisp/src/obc/'
extensions = ('.cpp', '.h', '.hpp', '.cc')

argvlist = []

# print type(extensions)

for file_name in os.listdir(dir_path):
    if file_name.endswith(extensions):
        argvlist.append(dir_path + file_name)

sys.argv = [program_name] + argvlist

# print argvlist

execfile(program_name)
