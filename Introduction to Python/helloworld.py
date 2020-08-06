print ('techcamp')
x = 1+2
print (x)
#######Vari_ablesThereal_thing###

# 1st Rule : nospaceinnamingvariables.
#Camel Case =techCampPortal (All frist letters of every word apart from the first letter, is capital)
# Snake Typing = use a hyphen instead of space (Tech _Camp)
#  ; stay consistent.

#2nd Rule : Never begin with a number but can contain numbers
#3rd Rule : should never contain special characters
#4th Rule : Should never contain key words (If, else, etc)


########DATA TYPES##########
#String =  ('Anything written inside quotation marks')
#Integers = Numbers (whole numbers)
#Booleans = True or false statements.
# For instance 

b = 5.0
print (type (b))
print(b, "is of type", type(b))
# Definition of Booleans
Male = True 
print (type(Male))
# Definition of a single line string 
string = ('techChamp is practical')
print (string)
print (type(string))

#Multi-line string#
description ="""
Hello, Welcome to techcamp
we are pleased to learn from this """

print (type(description))

#String Indexing.
# Indexing begins at zero
# ...The first character is always at index zero.


Bootcamp = "Python programming"
print (Bootcamp)
print (Bootcamp[0])

# Positive Indexing begins from left to right he first element is indexed at 0 (onwards)
# Negatve Indexing begins from left to right he first element is indexed at 0 (backwards)
print (Bootcamp[-7])

#String Slicing ; picking a section of sth [start:stop(rest value +1)]

print (Bootcamp[0:6])

print (Bootcamp[11:14])
print (Bootcamp [-5:-8])

#Concantenation
f_name = "Brian"
l_name = "Ngulolu"

print ('my name is',f_name , l_name)

g = 'I love coding'
print (g.lower())
print (g.upper())
print (g.capitalize())
print (g.find())