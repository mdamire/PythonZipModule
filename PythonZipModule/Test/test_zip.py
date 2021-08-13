import unittest
import os
import shutil

from ..util.zip import Zipper
from ..util.zipcomplete import ZipComplete

class TestZipper(unittest.TestCase):
    
    def setUp(self) -> None:
        testdir = os.path.join(os.path.dirname(__file__), 'testdir')
        testfile = os.path.join(testdir, 'testfile.txt')
        testzip = os.path.join(testdir, 'testzip.zip')
        if not os.path.isdir(testdir):
            os.mkdir(testdir)
        with open(testfile, 'w') as tf:
            tf.write('This is a test file\n')

        self.testdir = testdir
        self.testzip = testzip
        self.testfile = testfile

    def test_add(self):
        zipper = Zipper(self.testzip)
        zc = zipper.add(self.testfile, '/abcd/abcd.txt')
        self.assertEqual(isinstance(zc, ZipComplete), True)
        self.assertEqual(zc.get_returncode(), 0)
        self.assertEqual(os.path.isfile(self.testzip), True)

    def tearDown(self) -> None:
        shutil.rmtree(self.testdir)