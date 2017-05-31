#coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# https://github.com/SeleniumHQ/selenium/issues/1689
chrome_options = Options()

# Private browsing
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome('C:\Users\Kai-i5\GitHub\python\PycharmProjects\scrapy_tutorial\download\chromedriver.exe', chrome_options=chrome_options) #.Firefox()
driver.get("https://www.facebook.com/profile.php?id=100011632713288")
inputEmail = driver.find_element_by_id("email")
inputEmail.send_keys("t104368014@ntut.edu.tw")
inputPass = driver.find_element_by_id("pass")
inputPass.send_keys("t104368014")
inputPass.submit()


# page_text = (driver.page_source).encode('utf-8')
# soup = BeautifulSoup(page_text)
# parse_data = soup.get_text().encode('utf-8').split('Jimmy Lin')#if you use your name extactly how it is displayed on facebook it will parse all post it sees, because your name is always in every post.
# latest_message = parse_data[3]
# driver.close()
# print latest_message

page_text = (driver.page_source).encode('utf-8')
soup = BeautifulSoup(page_text)
parse_data = soup.get_text().encode('utf-8').split('Jimmy Lin')
latest_message = parse_data[4].split('.')
results = soup.findAll("div", {"aria-label" : "動態"})

for newsfeed in results:
    print newsfeed.text

driver.close()
time = latest_message[0]
message = latest_message[1]
print time,message

