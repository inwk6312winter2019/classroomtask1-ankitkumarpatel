# This is a program for traversing content of home folder as a part of classroom task1

#    printing current working directory

import os

path_to_home ='/home/ankit'

print ("Content of Home directory:",end="\n\n\n")


def directory_content(directory):

    for item in os.listdir(directory):
        
        path = os.path.join(directory,item)
        if os.path.isfile(path):
            print(path)

        else:
            directory_content(path)

directory_content(path_to_home)
