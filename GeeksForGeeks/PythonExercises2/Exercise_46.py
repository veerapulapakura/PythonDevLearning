# Define a class named American and its subclass NewYorker.

class American(object):
    def method1(self):
        print('Veera Pulapakura from American')

class NewYorker(American):

    def method2(self):
        print('Veera Pulapakura from Newyorker')

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican.method1())
print(aNewYorker.method2())
print(aNewYorker.method1())