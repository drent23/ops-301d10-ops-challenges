# Imports os lib
import os
import subprocess

# Define a function
def linux_function():
    print("I'm going to use Python's os module to execute a Bash command to capture the user name in a Linux machine: \n")
    # Assign os variables and print to screen
    get_username = os.system('whoami')
    print(get_username)
    print("\nNow I'll do the same to capture the Linux machine's ip: \n")
    get_ip = os.system('ip a')
    print(get_ip)
    print("\nFinally, I'll show you a short list of the Linux machine's hardware: \n")
    hardware_list = os.system('lshw -short')
    print(hardware_list)
    print("\n\n")
    print("\nNow I'll do the same commands using the subprocess module: \n")
    # Assign subprocess variables and print to screen
    username_subprocess = subprocess.run(['whoami'], capture_output=True, text=True)
    print("\nSubprocess output of 'whoami': \n", username_subprocess.stdout.strip())
    ipaddr_subprocess = subprocess.run(['ip', 'a'], capture_output=True, text=True)
    print("\nSubprocess output of 'whoami': \n", ipaddr_subprocess.stdout.strip())
    hwlist_subprocess = subprocess.run(['lshw', '-short'], capture_output=True, text=True)
    print("\nSubprocess output of 'whoami': \n", hwlist_subprocess.stdout.strip())
# Call/invoke functiion
linux_function()