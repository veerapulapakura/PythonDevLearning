# Regular Expressions
import re

str = 'my name  is veera venkata ratna veera kumar this, this eeee'
print('veera' in str)  # Will return true as Veera os there
print('is' in str)  # Will return true as Veera os there
print('veerwa' in str) # Will return False as Veera os there

a = re.search('veera', str)  # This will search for the value
print(a.span())   # This will print the start and end
print(a.start())  # This will print the starting of the string.
print(a.end())  # This will print the ending of the string.

print(a.group())  # This will print the ending of the string.

patttern = re.compile('my name  is veera venkata ratna veera kumar this, this')
a = patttern.search(str)
b = patttern.findall(str)
print(a)   # this will return None as there is no this.
print(b)   # this will return all the this in the String.

c = patttern.fullmatch(str)
print(c)   # Not found the full match

d = patttern.match(str)
print(d)   # Finding full match







