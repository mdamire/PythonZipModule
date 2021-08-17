import unittest
import os
import shutil

from ..util.zip import Zipper
from ..util.zipcomplete import ZipComplete

class TestZipper(unittest.TestCase):
    
    def setUp(self) -> None:
        testdir = os.path.join(os.path.dirname(__file__), 'testdir')
        testfile = os.path.join(testdir, 'testfile.txt')
        testfile2 = os.path.join(testdir, 'testfile2.txt')
        if not os.path.isdir(testdir):
            os.mkdir(testdir)
        with open(testfile, 'w') as tf:
            tf.write('This is a test file\n')
        with open(testfile2, 'w') as tf:
            tf.write('This is 2nd test file\n')

        self.testdir = testdir
        self.testfile = testfile
        self.testfile2 = testfile2

    def test_add(self):
        #test zip 1
        testzip = os.path.join(self.testdir, 'testzip.zip')

        zipper = Zipper(os.path.join(self.testdir, 'testzip'))
        self.assertEqual(zipper.zipfile, testzip)


        zc = zipper.add(self.testfile, '/abcd/abcd.txt')
        self.assertEqual(isinstance(zc, ZipComplete), True)
        self.assertEqual(zc.get_returncode(), 0)
        self.assertEqual(os.path.isfile(testzip), True)

        #Test zip 2
        testzip2 = os.path.join(self.testdir, "subdir", 'testzip.zip')
        zipper = Zipper(testzip2)
        with self.assertRaises(OSError):
            zipper.add(self.testfile)

        zipper.add(self.testfile, createDir=True)
        self.assertEqual(zipper.zipfile, testzip2)
        self.assertEqual(os.path.isfile(testzip2), True)

        #test update
        zc = zipper.update(self.testfile2)
        self.assertEqual(zc.get_returncode(), 0)

        #test remove
        self.assertEqual(zipper.remove('testfile2.txt').get_returncode(), 0)

        #test extract
        extractdir = os.path.join(self.testdir, 'outdir')
        with self.assertRaises(OSError):
            zipper.extract(extractdir)

        zipper.extract(extractdir, createDir=True)
        self.assertTrue(os.path.isfile(os.path.join(extractdir, 'testfile.txt')))

        extractdir2 = os.path.join(self.testdir, 'outdir2')
        with self.assertRaises(OSError):
            zipper.extractWithPath(extractdir2)

        zipper.extractWithPath(extractdir2, createDir=True)
        self.assertTrue(os.path.isfile(os.path.join(extractdir2, 'testfile.txt')))


    def tearDown(self) -> None:
        shutil.rmtree(self.testdir)

