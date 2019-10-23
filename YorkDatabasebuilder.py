import os
import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import \
    expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait


ff_options = webdriver.FirefoxOptions()
ff_options.binary = FirefoxBinary()
ff_options.binary_location = '/usr/bin/firefox'
ff_options.headless = False #true for no browser opening

ignore = {"Type", "Day", "Start", "Time","Duration","Location", "Time","Cat #", "Instructor", "Notes/Additional Fees"}
setxpath = "/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr"
timeinfo = []
#yorkbaselink = "https://w2prod.sis.yorku.ca/"
newstr = ""
user = 'bilalb'
passw = 'choagrave0409'
termindex = 0
classtypes = ["BLEN", "CLIN", "CORS", "DISS", "DIRD", "FDEX", "FIEL", "IDS", "ISTY", "INSP", "LAB", "LECT ",
               "LGCL", "ONLN", "PERF", "PRAC", "REEV", "RESP", "REVP", "SEMR", "STDO", "TUTR", "THES", "WKSP"]
f = open("data.txt", "w")
currenttype = ''
writtentype = ""
dates = {'M':'Monday', 'T':'Tuesday', 'W':'Wednesday', 'R':'Thursday', 'F':'Friday', 'U':'Sunday', 'S':'Saturday', 'SU':'Saturday/Sunday',
          'MWF':'Monday/Wednesday/Friday', 'TR':'Tuesday/Thursday'}
