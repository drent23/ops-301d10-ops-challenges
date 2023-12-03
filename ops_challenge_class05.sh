!#/bin/bash



# Create a function for script
compressing_log_files() {
# Assign variable to log files
log_files=("/var/log/syslog" "/var/log/wtmp")

# Create a backup directory
backup_directory="/var/log/backups/syslog"
sudo mkdir -p "$backup_directory"

# Create timestamp using YYYYMMDDHHSS
timestamp=$(date "+%Y%m%d%H%M%S")
# Print to screen the size of each file
    for file in "${log_files[@]}"; do
        # Get original size
        og_size=sudo $(du -h "${file}" | awk '{print $1}')
        echo "The original size of $file is $og_size."
        # Compress log files to backup directory and add timestamp
        comp_file="sudo ${backup_directory}/$(basename ${file})-${timestamp}.gzip"
        sudo gzip -c "${file}" > "${comp_file}"
        # Clear contents of the log file
        > "$file"
        # Get compressed size
        comp_size=$(du -h "${comp_file}" | awk '{print $1}')
        echo "The compressed size of $comp_file is $comp_size."
        # Compare sizes
        echo "The difference between the original size $og_size and the compressed size $comp_size is ($og_size - $comp_size)."
    done
# Use 'shred' to clear tracks of who logged into the system to manipulate/compress log files
shred -vfzu auth.log
}
compressing_log_files