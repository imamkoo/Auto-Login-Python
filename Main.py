from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

username = "imam.ubaidillah@binus.ac.id" 
password = "AllahSWT."

driver = webdriver.Chrome("E:/@BINUS OL/PYTHON/chromedriver")

driver.get("https://ol.binus.ac.id/LoginBinusian")

# Click login Binus
driver.find_element("id","btnLoginSSO").click()

# Waiting to access input username
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable(('id', 'i0116')))
# If username field can click , input username
driver.find_element("id","i0116").send_keys(username)
# Click to access input password
driver.find_element("id","idSIButton9").click()

# Waiting to access input password
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable(('id', 'i0118')))
# If password field can click , input password
driver.find_element("id","i0118").send_keys(password)
# Click to access dashboard BINUS
driver.find_element("id","idSIButton9").click() 
# Stay signed in? NO
driver.find_element("id","idBtn_Back").click()

print ("LOGIN SUCCESS!")

action = ActionChains(driver)
wait = WebDriverWait(driver, 20)
element = wait.until(EC.element_to_be_clickable(('id', 'page')))
action.key_down(Keys.ESCAPE).key_up(Keys.ESCAPE).perform()

print("WELCOME TO DASHBOARD!")

driver.get("https://ol.binus.ac.id/Course/CourseList")
driver.find_element(By.ID,"MainContent_RptCourseList_LblCourseName_4").click()

print("WELCOME TO OOP!")

driver.find_element(By.ID,"MainContent_UCCourseSubMenu_rptSubMenu_lnkSubMenu_4").click()

print("OPENING ZOOM CLASS...")

driver.find_element(By.ID,"MainContent_rptVideoConference_lbAttend_2").click()