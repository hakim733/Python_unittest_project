import re
import string
from collections import Counter

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def convert_numbers_to_words(self):
        number_map = {
            1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
            7: "seven", 8: "eight", 9: "nine", 10: "ten"
        }

        def replace(match):
            number = int(match.group(0))
            return number_map.get(number, str(number))
        
        return re.sub(r'\b\d+\b', replace, self.text)  # Convert numbers to words.
    
    def remove_punctuation(self):
    # Remove punctuation but preserve numbers
       text_without_punctuation = re.sub(r'[^\w\s]', '', self.text)
    
    # Normalize whitespace to a single space
       text_no_extra_spaces = re.sub(r'\s+', ' ', text_without_punctuation)
    
    # Strip leading/trailing spaces
       cleaned_text = text_no_extra_spaces.strip()
    
       return cleaned_text


  

    def convert_to_lowercase(self):
        return self.text.lower()

    def extract_emails(self):
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.findall(email_pattern, self.text)

    def find_hashtags(self):
        hashtag_pattern = r'#\w+'
        hashtags = re.findall(hashtag_pattern, self.text)
        return sorted(hashtags), len(hashtags)  # Sort for consistent order

    def find_urls(self):
        url_pattern = r'https?://[^\s,!?]+'
        urls = re.findall(url_pattern, self.text)
        # Remove trailing punctuation marks and ensure no duplicates
        return sorted(set(url.rstrip(string.punctuation) for url in urls))

    def average_word_length(self):
        words = self.text.split()
        if not words:
            return 0
        # Remove punctuation and count only alphabetic words
        words = [word.strip(string.punctuation) for word in words if word.strip(string.punctuation).isalpha()]
        if not words:  # If all words are non-alphabetic
            return 0
        total_length = sum(len(word) for word in words)
        return round(total_length / len(words), 2)

    def top_3_words(self):
        words = self.text.split()
        word_count = Counter()
        for word in words:
            # Normalize: remove punctuation and convert to lowercase
            cleaned_word = word.strip(string.punctuation).lower()
            if cleaned_word and cleaned_word.isalpha():  # Only count valid words
                word_count[cleaned_word] += 1
        return word_count.most_common(3)  # Get the top 3 most common words

    def longest_word(self):
        words = self.text.split()
        longest = ""
        for word in words:
            cleaned_word = word.strip(string.punctuation)
            # Exclude words that are URLs or non-alphabetic
            if cleaned_word.isalpha() and len(cleaned_word) > len(longest):
                longest = cleaned_word
        return longest

    def sentences_with_python(self):
        sentences = re.split(r'[.!?]\s*', self.text)  # Split into sentences and trim the spaces
        # Filter out sentences that do not contain 'Python' as a whole word
        return [s.strip() for s in sentences if re.search(r'\bPython\b', s)]
