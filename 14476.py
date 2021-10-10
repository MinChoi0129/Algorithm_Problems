from math import gcd
from copy import deepcopy as DC

def myGCD(numbers):
    currentGCD = numbers[0]
    for i in range(1, len(numbers)):
        currentGCD = gcd(currentGCD, numbers[i])
    return currentGCD

n = int(input())
numbers = map(int, input().split())

max_gcd = -1
k = -1
for i in range(n):
    copied_numbers = [*DC(numbers)]   
    popped_number = copied_numbers.pop(i)
    gcd_number = myGCD(copied_numbers) 
    
    if popped_number % gcd_number != 0:
        max_gcd = max(max_gcd, gcd_number)
        k = popped_number

if max_gcd != -1: print(max_gcd, k)
else: print(max_gcd)