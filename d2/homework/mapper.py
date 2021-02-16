#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

for line in sys.stdin: # line 한 줄 씩 입력
    line = line.strip() # 개행 문자 (\r\n) 삭제
    word_list = line.split(',') # ','를 기준으로 line을 나눔
    
    stopwords = ['온라인','코로나19']

    
    for word in word_list: # 각 keyword를 입력 받아서 count를 1로 함
        if word in stopwords:
            continue

        count = 1
        print('{0}\\{1}'.format(word, count)) # reduce로 데이터 보냄
