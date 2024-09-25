import unittest

class suiteTest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20

    def testadd(self):
        """Add"""
        result = self.a + self.b
        self.assertTrue(result == 30)

    def testsub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


def suite():
    suite = unittest.TestSuite()
    ##   suite.addTest (simpleTest3("testadd"))
    ##   suite.addTest (simpleTest3("testsub"))
    suite.addTest(unittest.makeSuite(suiteTest))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    result = runner.run(test_suite)

    print("---- START OF TEST RESULTS")
    print(result)

    print("result::errors")
    print(result.errors)

    print("result::failures")
    print(result.failures)

    print("result::skipped")
    print(result.skipped)

    print("result::successful")
    print(result.wasSuccessful())

    print("result::test-run")
    print(result.testsRun)
    print("---- END OF TEST RESULTS")