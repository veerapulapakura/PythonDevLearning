# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

my_list = [5,6,77,45,22,12,24]
no_evenNumbers= []
for i in my_list:
    if i%2 !=0:
        no_evenNumbers.append(i)
print(no_evenNumbers)


def isEven(n):
    return n%2!=0

li = [5,6,77,45,22,12,24]
lst = list(filter(isEven,li))
print(lst)



li = [5,6,77,45,22,12,24]
lst = list(filter(lambda n:n%2!=0,li))
print(lst)