# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

import random
resp = random.sample(range(100,201,2),5)
print(resp)

rands = random.sample([i for i in range(100,201) if i%2==0], 5)
print(rands)

print(random.sample([i for i in range(100,201) if i%2==0], 5))

