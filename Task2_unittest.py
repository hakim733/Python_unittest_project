import unittest
import re
from Task2 import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.text = """
        Hello! This is a sample text. Contact me at user@example.com. Python is awesome.
        The Python programming language is widely used. Python NLP! Check out https://example.com
        #Python #NLP Check out https://example.com.
        """
        self.tp = TextProcessor(self.text)

    def test_convert_to_lowercase(self):
        result = self.tp.convert_to_lowercase()
        expected = self.text.lower()
        self.assertEqual(result, expected)

    def test_extract_emails(self):
        result = self.tp.extract_emails()
        expected = ['user@example.com']
        self.assertEqual(result, expected)

    def test_find_hashtags(self):
        result, count = self.tp.find_hashtags()
        expected = ['#Python', '#NLP']  # Order updated
        self.assertEqual(sorted(result), sorted(expected))  # Sort both lists to ignore order
        self.assertEqual(count, 2)

    def test_find_urls(self):
        result = self.tp.find_urls()
        expected = ['https://example.com']  # Expecting one unique URL
        self.assertEqual(result, expected)

    def test_average_word_length(self):
        result = self.tp.average_word_length()
        expected = 4.52  # Adjust this if needed based on the actual count
        self.assertAlmostEqual(result, expected, places=2)

    def test_top_3_words(self):
        result = self.tp.top_3_words()
        expected = [('python', 4), ('is', 3), ('nlp', 2)]  # Adjusted based on the actual text
        self.assertEqual(result, expected)

    def test_longest_word(self):
        result = self.tp.longest_word()
        expected = 'programming'
        self.assertEqual(result, expected)

    def sentences_with_python(self):
        sentences = re.split(r'[.!?]\s*', self.text)  # Split into sentences and trim the spaces
       # Filter out sentences that do not contain 'Python' as a whole word
        return [s.strip() for s in sentences if re.search(r'\bPython\b', s)]
    
    def test_remove_punctuation(self):
        result = self.tp.remove_punctuation()
        expected = "Hello This is a sample text Contact me at userexamplecom Python is awesome The Python programming language is widely used Python NLP Check out httpsexamplecom Python NLP Check out httpsexamplecom"
        self.assertEqual(result, expected)


    def test_convert_numbers_to_words(self):
        self.text = "I have 1 apple, 2 oranges, and 10 bananas."
        self.tp = TextProcessor(self.text)
        result = self.tp.convert_numbers_to_words()
        expected = "I have one apple, two oranges, and ten bananas."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
