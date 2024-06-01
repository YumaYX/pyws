import glob
import os
import re
import subprocess
import unittest

from src import file


class TestFile(unittest.TestCase):

    def tearDown(self):
        current_directory = os.getcwd()
        txt_files = glob.glob(os.path.join(current_directory, '*.txt'))
        for txt_file in txt_files:
            try:
                os.remove(txt_file)
                print(f"Deleted: {txt_file}")
            except OSError as e:
                print(f"Error: {txt_file} : {e.strerror}")

    def test_file_read(self):
        content = file.file_read("testdata/a.txt")
        self.assertEqual("hello\n", content)

    def test_file_read_include(self):
        content = file.file_read("testdata/a.txt")
        assert(re.search("llo", content))
        
    def test_exec_command(self):
        result = subprocess.run(['echo', 'goodbye'], capture_output=True, text=True)
        assert(re.search("goodbye", result.stdout))

    def test_exec_command_w_r(self):
        result = subprocess.run('echo "Hello" > temp.txt', shell=True)
        content = file.file_read("temp.txt")
        assert(re.search("Hello", content))
