#!/bin/bash

# Assign log files to an array/list
log_files=("/var/log/syslog" "/var/log/wtmp")

# Declare backup directory
backup_directory="/var/log/backups"

# Create a backup directory
mkdir -p "$backup_directory"

# Create timestamp
timestamp=$(date "+%Y%m%d-%H:%M:%S")

# Declare a function to compress files
compress_files() {
    file="$1"
    # Create compressed file
    comp_file="$backup_directory/$(basename $file)-$timestamp.gzip"
    # Get original size
    og_size=$(stat -c %s "$file")
    echo "The original size of $file is $og_size."
    # Compress log files to backup directory and add timestamp
    gzip -c "$file" > "$comp_file"
    # Get compressed size
    comp_size=$(stat -c %s "$comp_file")
    echo "The compressed size of $comp_file is $comp_size."
    # Compare sizes
    echo "Original size: $og_size vs Compressed size: $comp_size."
    # Clear contents of the log file
    > "$file"

# Use 'shred' to clear tracks of who logged into the system to manipulate/compress log files
    shred -vfzu auth.log
}
# Go through log files and backup/compress
for file in "${log_files[@]}"; do
    if [ -e "$file" ]; then
        compress_files "$file"
        echo "$file backedup and compressed."
    else
        echo "That file doesn't exist."
    fi 
done
compress_files()