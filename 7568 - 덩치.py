# -*- coding: utf-8 -*- 

def 비교(원본, 비교본):
    if 원본[0] < 비교본[0]:
        if 원본[1] < 비교본[1]:
            return 1
        else:
            return 0
    else:
        return 0

def 순위매기기(사람들):
    for i in 사람들:
        랭크 = 1
        for j in 사람들:
            if 비교(i, j) == 1:
                랭크 += 1
        print(랭크, end = " ")

회원수 = int(input())      
사람들 = []

for i in range(회원수):
    몸무게, 키 = map(int, input().split())
    사람들.append((몸무게, 키))
순위매기기(사람들)