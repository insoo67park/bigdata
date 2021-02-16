#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
prev_deptno = None
location = None
enames = []

# 입력: (deptno (dept,loc)) 또는 (deptno (emp,ename)), 같은 deptno가 연속으로 입력 됨
#   ex) (10 (emp,miller)) (10 (dept, new york)) 
for key_value in sys.stdin:
    key_value = key_value.strip()
    deptno, table_value = key_value.split("\t") # map의 출력을 "\t"로 나눔
    table, value = table_value.split(",") # value에서 file 이름을 “,"로 나눔
 
    if prev_deptno == deptno: # 이전 입력과 같은 deptno가 들어왔을 때
        if table == 'emp': # file 이름이 emp 이면, enames list에 추가
            enames.append(value)
        else: # file 이름이 dept 이면, location에 저장
            location = value
    else: # 새로운 deptno가 들어왔을 때
        if prev_deptno and location and enames: # 첫 입력이 아니면,
            for ename in enames: # ename과 location을 맞춰서 파일로 출력
                print("%s, %s"%(ename, location))

        location = None # ename과 location을 초기화
        enames = []
        
        if table == 'emp': # 새로운 deptno에 대해 ename or loc 저장
            enames = [value]
        else: # table == 'dept'
            location = value
        prev_deptno = deptno

if prev_deptno and location and enames: # 마지막 deptno에 대해
    for ename in enames: # ename과 location을 맞춰서 파일로 출력
        print("%s, %s"%(ename, location))
