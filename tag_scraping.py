#!/usr/bin/env python
# coding: utf-8

# Import libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

# Collect first page of title's list
link = 'https://www.detik.com/terpopuler/news?utm_source=detiknews&utm_medium=desktop'
request = requests.get(link)
content = request.content
soup = BeautifulSoup(content,"html.parser") 

isi = soup.find_all("span", {"class" : "nav__item"})
isi_text = ''

for title in isi:
    isi_text += title.get_text(strip=True) + '\n'

import datetime
  
filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
f = open(f"./tag/{filename}.txt", "x")
f.write(isi_text)
f.close()

#open and read the file after the appending:
f = open(f"./tag/{filename}.txt", "r")
print(f.read())




