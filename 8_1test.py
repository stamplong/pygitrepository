import sys
import os
file_path = os.getcwd()
print file_path
new_file_path2 = os.path.join(file_path,'123.txt')
print new_file_path2
a = ['123']
b = ['456']
c = a + b
print c
