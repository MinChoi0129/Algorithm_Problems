import urllib.request
import os
month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

url = 'https://sugang.gnu.ac.kr/login'
# while True:
#     os.system('cls')
date = urllib.request.urlopen(url).headers['Date'][5:-4]
d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {hour}시 {min}분 {sec}초')