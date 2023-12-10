#!/usr/bin/env python3

# Script Name:                  Python Conditionals
# Author:                       David Renteria
# Date of latest revision:      12/08/2023
# Purpose:                      File handling

# Import libraries
import os

# Declaration of variables
test_file = "test.txt"
# Create the file and appends/adds 3 lines
with open(test_file, "w") as file2: # opening file and stashing in the file2 variable that lives online inside of the with statement
    file2.write("First line\n")
    file2.write("Second line\n")
    file2.write("Third line\n")
#print the first line
with open(test_file, "r") as file2:
    line_one = file2.readline().strip()
    print(line_one)
# Delete the file
os.remove(test_file)

# Call function


# End