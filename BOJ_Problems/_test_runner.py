from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import sys, time

browser = webdriver.Chrome()
browser.get("https://www.gnu.ac.kr/main/ad/fm/foodmenu/selectFoodMenuView.do?mi=1341")
browser.execute_script("\
    frm = document.getElementById('detailForm'); \
    frm.restSeq.value = '5';\
    frm.action = '/' + \
    document.getElementById('sysId').value + \
    '/ad/fm/foodmenu/selectFoodMenuView.do?mi=' + \
    document.getElementById('mi').value;\
    frm.submit();"
)
innerhtml = browser.execute_script("return document.body.innerHTML;")
data = BeautifulSoup(innerhtml, 'html.parser').find("div", "BD_table scroll_gr main").select("tbody > tr")[1].select("div p")[:5]

day_type = ['월요일', '화요일', '수요일', '목요일', '금요일']
food_type = ['비빔밥/뚝배기', '양식메뉴', '세트메뉴']
menu = [str(d)[12:-4].split('<br/>')[1:-1] for d in data]

def sendKakaoTalkMessage(mode):
    if mode == 'today':
        today = datetime.today().weekday()
        print("=======================================================")
        print("[ 오늘은 " + day_type[today] + "입니다 ]")
        print(food_type[0], "\t : ", list(menu[today])[0])
        print(food_type[1], "\t : ", list(menu[today])[1])
        print(food_type[2], "\t : ", ''.join(list(menu[today])[3:]))
    elif mode == 'weekday':
        for i in range(5):
            print("=======================================================")
            print("[" + day_type[i] + "]")
            print(food_type[0], "\t : ", list(menu[i])[0])
            print(food_type[1], "\t : ", list(menu[i])[1])
            print(food_type[2], "\t : ", ''.join(list(menu[i])[3:]))
sendKakaoTalkMessage('weekday')
browser.close()
# schedule.every().monday.at("10:30").do(sendKakaoTalkMessage)
# schedule.every().tuesday.at("10:30").do(sendKakaoTalkMessage)
# schedule.every().wednesday.at("10:30").do(sendKakaoTalkMessage)
# schedule.every().thursday.at("10:30").do(sendKakaoTalkMessage)
# schedule.every().friday.at("10:30").do(sendKakaoTalkMessage)
# schedule.every(10).seconds.do(sendKakaoTalkMessage, 'today')
# while True:
#     schedule.run_pending()
#     browser.close()
    