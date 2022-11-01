from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import schedule, json, requests

day_type = ['월요일', '화요일', '수요일', '목요일', '금요일']
food_type = ['비빔밥/뚝배기', '양식메뉴', '세트메뉴']

def generateMenuMesseage(menu):
    txt = "=======================================================\n"
    today = datetime.today().weekday()
    txt += "[ 오늘은 " + day_type[today] + "입니다 ]" + '\n'
    txt += str(food_type[0]) + "\t : " + str(list(menu[today])[0]) + '\n'
    txt += str(food_type[1]) + "\t : " + str(list(menu[today])[1]) + '\n'
    txt += str(food_type[2]) + "\t : " + ''.join(list(menu[today])[3:]) + '\n'
    
    return txt

def sendKakaoTalkMessage(menu):
    message = generateMenuMesseage(menu)
    print("전송시각 : ", datetime.now())
    print(message)
    print("전송완료")

def runKakaoTalkBot():
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
    innerhtml: str = browser.execute_script("return document.body.innerHTML;")
    food_html: list = BeautifulSoup(innerhtml, 'html.parser').find("div", "BD_table scroll_gr main").select("tbody > tr")[1].select("div p")[:5]
    menu = [str(bs4_element)[12:-4].split('<br/>')[1:-1] for bs4_element in food_html] # double list
    sendKakaoTalkMessage(menu)
    browser.close()

schedule.every(5).seconds.do(runKakaoTalkBot)

while True:
    schedule.run_pending()