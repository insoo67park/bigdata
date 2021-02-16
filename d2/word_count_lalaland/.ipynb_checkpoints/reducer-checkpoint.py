#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
prev_word = None
counts = 0

for word_count in sys.stdin:
    word, count = word_count.split("\\") 
    count = int(count)
    
    if prev_word == word:
        counts += count
        
    else: 
        if prev_word: 
            print("%s: %s"%(prev_word, counts))
        
        counts = count
        prev_word = word
if prev_word:
    print("%s: %s"%(prev_word, counts))
