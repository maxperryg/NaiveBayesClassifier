import os
import sys
import json
import math

def create_documents(documents, classes):
    training_file = sys.argv[1]
    processed_feature_vectors = open(training_file, 'r')
    for line in processed_feature_vectors.readlines():
        vector = json.loads(line)
        documents.append(vector)
        key = list(vector.keys())[0]
        if key in classes:
            classes[key].append(vector[key])
        else:
            classes[key] = [vector[key]]


def train_naive_bayes(number_of_documents, classes):
    prior_probabilities = {}
    num_of_words_in_each_class = {}
    bow = {}
    for label, document in classes.items():
        num_of_documents_in_class = len(document)
        prior_probabilities[label] = math.log2(num_of_documents_in_class/number_of_documents)
        bow[label] = {}
        num_of_words_in_each_class[label] = 0
        for doc in document:
            for word, value in doc.items():
                num_of_words_in_each_class[label] += value
                if word in bow[label]:
                   bow[label][word] += value
                else:
                    bow[label][word] = value
        print(prior_probabilities)
        print(bow)


test_file = sys.argv[2]
parameters_file = sys.argv[3]
predictions_file = sys.argv[4]
vocabulary = set([line.rstrip() for line in open('Reviews/imdb.vocab')])

documents = []
classes = {}

create_documents(documents, classes)
number_of_documents = len(documents)
train_naive_bayes(number_of_documents, classes)





# with open(training_file) as training_file:
#     for