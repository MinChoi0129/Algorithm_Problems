import sys, datetime
input = lambda : sys.stdin.readline().rstrip()

def getPi(n, i, tn, ti): # 'i' starts from 1
    return max(0.5 ** round((tn - ti).total_seconds() / 31536000, 10), 0.9 ** (n - i))
    
n = int(input())

if n == 0: print(0)
else:
    timelines = []
    for _ in range(n):
        date, time, level = input().split(' ')
        timelines.append([datetime.datetime.strptime(date + ' ' + time, '%Y/%m/%d %H:%M:%S'), float(level)])
        
    numerator, denominator = 0, 0
    for i in range(n): # 'i' starts from 0 (required +1 for function getPi)
        numerator += (getPi(n, i + 1, timelines[-1][0], timelines[i][0]) * timelines[i][1])
        denominator += getPi(n, i + 1, timelines[-1][0], timelines[i][0])
    print(round(numerator / denominator))

'재미삼아 숏코딩'
# import datetime
# def Pi(n,i,tn,ti): return max(0.5**((tn-ti).total_seconds()/31536000),0.9**(n-i))
# n,u,d,t=int(input()),0,0,[]
# if n:
#     for _ in range(n):dt,tm,lv=input().split();t.append([datetime.datetime.strptime(' '.join([dt,tm]),'%Y/%m/%d %H:%M:%S'),int(lv)])
#     for i in range(n):u+=(Pi(n,i+1,t[-1][0],t[i][0])*t[i][1]);d+=Pi(n,i+1,t[-1][0],t[i][0])
#     print(round(u/d))
# else:print(0)