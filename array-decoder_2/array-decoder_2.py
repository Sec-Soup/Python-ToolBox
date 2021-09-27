#Deobfusce DopplelDridex
# Simply Python script to decode an array of integers that require a subtraction operation. Helpful to de-obfuscate strings in macros in DoppelDridex campaigns from September 2021.

#Set the integers as an array
numbers = [<INSERT ARRAY HERE]

#loop through the integers. Subtract the required amount, then convert from decimal to ascii
for i in range (len(numbers)): 
	numbers[i]=chr(numbers[i] - <INSERT SUB OPERATOR HERE)
print ("".join(numbers)) 
