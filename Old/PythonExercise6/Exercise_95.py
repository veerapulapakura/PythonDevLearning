# If the following string is given as input to the program:
#
# 5
# 2 3 6 6 5
# Then, the output of the program should be:
#
# 5

arr = input().split()
arr = list(set(arr))
arr.sort()
print(arr[-2])

# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4

# You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
#
# If the following string is given as input to the program:
#
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Then, the output of the program should be:
#
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

"""Solution by: mishrasunny-coder
"""
import textwrap
string = input()
width = int(input())
print(textwrap.fill(string,width))

# You are given an integer, N. Your task is to print an alphabet rangoli of size N.
# (Rangoli is a form of Indian folk art based on creation of patterns.)

import string
def print_rangoli(size):
    n = size
    alph = string.ascii_lowercase
    width = 4 * n - 3

    ans = []
    for i in range(n):
        left = '-'.join(alph[n - i - 1:n])
        mid = left[-1:0:-1] + left
        final = mid.center(width, '-')
        ans.append(final)

    if len(ans) > 1:
        for i in ans[n - 2::-1]:
            ans.append(i)
    ans = '\n'.join(ans)
    print(ans)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



















