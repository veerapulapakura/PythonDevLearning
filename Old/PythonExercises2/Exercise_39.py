#Write a program to generate and print another tuple whose values are even numbers in the given
# tuple (1,2,3,4,5,6,7,8,9,10).

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)

