# importing the modules
import time
import requests
import os
from bs4 import BeautifulSoup
  
# target url
url = 'https://www.espncricinfo.com/series/new-zealand-in-india-2021-22-1278658/india-vs-new-zealand-1st-test-1278674/live-cricket-score/'
  
# making requests instance
reqs = requests.get(url)
  
# using the BeaitifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')
  
# displaying the title
while True:
  os.system('clear')
  for title in soup.find_all('title'):
      print(title.get_text())
  time.sleep(60)
