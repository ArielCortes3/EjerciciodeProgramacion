"""Module to read words from a file and count their frequencies."""
# pylint: disable=invalid-name

import sys
import time

def read_words_from_file(filename):
    """Reads words from a file and returns a list of words."""
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words.extend(line.strip().split())
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit(1)
    return words

def count_word_frequencies(words):
    """Counts the frequency of each word in a list."""
    word_counts = {}
    for word in words:
        cleaned_word = ''.join(filter(str.isalnum, word)).lower()
        if cleaned_word:
            word_counts[cleaned_word] = word_counts.get(cleaned_word, 0) + 1
    return word_counts

def main():
    """Main function to handle file input and output processing."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    words = read_words_from_file(filename)
    if not words:
        print("No valid data to process.")
        sys.exit(1)

    word_frequencies = count_word_frequencies(words)
    elapsed_time = time.time() - start_time

    results = "\n".join([f"{word}: {count}" for word, count in sorted(word_frequencies.items())])
    results += f"\nExecution Time: {elapsed_time:.5f} seconds\n"

    print(results)
    with open("WordCountResults.txt", "w", encoding='utf-8') as output_file:
        output_file.write(results)

if __name__ == "__main__":
    main()
