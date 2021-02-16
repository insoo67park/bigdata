#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
prev_empno = None
mgr_name = None
enames = []

for key_value in sys.stdin:
    key_value = key_value.strip()
    empno, table_value = key_value.split("\t") 
    table, value = table_value.split(",") 
 
    if prev_empno == empno:
        if table == 'e': 
            enames.append(value)
        else:
            mgr_name = value
    else: 
        if prev_empno and enames:
            for ename in enames: 
                print("%s, %s"%(ename, mgr_name))

        mgr_name = None 
        enames = []
        
        if table == 'e':
            enames = [value]
        else:
            mgr_name = value
        prev_empno = empno

if prev_empno and enames: 
    for ename in enames: 
        print("%s, %s"%(ename, mgr_name))
