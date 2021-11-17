"""
import sys

s = []
m = int(sys.stdin.readline().rstrip())

def calc(func, num = 0):
    
    global s
    
    if func == "add":
        if num not in s:
            s.append(num)
    elif func == "remove":
        if num in s:
            s.remove(num)
    elif func == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif func == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.append(num)
    elif func == "all":
        s = [i for i in range(1, 21)]
    elif func == "empty":
        s = []
        
for _ in range(m):
    
    cmd = sys.stdin.readline().rstrip()
    
    if cmd == "all" or cmd == "empty":
        calc(cmd)
    else:
        cmd = list(cmd.split())
        calc(cmd[0], int(cmd[1]))
        
        
"""------------------------------------------------------------------------------------"""

import sys

s = set()
m = int(sys.stdin.readline().rstrip())

def calc(func, num = 0):
    
    global s
    
    if func == "add":
        if num not in s:
            s.add(num)
    elif func == "remove":
        s.discard(num)
    elif func == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif func == "toggle":
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif func == "all":
        s = set([i for i in range(1, 21)])
    elif func == "empty":
        s = set()
        
for _ in range(m):
    
    cmd = sys.stdin.readline().rstrip()
    
    if cmd == "all" or cmd == "empty":
        calc(cmd)
    else:
        cmd = list(cmd.split())
        calc(cmd[0], int(cmd[1]))
"""