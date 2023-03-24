import sys
import string

# Read filename from command line argument
filename = sys.argv[1]

# Open file and read contents into a string
with open(filename) as file:
    text = file.read()

# Remove punctuation from text and convert to lowercase
text = text.translate(str.maketrans('', '', string.punctuation))
text = text.lower()

# Split text into words
words = text.split()

# Count frequency of each word
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Sort words by frequency
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

# Print sorted words to console
for word, count in sorted_words:
    print(f"{word}: {count}")
