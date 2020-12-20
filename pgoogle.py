from selenium import webdriver
import random 

driver = webdriver.Chrome()
url = 'https://www.google.co.kr/preferences?hl=ko'
driver.get(url)

randomcountry = ["regiontGH","regiontZZ","regiontGA"]

optionbutton = driver.find_element_by_id(random.choice(randomcountry))
optionbutton.click()

okaybutton = driver.find_element_by_css_selector("div.goog-inline-block")
okaybutton.click()