from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

user = input('Enter your username without the @uottawa.ca part here: ')
passw = input('Enter your password here: ')
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

gmail = driver.find_element_by_id('identifierId')
gmail.send_keys(user+'@uottawa.ca')
driver.find_element_by_xpath("//*[@id='identifierNext']/content/span").click()
time.sleep(1)
elem0 = driver.find_element_by_id('username')
elem1 = driver.find_element_by_id('password')

elem0.click()
elem0.clear()
elem0.send_keys(user)

elem1.clear()
elem1.send_keys(passw)
elem1.send_keys(Keys.RETURN)
