# Given 2 sets of integers, M and N, print their symmetric difference in ascending order.
# The term symmetric difference
# indicates those values that exist in either M or N but do not exist in both.

# The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.
#
# 4
# 2 4 5 9
# 4
# 2 4 11 12

if __name__ == '__main__':
    n = int(input())
    set1 = set(map(int,input().split()))

    m = int(input())
    set2 = set(map(int, input().split()))

    ans = list(set1 ^ set2)
    ans.sort()
    for i in ans:
        print(i)