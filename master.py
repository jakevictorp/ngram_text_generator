#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from ngram import *
from seed_gen import *


import argparse
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)


parser = argparse.ArgumentParser()


# add argument for the name of the text file to use as training data
parser.add_argument('--txtfile', '-t', type=str, help='The name of the .txt file for training')
# add argument for length of n-gram
parser.add_argument('--ngram', '-n', type=int, help='The number of characters/segments/words in each n-gram (i.e. n)')
# add argument for smoothing factor "k"
parser.add_argument('--ksmoothing', '-k', type=float, help='The value of k for add-k smoothing')
# add argument for whether or not to use log probabilities
parser.add_argument('--logprob', '-l', type=str, help='Set as "log" to use (natural) log probabilities, set as "nolog" to use raw probabilities (defaults to log probabilities)', default="log")
# add argument for desired length (in characters) of generated text
parser.add_argument('--genlen', '-g', type=int, help='The number of characters of random text to generate')
# add argument for whether or not to select next character only from among maximum likelihoods or randomly from probability distribution
parser.add_argument('--max_rand', '-m', type=str, help='Set as "max" to select next character only from among maximum likelihoods (defaults to random selection)', default="rand")



args = parser.parse_args()

txt = args.txtfile
n = args.ngram
k = args.ksmoothing
inp_logprob = args.logprob
maxrand = args.max_rand
genlen = args.genlen
if inp_logprob == "nolog":
    logprob = False
elif inp_logprob == "log":
    logprob = True
else:
    logprob = True
if maxrand == "max":
    max_rand = True
elif maxrand == "rand":
    max_rand = False
else:
    max_rand = False



train_string = GetTrainingText(txt)
vocab = GetVocab(train_string)
counts_dict = GenCountsDict(train_string, n)
counts_n_min_one = GenCountsDict_n_min_one(train_string, n)
model = GenModel(counts_dict, counts_n_min_one, k, vocab, logprob)


seed = SelectSeed(train_string, n)


# pp.pprint(NextChar(seed, model, max_rand))
print(GenText(seed, model, genlen, n, max_rand))


# random_text = GenText(seed, model)

# pp.pprint(model)