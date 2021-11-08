'''
Unit tests for the machine translation project.
'''

import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f(self):
        '''
        Tests hello, goodbye
        '''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')
        self.assertNotEqual(english_to_french('Goodbye'), 'Bonjour')
    
class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e(self):
        '''
        Tests hello, goodbye
        '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodbye')
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello')

# Run the tests
if __name__ == '__main__':
    '''
    Run the tests
    '''
    unittest.main()