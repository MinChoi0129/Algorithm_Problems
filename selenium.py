from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(1)

driver.find_elements_by_name("username")[0].send_keys("testId@gmail.com") #아이디 입력
driver.find_elements_by_name("password")[0].send_keys("testPassword") #비밀번호 입력
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
#로그인 성공

LoginPopup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
LoginPopup.send_keys(Keys.ENTER)
#로그인 저장 팝업 아니오 클릭

AlarmPopup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
AlarmPopup.send_keys(Keys.ENTER)
time.sleep(2)
#알람팝업 아니오 클릭

serch = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
serch.send_keys('#좋아요')
time.sleep(3)
serch.send_keys(Keys.ENTER)
serch.send_keys(Keys.ENTER)
# #좋아요 검색 후 첫번째 해쉬태그로 이동
# 엔터를 두번 누르는 이유는 첫번째 해쉬태그를 선택 후 그 다음 엔터로 들어가야하기 때문이에요.


#imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
[출처] #1 [파이썬 셀레니움 프로젝트] - 인스타그램 로그인 및 좋아요 자동화 (자동 로그인, 해쉬태그 검색)|작성자 JaeYoonLee