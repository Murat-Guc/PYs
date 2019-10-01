from selenium import webdriver
import time
driver_path = r"C:\Users\Murat\Downloads\chromedriver_win32\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument('window-size=1200x600')  # optional
browser = webdriver.Chrome(executable_path=driver_path, options=options)
browser.get("https://eksisozluk.com/basliklar/m/populer")

liste = []
liste2 = []
saver = 1
while saver < 20:
    titles_t = browser.find_element_by_xpath('//*[@id="mobile-index"]/ul/li[{}]'.format(saver))
    title = titles_t.text
    print("entry sayısı -->",saver,")",titles_t.text)
    liste.append(titles_t)
    liste2.append(title)
    saver+=1

order = input("seç:")
abc = int(order) - 1
time.sleep(2)
if abc < 6:
    liste[abc].click()
elif 5<abc<17:
    browser.execute_script("window.scrollTo(300,600);")
    liste[abc].click()
elif 16< abc < 20:
    browser.execute_script("window.scrollTo(600,900);")
    liste[abc].click()
time.sleep(12)

first = browser.find_element_by_xpath('//*[@id="entry-item-list"]/li[1]/div[1]').text
print(50*"-")
print("baslik:\n",liste2[abc])
print(50*"-")
print("ilk entry:\n",first)
print(50*"-")
sükela = browser.find_element_by_link_text("tümü").click()
best = browser.find_element_by_xpath('//*[@id="entry-item-list"]/li[1]/div[1]').text
print("şükela:\n",best)
