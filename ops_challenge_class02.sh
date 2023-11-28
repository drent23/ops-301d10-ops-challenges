#!/bin/bash

# Get current DTG
dtg=`date`
# Target file path
syslog_file="/var/log/syslog"
# Destination file path
current_working_directory="syslog_${dtg}.log"
# Timestamped echo statement pre copy
echo "$(date) Preparing to copy syslog to $current_working_directory."
# Copy '/var/log/syslog' to current working directory
cp "$syslog_file" "$current_working_directory"
# Timestamped echo statement post copy
echo "$(date) Successful copy."
echo "$(date) Script finished."