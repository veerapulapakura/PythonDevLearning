def demo_gen():
    num = 10
    print('Statement number 1')
    yield num
    num += 1
    print('Statement number 2')
    yield num
    num += 1
    print('Statement number 3')
    yield num
for item in demo_gen():
    print(item)
    #pytest -k divisible -v  is to run all the test names includes divisible and - v for vebrose, detailed output.