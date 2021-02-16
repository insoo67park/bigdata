#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

for line in sys.stdin:
    line = line.strip()
    word_list = line.split()
    stopwords = ['영화','영화.','본','다','또','진짜','잘','너무','그','이','그냥','더','수','정말', '10', '9', '8', '7', '6', '5', '4', '3', '2', '1']

    for word in word_list:
        if word in stopwords:
            continue
        count = 1
        print('{0}\\{1}'.format(word, count)) 
