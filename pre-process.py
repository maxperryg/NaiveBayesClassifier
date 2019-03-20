import sys
import os
import re

reviews_folder = sys.argv[1]

positive_folder = os.path.join(reviews_folder, "pos")
negative_folder = os.path.join(reviews_folder, "neg")

punctuation = '!"*+,-./:;<=>?@[\\]^_`{|}~'


ignore_punctuation = '"'

for file in os.listdir(positive_folder):
    if file.endswith(".txt"):
        review_file = open(os.path.join(positive_folder, file), "r")
        review_text = review_file.read()
        review_text = ''.join(c for c in review_text if c not in punctuation)

# print(reviews_folder)
# print(positive_folder)
# print(os.listdir(positive_folder), "\n\n\n\n\n")
# print(negative_folder)
# print(os.listdir(negative_folder))