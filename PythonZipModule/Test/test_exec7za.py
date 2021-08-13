"""Test exec7za module"""
import unittest
import os
import shutil


from ..util.exec7za import Exec7za

class TestExec7za(unittest.TestCase):

    def setUp(self):
        self.obj = Exec7za()

    def test_args(self):
        self.obj.add_args('a', 'test.zip')
        self.assertEqual(self.obj.get_args(), ['7za', 'a', 'test.zip'])
        self.obj.add_args('test.txt')
        self.assertEqual(self.obj.get_args(), ['7za', 'a', 'test.zip', 'test.txt'])

    
    def test_empty_run(self):
        zc = self.obj.run()
        self.assertEqual(zc.get_returncode(), 0)
        self.assertRegex(zc.get_stdout(), r'<Switches>')
        self.assertEqual(zc.get_stderr(), '')

class TestExec7zaRun(unittest.TestCase):

    def setUp(self) -> None:
        testdir = os.path.join(os.path.dirname(__file__), 'testdir')
        testfile = os.path.join(testdir, 'testfile.txt')
        testzip = os.path.join(testdir, 'testzip.zip')
        if not os.path.isdir(testdir):
            os.mkdir(testdir)
        with open(testfile, 'w') as tf:
            tf.write('This is a test file\n')

        self.testdir = testdir
        self.obj = Exec7za('a', testzip, testfile)

    def test_run(self) -> None:
        zc = self.obj.run()
        self.assertEqual(zc.get_returncode(), 0)
        self.assertRegex(zc.get_stdout(),r'Everything is Ok')
        self.assertEqual(zc.get_stderr(), "")

    def tearDown(self) -> None:
        shutil.rmtree(self.testdir)

        
        
