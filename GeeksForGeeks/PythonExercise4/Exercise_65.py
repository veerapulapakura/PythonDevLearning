# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

data = [2,4,6,9]
for i in data:
    assert i%2 == 0, "{} is not an even number".format(i)