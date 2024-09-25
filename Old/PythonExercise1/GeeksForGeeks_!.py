
#Finding common elements between 2 set


friends_A = {"Alice", "Bob", "Charlie"}
friends_B = {"Bob", "David", "Eve"}
common_friends = friends_A.intersection(friends_B)
print(common_friends)  # Output: {'Bob'}


#Finding the unique elements between 2 set
friends_A = {"Alice", "Bob", "Charlie"}
friends_B = {"Bob", "David", "Eve"}
common_friends = friends_A.union(friends_B)
print(common_friends)  # Output: {'Bob'}


#Appending and removing
data = [23, 45, 12, 67, 34]
data.append(89)  # Add an item
data.remove(45)  # Remove an item
print(data)
print(sorted(data))

#Implementing Stacks and Queues
stack = []
stack.append('a')  # Push onto stack
stack.append('b')
print(stack.pop())  # Pop from stack -> 'b'
print(stack)


# def sortSecond(val):   Python sort List by Key
#     return val[1]
# my_list1 = [(1, 2), (3, 3), (1, 1)]
# my_list1.sort(key=sortSecond)
# print(my_list1)
# my_list1.sort(key=sortSecond, reverse=True)
# print(my_list1)
#
# [(1, 1), (1, 2), (3, 3)]
# [(3, 3), (1, 2), (1, 1)]

#Sorting numbers
print('Sorting numebrs ')
data = [23, 45, 12, 67, 34]
print(data)
print(sorted(data))
print(data)
print(data.sort())
print(data)
print(data)


