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

# Roger's example of Imports, variables, and functions lines 17-64
import os # Hold 'cmd' key while clicking on lib, ie 'os', to see more
import time
import sys
def get_username():
    user = input("Please enter your name: ")
    return user

# function for menu passing w/ user as parameter
def menu(user):
    # while loop
    while True:
        # set variable for user name
        message = "Hello " + user + ", lets try some commands."
        # print message and menu
        print(message)
        print("1. whoami")
        print("2. ip a")
        print("3. lshw -short")
        print("4. Exit")
        # get user input and assign to the variable
        answer =  input("Which number option do you choose? ")
        # conditional check of answers
        if answer == '1':
            # run bash command
            os.system("whoami")
            # wait for user to press enter to continue
            input("Please press enter to continue or '4' to exit.")
            # clear the screen
            os.system("clear")
        elif answer == "2":
            os.system("ip a") # or ifconfig if on Mac or ipconfig if on Windows
            input("Please press enter to continue or '4' to exit.")
            os.system("clear")
        elif answer == "3":
            os.system("lshw -short")
            input("Please press enter to continue or '4' to exit.")
            os.system("clear")
        elif answer == "4":
            sys.exit("\nThanks!")
        # catch all if user inputs wrong data
        else:
            print("Please enter a valid option.")
            time.sleep(2)
            os.system("clear")
# main gate function
if __name__ == "__main__":
    user = get_username()
    menu(user)

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

# Collections

# create a list
list_one = ['apple', 'orange', 'banana']
# print entire list
print(list_one)
# print one single item - remember 0 index
print(list[2])
# print last item in list
print(list_one[-1])
# print series inside list '0:2' = 0 is inclusive, 2 isn't inclusive, ':' means stop just before num
print(list_one[0:1])
# print first items
print(list_one[:2])
# reverse list/array
print(list_one[::-1])
# add to end of list/array
list_one.append("grape")
# remove from list
list_one.pop
# sets are unordered and they don't allow duplicate values

# 3 ways to open files (write, read, append)
open("test.txt", "w") # create file with write permissions

# Declaration of functions

# Main
file.write("hello world") # methods on file object
file.close() # have to close file to write to disk
file = open("test.txt", "a") # use append command otherwise write will erase previous data
file.write("\ngoodbye world") # written on new line and not written until close operation, don't forget
file.close()
file = open("test.txt", "r") # get data out of file
file.read()
bar = file.read()
type(bar) # see what the variable assignment creates

# PS Util

# install Python library with 'pip install' - different from import.  Import tells script that you need to bring it into script
# pip install psutil to install library
import psutil 

# Generate CPU times as a tuple
CPUtime = psutil.cpu_times()
print(CPUtime)

# Generate CPU times as a tuple
# CPUtime = psutil.cpu_times()
# print(CPUtime)

# Cleaner version
print(f"CPU TIME: {psutil.cpu_times()}\n")

# Generate CPU consumption percentage
print(f"CPU consumption %: {psutil.cpu_percent()}\n")

# F string example
val = "orange"
print(f"{val} is the first grocery item")

# Assign a requests.get function to a variable
response = requests.get("https://api.github.com")
print(response)

# More specific method - just the code, no 'Respose'
print(response.status_code)

# Get the site's html info/text
response2 = requests.get("http://google.com")
print(response2.text)