# The purpose of this script is brute force ZIP archives that are password protected. 
# The dictionary file passed can be whatever the user chooses.
# The passwords.txt file that is a companion to this script is spefically designed for crimeware variants such as Emotet, Qakbot, Bokbot, Ursnif, and Dridex that are often delivered as ZIP archives.
# The only dependency the user should need is pyzipper. See this documentation to install: https://pypi.org/project/pyzipper/
# Author: Ryan Campbell @sec_soup
# Acknowledgments: Special thanks to @HBRH_314, becuase I borrowed some of his code. 
# See Disclaimer at end

import argparse
import pyzipper
import os
import sys
import time
from datetime import datetime, timedelta

start_time = time.time()

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='specify zip FILE', type=str)
    parser.add_argument('-d', '--dictionary', help='specify dictionary METHOD', type=str)
    args = parser.parse_args()		
    zip_file = args.file
    dictionary = args.dictionary

    if zip_file is not None:
        if os.path.isfile(zip_file):
            if dictionary is not None:
                if os.path.isfile(dictionary):
                    crack(zip_file, dictionary)
                else:
                    print('[-] Dictionary file does not exist. Check file path. Exiting.')
                    sys.exit(2)
            else:
                print('[-] You must specify a dictionary file with the dictionary option. Exiting.')
                sys.exit(2)
        else:
            print('[-] File does not exist. Check path. Exiting')
            sys.exit(2)
    else:
        print('[-] You must specify a file. Exiting.')
        sys.exit(2)

def crack(zip_file, dictionary):
    password = None 
    with pyzipper.AESZipFile(zip_file) as zf:
        with open(dictionary, 'r') as f:
            for line in f.readlines():
                password = line.rstrip()
                try: 
                    zf.extractall(pwd=password.encode()) 
                    print(f'[+] Extraction succeeded: password = {password}') 
                except Exception:
                    pass 
                else:
                    break
    

if __name__ == '__main__':
    main()

elapsed_time = time.time() - start_time
print("[+] Extraction took: %s " % timedelta(seconds=round(elapsed_time)))


# ********************************************************************
# Disclaimer
# ********************************************************************
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.


