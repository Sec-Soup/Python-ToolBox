  
# zip-crack
The purpose of this script is brute force ZIP archives that are password protected. 

The dictionary file passed as an argument can be whatever the user chooses. passwords.txt is included here in this repo.

The passwords.txt file that is a companion to this script is spefically designed for crimeware variants such as BokBot, Valak, Ursnif, and Dridex that are often delivered as ZIP archives.

# Dependency:
Python3

pyzipper - See this documentation to install: https://pypi.org/project/pyzipper/

# Usage: 

```sh
for v1
python3 zip-crack.py -f EVILZIP.zip -d passwords.txt

for v2
dictionary METHOD: "python3 zip-crack.py -f '<FILENAME>.zip' -d -p passwords.txt"
regex METHOD: "python3 zip-crack.py -f '<FILENAME>.zip' -r"
```

# Acknowledgments: 
Special thanks to @AbsoZed, becuase I borrowed some of his code. 
