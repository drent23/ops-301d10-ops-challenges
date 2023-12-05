# Assign variable
user = 'David'

# Output to screen
# print('Hello, my name is: ')
# print(user)

# Concat
# print('Hello, my name is ' + user)

# Input data
# print(user)
# user = input('Please enter your name: ')
# print(user)

# Imports
import os # Hold 'cmd' key while clicking on 'os' to see more

# Bash things in Python
# os.system('ls -la')
# os.system('ip a')

# How through python can you execute a bash script?? (Google it)

# Functions
def py_to_linux_function():
    os.system('ls -la')
    os.system('ip a')

# Call/invoke functiion
py_to_linux_function()

# Python runs through entire code looking for errors before running, so don't use other languages syntax, ie '$' in Bash