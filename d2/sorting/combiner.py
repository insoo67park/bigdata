#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

for line in sys.stdin:
    numbers_str = line.split() # " "기준으로 나눔
    numbers_int = [int(i) for i in numbers_str] # string형을 int형으로 바꿈
    
    # mapper 별로 숫자를 정렬하여 reducer로 보냄
    # print(" ".join([str(i) for i in sorted(numbers_int)]))
    print(" ".join([str(i) for i in sorted(numbers_int, reverse=True)]))