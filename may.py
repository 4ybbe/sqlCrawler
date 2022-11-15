import time
import requests
import sys

from bs4 import BeautifulSoup

dork = input("Dork: ")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

nav = webdriver.Chrome(ChromeDriverManager().install())



nav.get("https://google.com.br")
nav.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(dork)
nav.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(Keys.RETURN)



xD = 2


vuln = open("vuln.txt", 'a+')



def bye(sub):
    num = "0123456789"
    for num in num:
        sub = sub.replace(num, '')
    sub = sub + "'"
    return sub

xD = 2

while True:
    urlnative = nav.current_url
    reqs = requests.get(urlnative)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    try:
        for link in soup.find_all('a'):
            try:
                data = link.get('href')
                if data[0] == "/" and data[1] == "u":
                    try:
                        nav.get("https://google.com" + data)

                        urldone = nav.current_url
                        urlshow = urldone
                        urldone = bye(urldone)

                        nav.get(urldone)
                        found = nav.page_source
                        if "Mysql" in found or "SQL" in found:
                            vuln.write(urlshow)
                            vuln.write('\n')
                            vuln.close()
                            vuln = open("vuln.txt", 'a+')
                    except:
                        pass
                check = nav.page_source
                if "captcha-form" in check:
                    time.sleep(30)
                    link.next()    #nao funciona
                else:
                    pass
            except:
                pass
        nav.get(urlnative) 



        xD = xD + 1
        nav.find_element_by_xpath('//*[@id="botstuff"]/div/div[2]/table/tbody/tr/td['+str(xD)+']/a').click()
        urlnative = nav.current_url
    except:
        vuln.close()



