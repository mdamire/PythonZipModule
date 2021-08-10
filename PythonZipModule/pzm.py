
if __name__ == "__main__":
    print('name: {}; package: {}; file: {}'.format(__name__, __package__, __file__))
    from .Test import test_exec7za
    import unittest

    suite = unittest.TestLoader().loadTestsFromModule(test_exec7za)
    unittest.TextTestRunner(verbosity=2).run(suite)
