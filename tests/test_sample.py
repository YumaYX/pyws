import unittest

from src import add_f

class TestSample(unittest.TestCase):
    def setUp(self):
        print("setUp()")

    def tearDown(self):
        print("tearDown()")

    def test_mypackages(self):
        print("test1")
        self.assertEqual(True, True)

    def test_mypackages2(self):
        print("test2")
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEqual(add_f.add(4, 5), 9)
