#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from random import choices
from ngram import *









# print(GetTrainingText('fa.txt'))

# GetTrainingText(txt)


def SelectSeed(txt, n):
    secure_random = random.SystemRandom()
    seed_index = secure_random.choice(range(len(txt) - n))
    seed = txt[seed_index:(seed_index+n-1)]
    return seed

def NextChar(seed, model, max_rand):   
    secure_random = random.SystemRandom()
    candidates = []
    for ngram in model:
        if ngram[0:n-1] == seed:
            candidates.append((ngram, seed))
    if max_rand == True:
        # move through candidate list and select the candidate with the highest probability that is seen first
        # randomly shuffle the candidate list to ensure it is a random selection from among the equally most likely candidates
        unshuffled = candidates.copy()
        random.shuffle(candidates)
        # set max_prob to very low negative number to account for optional log probabilities
        max_prob = -100
        for c in candidates:
            if model[c[0]] > max_prob:
                winner = c[0]
                max_prob = model[c[0]]
            else:
                continue
    else:
        # select randomly from among candidates's probability distribution
        cands = []
        weights = []
        for c in candidates:
            cands.append(c[0])
            weights.append(model[c[0]])
        # note: random.choices returns a list with one element, so select first element        
        winner = choices(cands, weights)[0]
    return winner

def GenText(seed, model, length, n, max_rand):
    text = seed
    for i in range(length):
        current_segment = text[-(n-1):]
        next_char = NextChar(current_segment, model, max_rand)[-1]
        text = text + next_char
    return text
    
    
    
    
    
    
    
    
