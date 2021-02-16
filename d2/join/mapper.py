#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

for line in sys.stdin: # line 한 줄 씩 입력
    line = line.strip() # 개행 문자 삭제
    tuple_list = line.split(",") # ','를 기준으로 line을 나눔
    
    # hadoop은 폴더의 모든 파일을 한 번에 입력 받음
    # emp file과 dept file을 attribute (column) 수로 구분
    # attribute가 emp file은 8개, dept file은 3개
    
    if len(tuple_list) == 8: # emp file
        ename = tuple_list[1]
        deptno = tuple_list[7]
        
        # key: deptno  value: emp,ename
        print('{0}\t{1}'.format(deptno, 'emp,'+ename)) 
        
    else: # dept file
        loc = tuple_list[2]
        deptno = tuple_list[0]
        
        # key: deptno  value: dept,loc
        print('{0}\t{1}'.format(deptno, 'dept,'+loc))
