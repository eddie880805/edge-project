from bs4 import BeautifulSoup
import urllib.request
import xlwt
import xlrd
import lxml
import re

base_url = "http://quote.morningstar.ca/quicktakes/Fund/f_ca.aspx?t="


fund="F0CAN05MWM&region=CAN&culture=en-CA"




url = base_url + fund

sauce=urllib.request.urlopen(url)

soup=BeautifulSoup(sauce,'html.parser')

print(soup.find_all("div"))
