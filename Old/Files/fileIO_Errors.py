# File IO Errors

try:
    with open('text.text', mode = 'x') as myfile:
        print(myfile.read())
except FileExistsError as err:
    print('File not founf error')
    raise err
except IOError as err:
    print('IO Error')
    raise err



