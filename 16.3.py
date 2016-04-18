import unittest

# A simple function to illustrate
def parse_int(s):
    return　int(s)
    
calss TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')
        
import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
            
        else:
            self.fail('IOError not raised')





