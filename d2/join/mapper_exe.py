#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys

for line in sys.stdin:
    line = line.strip()
    tuple_list = line.split(",")
    
    if len(tuple_list) == 8: # emp file
        ename = tuple_list[1]
        empno = tuple_list[0]
        mgr = tuple_list[3]
        
        print('{0}\t{1}'.format(mgr, 'e,'+ename)) 
        print('{0}\t{1}'.format(empno, 'm,'+ename)) 
