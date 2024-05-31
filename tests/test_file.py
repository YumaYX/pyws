import unittest
import re

from src import file

class TestFile(unittest.TestCase):
    def test_file_read(self):
        content = file.file_read("testdata/a.txt")
        self.assertEqual("hello\n", content)

    def test_file_read_include(self):
        content = file.file_read("testdata/a.txt")
        assert(re.search("llo", content))
