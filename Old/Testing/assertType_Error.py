import unittest
import re


class raiseTest(unittest.TestCase):
    def testraiseRegex(self):
        self.assertRaisesRegexp(TypeError,"Point", "TutorialsPoint")

if __name__ == '__main__':
    unittest.main()