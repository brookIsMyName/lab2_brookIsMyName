#!/bin/bash

set -euo pipefail

if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv was not found."
    exit 1
fi

# then i Create the archive directory
mkdir -p archive

# Generate a timestamp so we can later on name our log files with them.
timestamp=$(date +"%Y%m%d-%H%M%S")

# Generate archived filename with our new timestamp
archived_filename="grades_${timestamp}.csv"

# Prevent overwriting an existing archive
if [ -e "archive/${archived_filename}" ]; then
    echo "Error: An archive with this timestamp already exists."
    exit 1
fi

# then i can just move the file into the archive folder.
mv grades.csv "archive/${archived_filename}"

# Now I can create a new grades.csv.
touch grades.csv

# final move is to append everthing we did into a log file.

echo "Archived grades.csv to archive/${archived_filename} and created a new grades.csv at ${timestamp}" >> organizer.log

echo "Archiving completed successfully!!!"