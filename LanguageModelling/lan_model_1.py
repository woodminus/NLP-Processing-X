# Goal:
# Apply different language models like unigram, bigram, trigram on the given twitter corpus and codemixed corpus.
# Find CMI and Perplexity for each of the above models.
# Compare perplexity and analyse the best among them.

# Steps:
# Preprocess the data (Apply tokenization and stemming).
# Store all the words(V) in a dictionary with unique id's and their frequencies in a list.
# Create a V*V matrix with all bigram totalLiness.
# Apply add-one smoothing on the matrix.
# For every sentence in the corpus, find probabilities P( word(n)|word(n-1) ) of each word in the sequence and thereby find the perplexity of each sentence.
# Take the average of all the perplexities.
# Analyse the perplexities of different models.

# Variables:
# wordDict: Dictionary which stores all the words.
# index: To give unique id's to every word in the dictionary.
# V: Vocabulary size.

# Code
import numpy as np
import nltk
import os
import sys
# from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
import json
import re
# porter = PorterStemmer()

# Put words in dictionary
index=0		# Index of word in dictionary
totalLines=0		# Total number of lines
tokens=0	# Total number of words in the corpus
V=0
V_tri=0
matrix={}
triMatrix = {}
wordDict = {}
bigram_perplex=[]
secondDict={}

def get_count():
	global index
	return index

def createBiMatrix():
	global matrix
	matrix = {}

def createTriMatrix():
	global triMatrix
	triMatrix = {}

def putInDict(filename):
	global totalLines, tokens, index
	with open(filename) as file:
		for line in file:
			totalLines+=1
			# line = "My name is Abhishek and the name of the boy who was standing there is not Abhishek"
			listOfWords = wordpunct_t