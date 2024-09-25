# Files

myfile = open('/Users/veerapulapakura/desktop/text.txt')
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.read())

#Seek is used to move the curser to the beginning of the file.
myfile.seek(0)

print('Before readline Print ')
print(myfile.readline())
print(myfile.readline())

# readline is used to read only 1 line

# readlines is used to read only all the lines.

print('Before readlines')
print(myfile.readlines())

# To close the file after using.
myfile.close()

print('Opening Again')
with open('/Users/veerapulapakura/desktop/text.txt') as myfiles:
    print(myfiles.read())