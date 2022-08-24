n = input()
need = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0}

for text in n:
    if text in ['6', '9']:
        need['6'] += 1
    else:
        need[text] += 1
        
if need['6'] % 2 == 0:
    need['6'] = need['6'] // 2
else:
    need['6'] = need['6'] // 2 + 1
    
        
print(max(need.values()))