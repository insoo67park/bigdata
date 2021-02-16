#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
merged_numbers = []

for line in sys.stdin:
    numbers_str = line.split()
    numbers_int = [int(i) for i in numbers_str]
    if len(merged_numbers) == 0: # 첫 입력인 경우
        merged_numbers = numbers_int
    else: # 첫 입력이 아니면, 이 전 merged list와 새로운 list를 merge함
        l1 = merged_numbers
        l2 = numbers_int
        new_merged_numbers = []
        index1 = 0
        index2 = 0
        while index1 < len(l1) and index2 < len(l2): # 둘 중 한 list가 없어질 때 까지 merge함
            a = l1[index1]
            b = l2[index2]
            if a > b:
                new_merged_numbers.append(a)
                index1 += 1
            else:
                new_merged_numbers.append(b)
                index2 += 1
        # 남은 list를 그대로 뒤에 붙임
        if index1 == len(l1) and index2 < len(l2):
            new_merged_numbers.extend(l2[index2: ])
        if index1 < len(l1) and index2 == len(l2):
            new_merged_numbers.extend(l1[index1: ])

        merged_numbers = new_merged_numbers
print(" ".join([str(i) for i in merged_numbers])) # merge가 끝난 list를 출력
