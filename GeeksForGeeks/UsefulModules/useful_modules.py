from collections import Counter, defaultdict, OrderedDict
listt = [1,2,3,4,5,6,7,7,8,9]
my_str = 'veera venkata ratna kumar pulapakura'
print(Counter(listt))
print(Counter(my_str))

dicto = {'a':1, 'b':2}
print(dicto['a'])

# To access the values which  are not avialable in the dictionary. Using lamba funtions
dicto = defaultdict(lambda :5,{'a':1, 'b':2, 'c':3})
print(dicto['d'])

#Orderd dict, it will return true if the order is same as earlier

d1 = OrderedDict()
d1['a'] = 1
d1['2'] = 2

d2 = OrderedDict()
d2['2'] = 2
d2['a'] = 1


print(d1==d2)



