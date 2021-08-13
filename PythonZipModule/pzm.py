
if __name__ == "__main__":
    # print('name: {}; package: {}; file: {}'.format(__name__, __package__, __file__))
    from .Test import test_exec7za, test_zip
    import unittest

    suite = unittest.TestLoader().loadTestsFromModule(test_exec7za)
    suite.addTests(unittest.TestLoader().loadTestsFromModule(test_zip))
    unittest.TextTestRunner(verbosity=2).run(suite)
