from selenium import webdriver
import time

driver_path = r"C:\Users\Murat\Downloads\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')  # optional
browser = webdriver.Chrome(executable_path=driver_path, options=options)

#
feedback = input("Çevirmek istediğiniz kelime/cümle; \nTürkçe ise T, \nİngilizce ise İ \nyazıp emter tuşuna basınız: ")

if feedback == "T":
    browser.get("https://translate.google.com/#view=home&op=translate&sl=tr&tl=en")
    time.sleep(2)
    get = input("Çevirmek istediğiniz Türkçe ifadeyi yazınız: ")
    space = browser.find_element_by_xpath("//*[@id='source']")
    space.send_keys(get)
    time.sleep(2)
    translation = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/span")
    print("----->", translation.text, "<----- \nSoftw4re 0.1")

if feedback == "İ":
    browser.get("https://translate.google.com/#view=home&op=translate&sl=en&tl=tr")
    time.sleep(2)
    get = input("Çevirmek istediğiniz İngilizce ifadeyi yazınız: ")
    space = browser.find_element_by_xpath("//*[@id='source']")
    space.send_keys(get)
    time.sleep(2)
    translation = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div/span[1]/span")
    print(translation.text)






