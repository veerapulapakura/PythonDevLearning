# Files

with open('/Users/veerapulapakura/desktop/text.txt', mode ='r+') as myfiles:
    print(myfiles.read())

    # r+ means it is overriting the content of the file
    # a - we need to open the file with append mode so that it will add the content at the end.
    myfiles.close()

with open('/Users/veerapulapakura/desktop/text.txt','a') as myfiles:
    myfiles.write('Additional data we are appending?\n')

    # /Users/veerapulapakura/desktop/text.txt   - This is absolute path
    # ./text.txt  -  this means current directory
    # ../ means going back 1 folder



