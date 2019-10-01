from selenium import webdriver
import time

print("Hello\nWelcome to he4rtmach1ne.\nIt provides you to like tweets which are written by person you chose."
      "\nPlease click enter after you type.\nforceX Software v1.0")
usernameget = input("usern4me: ")
passwordget = input("passw0rd: ")
profileget = input("profi1e 1ink: ")

driver_path = r"C:\Users\Murat\Downloads\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1200x600')  # optional
browser = webdriver.Chrome(executable_path=driver_path, options=options)

browser.get("https://twitter.com/login")
username = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input")
password = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input")
username.send_keys(usernameget)
time.sleep(2)
password.send_keys(passwordget)
time.sleep(2)
login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login.click()

browser.get(profileget)
integer=1
while integer<550:
    browser.execute_script("window.scrollTo(10000000000000,10000000000300);")
    time.sleep(0.1)
    integer +=1
browser.execute_script("window.scrollTo(0,300);")
time.sleep(1)
hearts = browser.find_elements_by_class_name("HeartAnimation")
time.sleep(5)

saver = 0
for heart in hearts:
    heart.click()
    time.sleep(2)
    del hearts[0]
    time.sleep(2)
    saver += 1

print(saver," tweets were liked!")
