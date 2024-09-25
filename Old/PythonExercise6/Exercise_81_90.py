# By using list comprehension, please write a program to print the list after removing
# numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
li = [x for x in li if x % 35!=0]
print(li)

#By using list comprehension, please write a program to print the list after removing the
# 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2 != 0 and i <= 6]
print(li)

# By using list comprehension, please write a program to
# print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i < 3 or i > 4]
print(li)

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i<3 or 4<i]
print(li)

# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)

# By using list comprehension, please write a program to print the list after
# removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].


li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i not in (0,4,5)]
print(li)

# By using list comprehension, please write a program to print the list after removing
# the value 24 in [12,24,35,24,88,120,155].

li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if li[i]!=24]
print(li)

li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)

li = [12,24,35,24,88,120,155]
li.remove(24)  # this will remove only the first occurrence of 24
print(li)

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.

list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
combined_list = []

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.

list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
set1= set(list1)
set2= set(list2)
intersection = set1 & set2
print(intersection)

# With a given list [12,24,35,24,88,120,155,88,120,155],
# write a program to print this list after removing all duplicate values with original order reserved.

li = [12,24,35,24,88,120,155,88,120,155]
for i in li:
    if li.count(i) > 1:
        li.remove(i)
print(li)

# Define a class Person and its two child classes: Male and Female. All classes have a method
# "getGender" which can print "Male" for Male class and "Female" for Female class.

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
Uanknown = Person()

print(Uanknown.getGender())
print(aMale.getGender())
print(aFemale.getGender())

# Please write a program which count and print the numbers of each character in a string input by console.
#
# Example: If the following string is given as input to the program:
#
# abcdefgabc

import string

s = input()
for letter in string.ascii_lowercase:
    cnt = s.count(letter)
    if cnt > 0:
        print("{},{}".format(letter,cnt))



