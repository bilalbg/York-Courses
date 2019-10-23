import os
import webbrowser
import requests
import lxml
import time
from lxml import html
import selenium 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary()


driver = webdriver.Firefox(executable_path ='geckodriver' )
import splinter
from splinter import Browser
driver.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')
assert "York University" in driver.title
elem = driver.find_element_by_xpath("/html/body/p/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/ul/li[1]/ul/li[1]/a")
actions = ActionChains(driver)

driver.execute_script("window.open('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')")
time.sleep(2)
driver.close()
driver.switch_to.window(driver.window_handles[0])
#actions.key_down(Keys.CONTROL).click(elem).key_up(Keys.CONTROL).perform() --- doesnt work for some reason
#actions.key_down(Keys.SHIFT).click(elem).key_up(Keys.SHIFT).perform()
#elem[0].click()
#siz = len(handles)
#print(siz)
#print(WebDriverWait(driver, 10000).until(ExpectedConditions.number_of_windows_to_be(2)))
#handles = driver.window_handles
#print(handles)
#driver.switch_to.window(handles[1])
print(driver.current_url)
term = input("Enter the term(F/W/S): ")
if term.upper() in {'F', 'W'}:
     term = 'Fall/Winter 2018-2019'
else:
     term = 'Summer 2019'
#waita.until(ExpectedConditions.staleness_of(By.NAME, 'SessionPopUp'))
elem = driver.find_element_by_xpath(f"//*[contains(text(), '{term}')]")
elem.click()	

department = input('Enter the department: ')
department = department.upper()
elem = driver.find_element_by_xpath(f"//*[contains(text(), '{department}')]")
elem.click()

WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input")))

elem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input")
elem.click()

listelem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]").find_elements_by_css_selector("tr")
elemText = None
while elemText == None:
     course = input("Enter course number: ")
     for w in listelem:
          elemText = w
          #print(elemText.text)
          if course in elemText.text:
               elemText = elemText.find_element_by_xpath(".//td[3]/a")
               elemText.click()
               break
          else:
               elemText = None
     if elemText == None:
          print("Error: Course not found, please enter another course.")


print("Course Description: ")
elem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/p[3]")
print(elem.text)
#elem.click()
link = driver.current_url
print (link)	
#print(ur)
#print (req.content)
#req2 = requests.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/wa/DirectAction/cds', auth = ('bilalb', '0409choa'))
#req2 = requests.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/wa/DirectAction/cds')
#print (req2.content)
#webbrowser.open('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/wa/DirectAction/cds')
""" req = requests.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/8/wo/4bcnHHopsDqpyjpDv4UIlM/0.3.4.8.0')
tree = lxml.html.fromstring(req.content)
elements = tree.get_element_by_id('eecs')
for el in elements:
	print el.text_content() """
#print (req.content)
#inspect element to check option values and stuff - network tab
