# Read from the file words.txt and output the word frequency list to stdout.
#!/bin/bash

cat words.txt |
tr -s ' ' '\n' |
sort |
uniq -c |
sort -nr |
awk '{print $2, $1}'

# # Convert spaces into new lines
# tr -s ' ' '\n' < words.txt > words_one_per_line.txt

# # Sort words alphabetically so same words come together
# sort words_one_per_line.txt > sorted_words.txt

# # Count repeated words
# uniq -c sorted_words.txt > counted_words.txt

# # Sort by frequency descending
# sort -nr counted_words.txt > sorted_counted_words.txt

# # Print word first, then count
# awk '{print $2, $1}' sorted_counted_words.txt
