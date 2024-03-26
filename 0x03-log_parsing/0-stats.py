#!/usr/bin/env python3
import sys
import signal


status_codes_count = {}
total_file_size = 0


def signal_handler(sig, frame):
    """Signal handler for SIGINT."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

def print_stats():
    """Function to print the statistics."""
    print(f"File size: {total_file_size}")
    for status_code in sorted(status_codes_count.keys()):
        print(f"{status_code}: {status_codes_count[status_code]}")

def process_line(line):
    """Process each line from stdin."""
    global total_file_size
    try:
        parts = line.split()
        status_code = parts[-2]
        file_size = int(parts[-1])


        total_file_size += file_size


        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        else:
            status_codes_count[status_code] = 1
    except (IndexError, ValueError):
        pass

def main():
    """Main function to read from stdin."""
    line_count = 0
    try:
        for line in sys.stdin:
            process_line(line.strip())
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)

    print_stats()

if __name__ == "__main__":
    main()
