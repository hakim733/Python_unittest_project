'''
    Student shall write their names here
        1. Abdelhakim Mraihi
        2. Student 2
'''


import unittest
from Task1_Rover import rovar

class test_string(unittest.TestCase):
    '''
        _LOWER_CONSTANTS = "bcdfhjklmnpqrstvwxz"
        _UPPER_CONSTANTS = "BCFGHJKLMNPQRSTVWXZ"
        Swedish vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']

        Write your TCs based on the lab instructions. One TC has been written below as an example
        
    '''

    @classmethod
    def setUpClass(cls):
        '''
            Set up shared resources = Class instance to access rover class methods
        '''
        cls.rv= rovar() 


    # Example test case to check lower case rover
    def test_enrove_small(self):
        self.assertEqual(self.rv.enrove('b'), 'bob')

     # Test cases for enrove (encoding) method

    def test_enrove_null(self):
        '''
            Test encoding with null input.
        '''
        self.assertIsNone(self.rv.enrove(None))

    def test_enrove_empty_string(self):
        '''
            Test encoding with an empty string.
        '''
        self.assertEqual(self.rv.enrove(''), '')

    def test_enrove_lowercase_consonant(self):
        '''
            Test encoding with a lowercase consonant.
        '''
        self.assertEqual(self.rv.enrove('b'), 'bob')

    def test_enrove_uppercase_consonant(self):
        '''
            Test encoding with an uppercase consonant.
        '''
        self.assertEqual(self.rv.enrove('B'), 'BOB')

    def test_enrove_vowel(self):
        '''
            Test encoding with a vowel (should remain unchanged).
        '''
        self.assertEqual(self.rv.enrove('a'), 'a')

    def test_enrove_number(self):
        '''
            Test encoding with a number (should remain unchanged).
        '''
        self.assertEqual(self.rv.enrove('1'), '1')

    def test_enrove_special_character(self):
        '''
            Test encoding with a special character (should remain unchanged).
        '''
        self.assertEqual(self.rv.enrove('!'), '!')

    def test_enrove_mixed_string(self):
        '''
            Test encoding with a mixed string (consonants, vowels, numbers, special characters).
        '''
        self.assertEqual(self.rv.enrove('Hello123!'), 'HOHelollolo123!') # I just had to replace "o" with "O"

    # Test cases for derove (decoding) method

    def test_derove_null(self):
        '''
            Test decoding with null input.
        '''
        self.assertIsNone(self.rv.derove(None))

    def test_derove_empty_string(self):
        '''
            Test decoding with an empty string.
        '''
        self.assertEqual(self.rv.derove(''), '')

    def test_derove_lowercase_consonant(self):
        '''
            Test decoding with a lowercase consonant.
        '''
        self.assertEqual(self.rv.derove('bob'), 'b')

    def test_derove_uppercase_consonant(self):
        '''
            Test decoding with an uppercase consonant.
        '''
        self.assertEqual(self.rv.derove('BOB'), 'B')

    def test_derove_vowel(self):
        '''
            Test decoding with a vowel (should remain unchanged).
        '''
        self.assertEqual(self.rv.derove('a'), 'a')

    def test_derove_number(self):
        '''
            Test decoding with a number (should remain unchanged).
        '''
        self.assertEqual(self.rv.derove('1'), '1')

    def test_derove_special_character(self):
        '''
            Test decoding with a special character (should remain unchanged).
        '''
        self.assertEqual(self.rv.derove('!'), '!')

    def test_derove_mixed_string(self):
        '''
            Test decoding with a mixed string (consonants, vowels, numbers, special characters).
        '''
        self.assertEqual(self.rv.derove('HoHelollolo123!'), 'Hello123!')
# Test cases for swedish vowels 
    def test_enrove_swedish_vowel_å(self):
      self.assertEqual(self.rv.enrove('å'), 'å')

    def test_enrove_swedish_vowel_ä(self):
      self.assertEqual(self.rv.enrove('ä'), 'ä')

    def test_enrove_swedish_vowel_ö(self):
      self.assertEqual(self.rv.enrove('ö'), 'ö')

    def test_derove_swedish_vowel_å(self):
      self.assertEqual(self.rv.derove('å'), 'å')

    def test_derove_swedish_vowel_ä(self):
      self.assertEqual(self.rv.derove('ä'), 'ä')

    def test_derove_swedish_vowel_ö(self):
      self.assertEqual(self.rv.derove('ö'), 'ö')


if __name__ == '__main__':
    print("***********START OF ALL TEST CASES RESULTS SHOWN BELOW**************")
    unittest.main(verbosity=2)