class quick:
     def check(self):
          logbox = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td[2]/div/table')
          
          if('New Student?' in logbox.text):
               print("logging in")
               instance.login()
          
     def login(self):
          driver.execute_script("window.open('http://mms.yorku.ca')")
          #logbox = driver.find_element_by_xpath()
          WebDriverWait(driver, 15).until(ExpectedConditions.visibility_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td[2]/div/table')))
          driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1])
          WebDriverWait(driver, 10).until(ExpectedConditions.presence_of_element_located((By.XPATH,"//*[@id='mli']")))
          userbox = driver.find_element_by_xpath("//*[@id='mli']")
          userbox.send_keys(user)
          passbox = driver.find_element_by_xpath("//*[@id='password']")
          passbox.send_keys(passw)
          button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input")
          button.click()
          WebDriverWait(driver, 10).until(ExpectedConditions.title_is('Manage My Services'))
          driver.close()
          driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1])
     def subject(self):
          driver.get('https://w2prod.sis.yorku.ca/Apps/WebObjects/cdm')
          elem = driver.find_elements_by_xpath("//*[contains(text(), 'Subject')]")
          elem[0].click()
          ter = Select(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select"))
          ter.select_by_index(termindex)
     def courseinfo(self):
          WebDriverWait(driver, 10000).until(ExpectedConditions.visibility_of_element_located((By.XPATH,setxpath)))
          print("\n Course Title: ")
          elem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[1]/tbody/tr/td[1]/p/font")
          coursetitle = elem.text
          #print(coursetitle)
          coursetitles = coursetitle.split(" ")
          coursename = ' '.join(coursetitles[4:])
          coursecred = coursetitles[2]
          coursedepname = ' '.join(coursetitles[0:2])
          print(coursedepname + " - " + coursename + " - Credits: " + coursecred + "\n")
          f.write(coursedepname + " - " + coursename + " - Credits: " + coursecred + "\n")
          #f.write(elem.text + "\n")
          print("\n Course Description: ")
          elem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/p[3]")
          coursedesc = elem.text
          print(coursedesc)
          f.write("Course description: \n" + elem.text + "\n\n")
          print("\n")
          breaks = True 
          section = 0
          sectiontimes = 1
          while breaks:
               while True:
                    d = 0
                    try:
                         setnewxpath = setxpath + "[" + str(sectiontimes) + "]/td/table/tbody/tr[3]/td/table/tbody" #before td
                         elem = driver.find_element_by_xpath(setnewxpath) 
                    except:
                         breaks = False
                         break
                    termsec = driver.find_elements_by_xpath("//*[contains(text(), 'Section ')]")
                    if('Cancelled' in elem.text):
                         print(termsec[section].text + " - CANCELLED \n")
                         f.write(termsec[section].text + " - CANCELLED \n")
                         section+=2
                         sectiontimes+=1
                         break
                    timeinfo.clear()
                    instance.check()
                    print (termsec[section].text) #section stuff
                    #####"SEATS AVAILABLE:___" VS "SECTION/COURSE: ___", TERMSEC FINDS SECTION/COURSE, NEED TO FIX
                    f.write(termsec[section].text + "\n")
                    sectiontable = driver.find_element_by_xpath((setxpath + "[" + str(sectiontimes) + "]/td/table/tbody/tr[2]"))
                    if('Please click here to see availability' in sectiontable.text):
                         sectiontable.find_element_by_xpath("//*[contains(text(), 'Please click here to see availability')]").click()
                         #if('Username' in driver.find_element_by_xpath('/html/body').text):
                         '''if('Passport York Login' in driver.title):
                              userbox = driver.find_element_by_xpath("//*[@id='mli']")
                              userbox.send_keys(user)
                              passbox = driver.find_element_by_xpath("//*[@id='password']")
                              passbox.send_keys(passw)
                              button = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/form/div[2]/div[2]/p[2]/input")
                              button.click()'''
                         instance.check()
                         WebDriverWait(driver, 15).until(ExpectedConditions.visibility_of_element_located((By.XPATH, setnewxpath)))
                         sectiontable = driver.find_element_by_xpath((setxpath + "[" + str(sectiontimes) + "]/td/table/tbody/tr[2]"))
                    
                    out = (((sectiontable).text).split('\n'))
                    if(len(out) is 2):
                         print (out[0] + "\n" + out[1])
                         f.write(out[0] + "\n")
                         f.write(out[1] + " ")
                    else:
                         print(out[0])
                         f.write(out[0] + " ")
                    innertables = driver.find_element_by_xpath(setnewxpath).find_elements_by_css_selector('td')
                    currenttype = ''
                    for timestri in innertables:
                         timestr = timestri.text
                         #print(timestr)
                         if any(z in timestr for z in [" - Course Materials", "Expanded Course Description", "enrolment"]) or timestr in ignore:
                              None
                         else:
                              if any(types in timestr for types in classtypes):
                                   #timeinfo.append(timestr + ": ")
                                   currenttype = timestr #CMCT/DIGM
                                   writtentype = ''
                              elif ':' in timestr:
                                   
                                   times = timestr.split("\n")
                                   if ' 0:00' in timestr or ': 0' in timestr:
                                        if(writtentype is not currenttype):
                                             f.write("\n" + currenttype + " has no in-class meetings right now. ")
                                             writtentype = currenttype
                                   elif (any(notes in timestr.lower() for notes in ['enrol','course','info','meeting', 'hours']) \
                                             or (len(timestri.find_elements_by_css_selector('a')) > 0)) or len(timestr)>45 :
                                        if('\n' in timestr):
                                             timestr = timestr.replace('\n', '. ') 
                                        app = "Additional notes: " + timestr
                                        print(app)
                                        infolink = timestri.find_elements_by_css_selector('a')
                                        #infolink = timestri.get_attribute('href')
                                        if(len(infolink) > 0):
                                             #print(lin.get_attribute('href') for lin in infolink)
                                             for lin in infolink:
                                                  if(lin.get_attribute('href') not in timestr):
                                                       app = app + "- " + lin.get_attribute('href')
                                             timeinfo.append(app)
                                        else:
                                             timeinfo.append(app)
                                   elif len(timestr.split(" ")) > 2:
                                        #print(timestr.split(" "))
                                        #if "\n" in timestr:
                                        #timeinfo.append(timestr.split("\n"))
                                        listtimes = []
                                        #print(timestr.split("\n"))
                                        fin = currenttype
                                        check = 0
                                        checktim = timestr.split("\n")
                                        times = []
                                        if '(' in timestr:
                                             while check < (len(timestr.split("\n"))-1)/2:
                                                  times.append(checktim[check] + checktim[check+1])
                                                  #print(times)
                                                  check +=2
                                             check = 0
                                        else:
                                             times = timestr.split("\n")
                                        for t in times:
                                             n = 0
                                             tim = t.split(" ")
                                             if(('ISTY' or 'ONLN') in currenttype):
                                                  date = ''
                                                  starttime = ''
                                                  duration = ''
                                                  location = ''.join(tim[3:])
                                             else:
                                                  print(tim)
                                                  if(tim[n] in dates):
                                                       date = dates[tim[0]]
                                                      # n+=1
                                                  else:
                                                       date = '(No available date)'
                                                  print(date)
                                                  if(':' in tim[n] and len(tim[n]) > 2):
                                                       starttime = tim[1]
                                                     #  n+=1
                                                  else:
                                                       starttime = '(Unknown time)'
                                                  print(starttime)
                                                  if(tim[2] is '0' or tim[2] is ''):
                                                       duration ='(No available duration)'
                                                  else:
                                                       duration = "(" + str(int(tim[2])) + "min) - "
                                                 # n+=1
                                                  location = ' '.join(tim[3:])
                                             if (len(location) < 3):
                                                  location = '(room N/A)'
                                             if(date is ''):
                                                  pass
                                             else:
                                                  fin += date + " at " + starttime + duration + location
                                             if(check < len(times)-1):
                                                  fin = fin + ", "
                                             else:
                                                  fin = fin + ". "
                                             check+=1
                                             #date = currenttype + " is on: " + dates[tim[0]] + ", "
                                             #starttime = "Starts at: " + tim[1] + ", "
                                             #duration = "Length: " + tim[2] + " minutes, "
                                             #location = "In room: " + ' '.join(tim[3:]) + ". " #+ "-" + tim[5]
                                             #listtimes.append(date + starttime + duration + location)
                                             
                                             #print(date + "\n" + starttime + "\n" + duration + "\n" + location + "\n")
                                        #else:
                                        #     timeinfo.append(timestr+ " ")
                                        timeinfo.append(fin)
                              
                                   
                              elif len(timestr) == 6 and len(timestr.split(" ")) == 1: 
                                   timeinfo.append("Course Code: " + timestr + " ")
                                   """ if(round((timestri.size)['width'],1) != 147.6):
                                        None
                                   else:
                                         """
                              elif '(' in timestr and 'course' not in timestr and 'campus' not in timestr:
                                   code = timestr.split('\n')
                                   timeinfo.append("Course Code: ")
                                   codelen = 0
                                   #for codes in timestr.split('\n'):
                                   for codes in code:
                                        if(codelen < len(code)-1):
                                             timeinfo.append(codes + ", ")
                                        else:
                                             timeinfo.append(codes + ".")
                                        codelen+=1
                                   
                                   timeinfo.append('\n')
                              else:
                                   splitter = timestr.split(" ")
                                   if len(splitter) == 2: #len(timestri.get_attribute('innerHTML')) != 6:
                                        if 'ONLN' in currenttype or 'ISTY' in currenttype or timestr is " ":
                                             #timeinfo.append("Instructor: (No Listed Professor) ")
                                             None
                                        else:
                                             timeinfo.append("Instructor: " + timestr + " ")
                    st = coursedesc.find('Prereq')
                    en = coursedesc.find('Previously')
                    ent = coursedesc.find('Course credit')
                    if((ent != -1 and ent < en) or en == -1):
                         en = ent
                    if(coursedesc[st:en] is ''):
                         None
                    else:
                         timeinfo.append(coursedesc[st:en])
                    print("Info for this section: ")
                    print(timeinfo)
                    codefound = 1
                    instructorfound = 1
                    listcount = 0
                    for info in timeinfo:
                         if('Course' in info):
                              codefound = 1
                         if('Instructor' in info):
                              instructorfound = 1
                         #if('Prereq' in info):
                              #f.write('\n')
                         if type(info) is list:
                              f.write("[")
                              count = 0
                              for infopart in info:
                                   if("  " in infopart and infopart[-2:] is not '  '):
                                        infopart = infopart.replace("  ", "-")
                                   f.write(infopart)
                                   if(count != len(info)-1):
                                        f.write(", ")
                                   else:
                                        None
                                   count+=1
                              f.write("] ")
                         """ if
                              if(codefound == 0):
                                   f.write('Course Code: N/A ')
                              if(instructorfound == 0):
                                   f.write('Instructor: N/A ') """
                         if any(types in info for types in classtypes) or (listcount == (len(timeinfo)-1)):
                              if(codefound == 0):
                                   f.write('Course Code: N/A ')
                              if(instructorfound == 0):
                                   f.write('Instructor: N/A ')
                              f.write("\n")
                              codefound = 0
                              instructorfound = 0
                         if(type(info) is not list):
                              f.write(info)
                         listcount+=1
                    f.write("\n\n")
                    print("\n")
                    
                    #b+=1 
                    section+=2
                    sectiontimes+=1
          driver.close()

start = time.time()
instance = quick()
driver = webdriver.Firefox(executable_path ='geckodriver', options=ff_options)
waita = WebDriverWait(driver, 500)
#instance.login()
instance.subject()
actions = ActionChains(driver)

listterms = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select").find_elements_by_css_selector("option")
if (len(listterms) > 2):
     print(len(listterms))
     termindex = 1
while termindex <= len(listterms):
     print (termindex)
     listterms = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select").find_elements_by_css_selector("option")
     print(listterms[termindex].text)
     f.write(listterms[termindex].text + "\n\n")
     ter = Select(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select"))
     ter.select_by_index(termindex)
     listdep = len(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]").find_elements_by_css_selector("option"))
     value = 0
     #for dep in listdep:
     print(listdep)
     while value<listdep:
          print (value)
          sel = Select(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/select"))
          WebDriverWait(driver, 10000).until(ExpectedConditions.element_to_be_clickable((By.ID,'yib11banner')))
          sel.select_by_index(value)
          value+=1
          depurl = driver.current_url
          elem = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/input")
          elem.click()
          if("No courses" in driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td").text):
               #print(driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td").text + " has no courses")
               instance.subject()
               #ADD WAY TO PRINT COURSE NAME
               continue
          listcourse = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody").find_elements_by_css_selector("a")
          for course in listcourse:
               if("Course Description" not in course.text):
                    link = course.get_attribute("href")
                    print(link)
                    driver.execute_script(f"window.open('{link}')")
                    WebDriverWait(driver, 10000).until(ExpectedConditions.number_of_windows_to_be(2))
                    driver.switch_to.window(driver.window_handles[1])
                    instance.courseinfo()
                    driver.switch_to.window(driver.window_handles[0])
          instance.subject()
     termindex += 1
f.close()
driver.quit()
print(time.time() - start)