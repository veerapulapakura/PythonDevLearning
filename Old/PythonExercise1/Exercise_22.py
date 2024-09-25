# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

from pprint import pprint
p=input().split()
pprint({i:p.count(i) for i in p})

