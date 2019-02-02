# This is a program for traversing content of home folder as a part of classroom task1

#    printing current working directory

import os
cwd = os.getcwd()
print("Current working directory: ",cwd,end="\n\n\n")

#    printing whole content(all files and folders listed) of home directory

print ("Content of Home directory:",end="\n\n\n")

for item in os.listdir('/home/ankit'):
    print(item)

#    printing only files of home directory

print ("Files only of Home directory:",end="\n\n\n")

for item in os.listdir('/home/ankit'):

    if os.path.isfile(item):
        print(item)

#    printing only Folders of home directory

print ("Folders only of Home directory:",end="\n\n\n")

for item in os.listdir('/home/ankit'):

    if os.path.isdir(item):
        print(item)

