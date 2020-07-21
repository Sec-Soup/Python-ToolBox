# Valak password cracker

# The purpose of this script is to extract the contents of password protected ZIP archives containing docs for Valak malware.
# This script is based on current naming conventions at the time of writing..
# The regex utilized here will likely need to be updated to account for tactical changes.
# Author: Ryan Campbell
# See Disclaimer at end


import argparse
import pyzipper
import exrex

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', help='specify zip FILE')
args = parser.parse_args()		
zip_file = args.file
password = list(exrex.generate('[0-9]{3}[A-Z]{2}'))
for i in range(len(password)):
	with pyzipper.AESZipFile(zip_file) as zf:
		try:
			zf.extractall(pwd=password[i].encode()) 
			print("[+] extraction succeeded")
		except Exception:
			pass
		else: 
			break


# ********************************************************************
# Disclaimer
# ********************************************************************
# This script is unsupported and is provided as-is.
