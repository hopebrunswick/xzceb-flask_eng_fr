'''
Unit tests for the machine translation project.
'''

import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f(self):
        '''
        Tests hello, goodbye, and null input
        '''
        if englishToFrench(not ''):
            self.assertEqual(englishToFrench('Hello'), 'Bonjour')
            self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')
        # test for null input
        self.assertEqual(englishToFrench(''), 'Error')
    
class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e(self):
        '''
        Tests hello, goodbye, and null input
        '''
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')
        # test for null input
        self.assertEqual(frenchToEnglish(''), 'Error')

# Run the tests
if __name__ == '__main__':
    '''
    Run the tests
    '''
    unittest.main()