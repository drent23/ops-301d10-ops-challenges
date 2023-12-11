#!/usr/bin/env python3

# Script Name:                  Psutil
# Author:                       David Renteria
# Date of latest revision:      12/08/2023
# Purpose:                      Fetch system information

# Import psutil library
import psutil

# Declare a function 
def fetch_times():
    cpu_times = psutil.cpu_times()
    print(f"Time spent by normal processes executing in user mode: {cpu_times.user}\n")
    print(f"Time spent by processes executing in kernel mode: {cpu_times.system}\n")
    print(f"Time when system was idle: {cpu_times.idle}\n")
    print(f"Time spent by priority processes executing in user mode: {cpu_times.nice}\n")
    print(f"Time spent waiting for I/O to complete: {cpu_times.iowait}\n")
    print(f"Time spent for servicing hardware interrupts: {cpu_times.irq}\n")
    print(f"Time spent for servicing software interrupts: {cpu_times.softirq}\n")
    print(f"Time spent by other operating systems running in a virtualized environment: {cpu_times.steal}\n")
    print(f"Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel: {cpu_times.guest}\n")

# Call function
fetch_times()