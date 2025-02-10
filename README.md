# Text Processing with Test-Driven Development (TDD)

## Project Overview
This project is a personal exploration of **Test-Driven Development (TDD)** in Python, focusing on text processing and analysis. The goal was to build a robust and well-tested Python application that performs various text manipulation tasks, such as extracting emails, identifying hashtags, and analyzing word frequency. The project also includes a fun implementation of the "Rövarspråket" language encoder and decoder.

The project was developed using **unit testing** and **code coverage** tools to ensure high-quality, maintainable code. It demonstrates my ability to write clean, modular code and follow TDD principles.

---

## Features

### Task 1: Rövarspråket Encoder and Decoder
Rövarspråket (also known as "Robber's Language") is a Swedish language game where consonants are doubled, and an "o" is inserted between them. Vowels, numbers, and special characters remain unchanged. For example:
- Input: `hello`
- Output: `hohelollolo`

This task includes:
- A Python implementation of the Rövarspråket encoder and decoder.
- Comprehensive unit tests to validate the functionality.

### Task 2: Text Analysis
This task focuses on text manipulation and analysis. The program performs the following operations:
1. Convert all words to lowercase.
2. Extract all email addresses mentioned in the text.
3. Find and count all unique hashtags (words or phrases starting with `#`).
4. Identify and list all URLs mentioned in the text.
5. Calculate the average word length in the document.
6. Determine the top 3 most frequent words in the text.
7. Find the longest word in the text.
8. Identify sentences containing the word "Python."
9. Remove all punctuation and special characters from the text.
10. Convert numerical figures (1-10) into their written-out forms (e.g., "1" becomes "one").

---

## Development Approach
This project was developed using **Test-Driven Development (TDD)**. For each feature, I:
1. Wrote unit tests to define the expected behavior.
2. Implemented the code to pass the tests.
3. Refactored the code to improve readability and performance.

I used Python's `unittest` framework for testing and the `coverage` tool to measure code coverage. The project achieved **high test coverage**, ensuring that the code is reliable and maintainable.

---

## Installation and Setup

### Prerequisites
1. **Python 3.x**: Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Visual Studio Code**: Download and install VS Code from [code.visualstudio.com](https://code.visualstudio.com/download).
3. **Coverage Tool**: Install the Python coverage tool using pip:
   ```bash
   python3 -m pip install coverage
