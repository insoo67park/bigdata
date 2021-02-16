#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
prev_word = None
counts = 0

# (keyword, count)하나의 pair가 입력 됨
# 같은 keyword가 묶여서 연속으로 입력 됨
# ex) (백신, 1) (백신, 1) (코로나, 1) (거리두기, 1)
for word_count in sys.stdin:
    word, count = word_count.split("\\") # map에서 보낸 "key$value"를 $로 나눠서 저장
    count = int(count) # string 형식을 int형식으로 다시 바꿔 줌
    
    if prev_word == word: # 이전 입력과 같은 keyword가 들어오면 count함
        counts += count
        
    else: # 새로운 keyword가 들어왔을 때
        if prev_word: # 첫 입력이 아니면, keyword랑 keyword 수 파일로 출력
            print("%s: %s"%(prev_word, counts))
        
        # 새로운 keyword에 대해 count 함
        counts = count
        prev_word = word

if prev_word: # 마지막 keyword에 대해 저장
    print("%s: %s"%(prev_word, counts))
