n = int(input())
m = int(input())

if m > 0:
    brokenNumbers = set(map(int, input().split()))
else:
    brokenNumbers = set()

minPress = abs(n - 100) # only +- 로만 조정(최대)

for channel in range(1000001): # i번채널로 숫자를 눌러 이동한 다음, +- 로 조정할 예정
    
    allPressable = True
    for char in str(channel):
        if int(char) in brokenNumbers:
            allPressable = False
            break   
        
    if allPressable: # 숫자만 눌러 i번으로 갈 수 있다면,
        minPress = min(minPress,        len(str(channel))            +    abs(n - channel))
                      #최소press횟수    #i번으로숫자로만이동   +    i번부터 가고싶은채널(n)까지 +-로 남은press횟수
               
print(minPress)