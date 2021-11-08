'''
Unit tests for the machine translation project.
'''

import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f(self):
        '''
        Tests hello, goodbye, and null input
        '''
        if english_to_french(not ''):
            self.assertEqual(english_to_french('Hello'), 'Bonjour')
            self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        # test for null input
        self.assertEqual(english_to_french(''), 'Error')
    
class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e(self):
        '''
        Tests hello, goodbye, and null input
        '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        # test for null input
        self.assertEqual(french_to_english(''), 'Error')

# Run the tests
if __name__ == '__main__':
    '''
    Run the tests
    '''
    unittest.main()