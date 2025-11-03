#!/usr/bin/env python3
import sys

LOG_FILE = '/var/log/sssd/sssd.log'
SEARCH_PATTERN = 'too many open files'
LINES_TO_CHECK = 100

def check_sssd_log():
    try:
        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()[-LINES_TO_CHECK:]
    except Exception as e:
        print(f"0 sssd_open_files_error - Could not read log file: {e}")
        sys.exit(3)

    # Check for error pattern in the log lines
    errors = [line for line in lines if SEARCH_PATTERN.lower() in line.lower()]

    if errors:
        print(f"2 sssd_open_files_error - Found '{SEARCH_PATTERN}' errors in SSSD logs")
        sys.exit(2)
    else:
        print("0 sssd_open_files_error - No 'too many open files' errors found in recent logs")
        sys.exit(0)


if __name__ == '__main__':
    check_sssd_log()
