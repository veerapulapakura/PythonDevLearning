import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('This is the begenning of each test')

    def test_do_stuff(self):
        num = 10
        result = main.do_stuff(num)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        num = 'dsdsdds'
        result = main.do_stuff(num)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        num = None
        result = main.do_stuff(num)
        self.assertEqual(result, 'Enter the number')

    def test_do_stuff4(self):
        num = ''
        result = main.do_stuff(num)
        self.assertEqual(result, 'Enter the number')

    def tearDown(self) -> None:
        print('End of the trsts')

if __name__ == '__main__':
    unittest.main()

    # run all the tests in this main
    # To run the files from the command line
    # touch filename then python3 -m unittest
    # python3 -m unittest -v   it will give more details about the tests.




