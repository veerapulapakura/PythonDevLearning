import unittest
import math
import re

class SimpleTest(unittest.TestCase):
   def test1(self):
      self.assertAlmostEqual(21.0/7,3.0)
   def test2(self):
      self.assertNotAlmostEqual(10.0/3,3)
   def test3(self):
      self.assertGreater(math.pi,3)
   # def test4(self):
   #    self.assertNotRegexpMatches("Tutorials Point (I) Private Limited","Point")

   def test5(self):
      self.assertRegexpMatches("Tutorials Point (I) Private Limited", "Point")


if __name__ == '__main__':
   unittest.main()