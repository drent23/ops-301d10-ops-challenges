#!/usr/bin/env python3

# import libraries
import os

# Get user input and put into a variable
user_directory = input("Please enter the directory name you wish to view: ")
# Declare a function
def get_directory():
    for (root, dirs, files) in os.walk(user_directory):
        # command to print root directory
        print(root)
        # command to print folders
        print(dirs)
        # command to print files
        print(files)

# Call the function
get_directory()