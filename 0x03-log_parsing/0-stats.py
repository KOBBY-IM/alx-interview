#!/usr/bin/python3
""" Log parsing script that reads from stdin and computes metrics based on
certain conditions"""


file_size = 0
codes = {}
ref_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0
if __name__ == "__main__":
    import sys

    def print_out(file_info, codes_info):
        """Prints information of files and status codes"""
        print(f"File size: {file_info:d}")
        for code in sorted(codes_info.keys()):
            print(f"{code}: {codes_info[code]:d}")

    try:
        for line in sys.stdin:
            words = line.split()
            if len(words) == 9 and '/projects/260' in words:
                file_size += int(words[-1])
                if words[-2] in ref_codes:
                    codes[words[-2]] = codes.get(words[-2], 0) + 1
                count += 1
            if count == 10:
                print_out(file_size, codes)
                count = 0
        print_out(file_size, codes)
    except KeyboardInterrupt:
        print_out(file_size, codes)
        raise
