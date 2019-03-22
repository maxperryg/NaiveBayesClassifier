import sys
import os


def count_frequencies(text):
    freq = {}
    for word in text:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq


def remove_unseen_words(words, vocab):
    for i in range(len(words)):
        if words[i] not in vocab:
            words.pop(i)


vocabulary = set([line.rstrip() for line in open('Reviews/imdb.vocab')])

punctuation = {'"', '*', '+', ',', '.', '/', '<', '>', '@', '^', '_', '`', '{', '|', '~'}

reviews_folder = sys.argv[1]

classes = os.listdir(reviews_folder)

class_0_folder = os.path.join(reviews_folder, classes[0])
class_1_folder = os.path.join(reviews_folder, classes[1])

bag_of_words = {classes[0]:{}, classes[1]:{}}

all_class_0 = ""
for file in os.listdir(class_0_folder):
    if file.endswith(".txt"):
        review_file = open(os.path.join(class_0_folder, file), "r")
        review_text = review_file.read()
        processed_text = ""
        for c in review_text:
            if c in '!?':
                processed_text += " " + c.lower()
                continue
            if c not in punctuation:
                processed_text += c.lower()
    all_class_0 += processed_text + " "
all_class_0 = all_class_0.split()
remove_unseen_words(all_class_0, vocabulary)
all_class_0 = count_frequencies(all_class_0)
bag_of_words[classes[0]] = all_class_0

print("\n preprocessed reviews in", classes[0], ":\n")
print("\t", all_class_0)

all_class_1 = ""
for file in os.listdir(class_1_folder):
    if file.endswith(".txt"):
        review_file = open(os.path.join(class_1_folder, file), "r")
        review_text = review_file.read()
        processed_text = ""
        for c in review_text:
            if c in '!?':
                processed_text += " " + c.lower()
                continue
            if c not in punctuation:
                processed_text += c.lower()
    all_class_1 += processed_text + " "
all_class_1 = all_class_1.split()
remove_unseen_words(all_class_1, vocabulary)
all_class_1 = count_frequencies(all_class_1)
bag_of_words[classes[1]] = all_class_1

print("\n preprocessed reviews in", classes[1], ":\n")
print("\t", all_class_1)

print("\n\n", bag_of_words)

