#!/usr/bin/python3
import sys
import signal

# Initialize total file size and dictionary for status codes
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    """Prints the current stats of the log parsing"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    """Handles keyboard interruption to print stats"""
    print_stats()
    sys.exit(0)

# Set up signal handling for CTRL+C (SIGINT)
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            # Parse line using expected format
            parts = line.split()
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update status code count if it is a known code
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats()

        except (IndexError, ValueError):
            # Skip line if it is incorrectly formatted
            continue

    # Print final stats after all lines are read
    print_stats()

except KeyboardInterrupt:
    # Print stats if CTRL+C is pressed
    print_stats()
    sys.exit(0)

