#!/usr/bin/python3
""" Log parsing script that reads from stdin and computes
metrics based on certain conditions"""

import sys


def parse_log_line(line):
    """Parses a log line in the specified format"""
    words = line.split()
    if len(words) == 8 and words[2] == "GET" and \
        words[3] == "/projects/260" and words[5].isdigit() and \
            words[6].isdigit():
        return int(words[6]), words[7]
    return None, None


def update_metrics(file_size, codes, file_size_increment, code):
    """Updates the metrics based on the parsed log line information"""
    file_size += file_size_increment
    if code in ref_codes:
        codes[code] = codes.get(code, 0) + 1
    return file_size, codes


def print_stats(file_size, codes):
    """Prints the total file size and number of lines by status code"""
    print(f"Total file size: {file_size}")
    for code in sorted(codes.keys()):
        print(f"{code}: {codes[code]}")


ref_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0
file_size = 0
codes = {}

try:
    for line in sys.stdin:
        file_size_increment, code = parse_log_line(line)
        if file_size_increment is not None:
            file_size, codes = update_metrics(file_size, codes,
                                              file_size_increment, code)
            count += 1
            if count == 10:
                print_stats(file_size, codes)
                count = 0
except KeyboardInterrupt:
    print_stats(file_size, codes)
    raise
