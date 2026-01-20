'''This program will analyse any logs/text file within a designated folder and output a summary into a folder for log summaries'''
# Goals of the log analysis:
# Count number of logs (number of lines)
# Split and count different logs (notices, error)


import os

log_folder = "logs"

for file_name in os.listdir(log_folder):
    entries = []  # List to store log entries and their components [timestamp, level, message]

    # Setting the file path to the log folder
    file_path = os.path.join(log_folder, file_name)
    # Opening the log file and reading it
    # default encoding for Windows is utf-8 or ASCII, but in case it's not, set to ignore errors
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            # Parsing the log data

            # Splitting the time stamp section
            # partition splits into 3 tuples, following the 1st instance of the indicated separator
            log_left, _, log_remainder = line.partition("]")
            # _ indicates that that particular iterable is not needed to be assigned a variable

            # Splitting the log type from the details
            log_remainder_left, _, log_remainder_right = log_remainder.partition(
                "]")

            time_stamp = log_left.lstrip("[")  # remove the left bracket
            log_type = log_remainder_left.lstrip(
                "[")  # remove the left bracket
            log_details = log_remainder_right.strip()  # remove trailing spaces

            # Add to list
            entries.append((time_stamp, log_type, log_details))

        # Log Summary

        # Track number of each log_type
        # Consider tracking/summarising log_types based on occurrence during a certain time window.

            # Output log summary as csv/text file to a summary folder
