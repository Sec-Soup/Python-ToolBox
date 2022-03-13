#This script decodes an obfuscated string commonly found in Danabot downloaders
#Author: Ryan Campbell @sec_soup
#Usage: Copy and paste the obfuscated string into the 'string' variable in line 7
#Future planned updates: Add support for passing VBS and Parent ZIP files as arguments for use in a terminal

####OPERATION One - set some stuff up 
#take string as input 
string='<INSERT STRING HERE>'
#set a variable to take 2 characters
n = 2
#take slices of string 
#take first slice for the Dictionary of keys/values
slice1 = string[:512]

#take second slice for conversion to ascii characters
slice2 = string[514:]

####OPERATION Two - Make the Dictionary decoder ring
#loop through string and take slices of two items while incrementing forward. 
my_dict1 = [slice1[index : index + n] for index in range(0, len(slice1), n)]

# convert to dictionary
dic1 = dict([(idx, item) for idx,item in enumerate(my_dict1)])

#make a list of the slices from earlier to use for looking up 
my_dict3 = [slice2[index : index + n] for index in range(0, len(slice2), n)]

#for each key in my_dict3, get the index from dic1
dict_items = dic1.items()

####OPERATION Three
#Loop throught the list of 2 character values and look them up in Dictionary, grab their associated key and convert to their ascii value. Join the strings and print. 
for i in my_dict3:
    #print (i)
    for key,value in dict_items:
        if value == i:       
            print(chr(key), end="")
