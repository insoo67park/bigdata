#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

for line in sys.stdin:
    # ","기준으로 나누고, 개행 문자 등을 삭제
    numbers_str = line.strip().split(",")

    print(" ".join(numbers_str)) # 각 line 별로 combiner로 보냄
