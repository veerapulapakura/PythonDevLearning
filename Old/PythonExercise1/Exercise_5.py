# Class with 2 methods

class IOstring():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

    def print_stringLower(self):
        print(self.s.lower())

xx = IOstring()
xx.get_string()
xx.print_string()
xx.print_stringLower()