# coding=utf-8

import string
import numpy
import sklearn.svm as svm
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
import io
from collections import defaultdict
import random

tagsetDict = {"Np" : 0,
              "Nc" : 1,
              "Nu" : 2,
              "N" : 3,
              "V" : 4,
              "A" : 5,
              "P" : 6,
              "R" : 7,
              "L" : 8,
              "M" : 9,
              "E" : 10,
              "C" : 11,
              "CC" : 12,
              "I" : 13,
              "T" : 14,
              "Y" : 15,
              "Z" : 16,
              "X_train" : 17 }

wordBank = defaultdict()
f_tagged = io.open("corpus/VNTQcorpus-small.tagged.txt", encoding='utf-8').read()
f = io.open("corpus/VNTQcorpus-small.txt", encoding='utf-8').read()

# Separate train and test set
# train = f_tagged[:int(len(f)/2)]
# test = f_tagged[int(len(f)/2):]
train = f_tagged[:50000]
test = f_tagged[50000:100000]

# Get training data
for w in train.split():
    parts = w.split("/")
    if len(parts) == 1 or parts[1] not in tagsetDict:
        continue
    word = parts[0]
    pos = parts[1]
    if word not in wordBank:
        wordBank[word] = [pos]
    else:
        wordBank[word] += [pos]

print ("finished getting training data")

# Features
def feature(word):
    feat = [1]

    # label pos tags for each word
    posIdx_array = ([0] * len(tagsetDict))
    if word in wordBank:
        posSet = wordBank[word]
    else:
        posSet = list(tagsetDict.keys())[random.randint(0, 5)] # Naive: always choose N
        posIdx_array[tagsetDict[posSet]] = 1
        return feat + posIdx_array

    for pos in posSet:
        posIdx = tagsetDict[pos]
        posIdx_array[posIdx] += 1.0/len(wordBank[word])
    feat += (posIdx_array)

    return feat

# Create y (list of pos tags) and x (feature) data
y = []
X_train = []
for w in train.split():
    parts = w.split("/")
    word = parts[0]
    if len(parts) == 1 or parts[1] not in tagsetDict:
        continue
    y.append(wordBank[word][0]) # [0] for first word tagged pos
    X_train.append(feature(word))

print ("finished creating y and xtrain")

print ( len(X_train) )
print ( len(y) )

print(X_train[0:10])
train_fit = OneVsRestClassifier(LinearSVC(random_state=0)).fit(X_train,y)

print ("finished fitting")

X_test = []
correct_results = []
# Get testing data
for w in test.split():
    parts = w.split("/")
    if len(parts) == 1 or parts[1] not in tagsetDict:
        continue
    word = parts[0]
    pos = parts[1]
    if word in string.punctuation or word == ":.":
        continue
    X_test.append(feature(word))
    correct_results.append(pos)

print("finished getting testing data")

predicted_results = train_fit.predict(X_test)
print(predicted_results)

numCorrect = 0
for cor,pred in zip(correct_results, predicted_results):
    if cor == pred:
        numCorrect += 1

accuracy = 1.0*numCorrect/len(correct_results)
print(accuracy)