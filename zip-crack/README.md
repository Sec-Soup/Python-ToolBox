  
# zip-crack
The purpose of this script is brute force ZIP archives that are password protected. 

The dictionary file passed as an argument can be whatever the user chooses. passwords.txt is included here in this repo.

The passwords.txt file that is a companion to this script is spefically designed for crimeware variants such as BokBot, Valak, Ursnif, and Dridex that are often delivered as ZIP archives.

# Dependency:
The only dependency the user should need is pyzipper. See this documentation to install: https://pypi.org/project/pyzipper/

# Usage: 
zip-crack.py -f EVILZIP.zip -d passwords.txt

# Acknowledgments: 
Special thanks to @AbsoZed, becuase I borrowed some of his code. 
