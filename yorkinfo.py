import os

import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import \
    expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait

#binary = FirefoxBinary()
ff_options = webdriver.FirefoxOptions()
ff_options.binary = FirefoxBinary()
ff_options.binary_location = '/usr/bin/firefox'
ff_options.headless = True
# def signin(self, user, passw):
     
ignore = {"Type", "Day", "Start", "Time","Duration","Location", "Time","Cat #", "Instructor", 
           "Notes/Additional Fees"}
timeinfo = []
newstr = ""
     

driver = webdriver.Firefox(executable_path ='geckodriver', options=ff_options)
waita = WebDriverWait(driver, 500)
driver.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')
assert "York University" in driver.title
elem = driver.find_elements_by_xpath("//*[contains(text(), 'Subject')]")
elem[0].click()
while True:
 	term = input("Enter the term(F/W/Y/S): ")
 	if term.upper() in {'F', 'W', 'Y'}:
 	     setterm = 'Fall/Winter'
 	     break
 	elif term.upper() == 'S':
 	     setterm = 'Summer'
 	     break
 	else:
 	     print("Incorrect term entered. " + str(term))
#waita.until(ExpectedConditions.staleness_of(By.NAME, 'SessionPopUp'))

elem = driver.find_element_by_xpath(f"//*[contains(text(), '{setterm}')]")
elem.click()	



while True:
      department = input('Enter the department: ')
      try:
          elem = driver.find_element_by_xpath(f"//*[contains(text(), '{department.upper()}')]")
          elem.click()
          break
      except:
          print("Department not found.")
#WebDriverWait(driver, 10).until(ExpectedConditions.element_to_be_clickable((By.XPATH, "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input")))

elem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input")
elem.click()

listelem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]").find_elements_by_css_selector("tr")
elemText = None
while True:
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
	     print("Error: Course not found")
     else:
	     break

link = driver.current_url
#print (link)	

basetable = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody"

#lenbigtable = len(elem[0].find_elements_by_css_selector('tr'))
setxpath = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr"
breaks = True 
b = c = 0
y = 1
while breaks:
     #a =
     while True:
          d = 0
          try:
               setnewxpath = setxpath + "[" + str(y) + "]/td/table/tbody/tr[3]/td/table/tbody" #before td
               elem = driver.find_element_by_xpath(setnewxpath) 
               #print (setnewxpath)
          except:
               breaks = False
               break
          #print(elem)
          timeinfo.clear()
          #newstr = ""
          termsec = driver.find_elements_by_xpath("//*[contains(text(), 'Section')]")
          #print (str(c))
          
          if term.upper() in termsec[c].text or 'Y' in termsec[c].text: 
               None
          else:
               #print(term.upper() + "notin" + termsec[c].text)
               #print(str(c))
               c+=2
               y+=1
               break
          print (termsec[c].text)
          
          sectiontable = driver.find_elements_by_xpath("//*[contains(text(), 'Section Director')]")
          out = (((sectiontable[b]).text).split('.'))
          print(out[1])
          innertables = elem.find_elements_by_css_selector('td')
          #print("-" + innertables[23].text + "-")
          #print("------")
          #print(innertables.text)
          for timestr in innertables:
               #print (texts.text)
               timestr = timestr.text
               if any(z in timestr for z in [" - Course Materials", "Expanded Course Description", "enrolment"]) or timestr in ignore:
                    None
               else:
                    #print(timestr)
                    if  any(types in timestr for types in ["LECT ","TUTR", "LAB"]):
                         newstr = (newstr + "Type: " + timestr + " ")
                         timeinfo.append(timestr)
                    elif ':' in timestr:
                         if len(timestr.split(" ")) > 2:
                              if "\n" in timestr:
                                   timeinfo.append(timestr.split("\n"))
                              else:
                                   timeinfo.append(timestr)
                         
                    elif len(timestr.split(" ")) == 6:
                         newstr = (newstr + " Course Code: " + timestr)
                    else:
                         splitter = timestr.split(" ")
                         #if len(timestr.split(" ")) != 2:
                         if timestr is " ":
                              None
                         if len(splitter) == 2:
                              #newstr = (newstr + " Instructor:" + timestr + " ")
                              if timestr is "":
                                   timeinfo.append("Instructor: (No Listed Professor)")
                              else:
                                   timeinfo.append("Instructor: " + timestr)
               newstr += "\n"
                                   
          
          print("Info for this section: ")
          #timeinfo = list(dict.fromkeys(timeinfo))
          print(timeinfo)
          print("\n")
          
          b+=1 
          #a+=1 
          c+=2
          y+=1
     
     #LECTR/TUTR/LAB
#print(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[1]/td/table/tbody/tr[3]/td/table/tbody/tr[4]/td[4]/a").text)
driver.quit()
#print(ur)
#print (req.content)
#print (req2.content)
#webbrowser.open('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/wa/DirectAction/cds')
""" req = requests.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm.woa/8/wo/4bcnHHopsDqpyjpDv4UIlM/0.3.4.8.0')
tree = lxml.html.fromstring(req.content)
elements = tree.get_element_by_id('eecs')
for el in elements:
	print el.text_content() """
#print (req.content)
#inspect element to check option values and stuff - network tab
