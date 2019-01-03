# Original Website Structure: mima.co.il

## Pages
* Home page: https://www.mima.co.il/
* Add fact page: https://www.mima.co.il/add_fact.php
* Artist page: https://www.mima.co.il/artist_page.php?artist_id=258
* Song Letter page: https://www.mima.co.il/song_letter.php?let=ד
* Questions Archive page: https://www.mima.co.il/questions_archive.php

## Entities and Relationships

### Artist
* artist_letter (str)
* artist_id (int)


### Song
* song_letter (str)
* song_id (int)
* artist_id (int)

### fact
* fact_id (int)
* song_id (int)
* fact_letter (str)

## code crawler 

import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import html5lib
diname = {}
listsong = []
disong = {}
saa = "אבגדהוזחטיכלמנסעפצקרשת"
path = "phantomjs"
driver = webdriver.PhantomJS(executable_path=path)
for x in saa:
    url = f"https://www.mima.co.il/artist_letter.php?let={x}"
    content = requests.get(url).content
    soup = BeautifulSoup(content,"html5lib")
    for link in soup.find_all('a'):
        if "artist_id" in link.get('href'):
            print(link.get_text().strip())
            url1 = f"https://www.mima.co.il/{link.get('href')}"
            content1 = requests.get(url1).content
            soup1 = BeautifulSoup(content1,"html5lib")
            for links in soup1.find_all('a'):
                if "song_id" in links.get('href'):
                    print("          ", links.get_text().strip())



                    listsong.append(links.get_text().strip())


                    url11 = f"https://www.mima.co.il/{links.get('href')}"

                    driver.get(url11)
                    soup11 = BeautifulSoup(driver.page_source)

                    for i,linkss in enumerate(soup11.find_all('td')):

                        if i == 57:
                           print(linkss.get_text().strip())
                           disong[links.get_text().strip()] = linkss.get_text().strip()
            diname[link.get_text().strip()] = listsong
            listsong = []


pickle.dump( diname, open( "diname.p", "wb" ) ) #save into file pikle
pickle.dump( disong, open( "disong.p", "wb" ) )






