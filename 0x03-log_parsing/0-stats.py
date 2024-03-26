#!/usr/bin/python3
""" Log parsing script that reads from stdin and computes
metrics based on certain conditions"""

import sys


def parse_log_line(line):
    """Parses a log line and returns relevant information"""
    words = line.split()
    if len(words) == 9 and '/projects/260' in words:
        return int(words[-1]), words[-2]
    return None, None


def update_metrics(file_size, codes, file_size_increment, code):
    """Updates the metrics based on the parsed log line information"""
    file_size += file_size_increment
    if code in ref_codes:
        codes[code] = codes.get(code, 0) + 1
    return file_size, codes


def print_out(file_info, codes_info):
    """Prints information of files and status codes"""
    print(f"File size: {file_info:d}")
    for code in sorted(codes_info.keys()):
        print(f"{code}: {codes_info[code]:d}")


ref_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0
file_size = 0
codes = {}

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            file_size_increment, code = parse_log_line(line)
            if file_size_increment is not None:
                file_size, codes = update_metrics(file_size, codes,
                                                  file_size_increment, code)
                count += 1
                if count == 10:
                    print_out(file_size, codes)
                    count = 0
    except KeyboardInterrupt:
        print_out(file_size, codes)
        raise
