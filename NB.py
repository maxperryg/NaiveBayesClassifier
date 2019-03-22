import os
import sys

training_file = sys.argv[1]
test_file = sys.argv[2]
parameters_file = sys.argv[3]
predictions_file = sys.args[4]


training_feature_vectors = []

# with open(training_file) as training_file:
#     for