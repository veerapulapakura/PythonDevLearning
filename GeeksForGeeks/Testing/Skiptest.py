import unittest

def add(x,y):
      return x+y

class SimpleTest(unittest.TestCase):
   @unittest.skip("demonstrating skipping")
   def testadd1(self):
      self.assertEquals(add(4,5),19)

   def testadd2(self):
       self.skipTest("another method for skipping")
       self.assertTrue(add(4 + 5) == 10)

if __name__ == '__main__':
   unittest.main()