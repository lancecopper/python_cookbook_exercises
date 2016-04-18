import unittest
import sys

class MyTest(unittest.TestCase):
    pass

def main(out=sys.stderr, verbosity=2)
    loader = unittest.TestLoader()
    suite = loader.loadTestFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)
    


if __name__ == '__main__':
    unittest.main()
    








