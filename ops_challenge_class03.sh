#!/bin/bash

# Prompt user for input directory path
read -p "Please enter your desired directory path: " directory_path

# Prompt user for input persmissions number
read -p "Please enter the persmission numbers would you liek to use: " perm_num

# Go to users input directory
cd "$directory_path"

# Create log file
log_file="changed_log.txt" > "$log_file"

# Change files to input setting
for file in *; do 
    if [[ -f "$file" ]]; then
        chmod "$perm_num" "$file"
        echo "Changing permissions of $file to $perm_num" | tee -a "$log_file"
        ls -l "$file" | tee -a "$log_file"
    fi
done

# Print to screen contents and new permissions
echo "Below are the files with new permissions you requested in your input directory - "
ls -l | tee -a "$log_file"
sleep 2

# Print to screen log file
cat "$log_file"