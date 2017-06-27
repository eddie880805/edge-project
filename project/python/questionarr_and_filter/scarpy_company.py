from bs4 import BeautifulSoup
import urllib.request
import xlwt
import xlrd
import lxml
import re

url = "http://www2.morningstar.ca/tools/screener/ca/FundFinder.aspx?culture=en-CA"


sauce=urllib.request.urlopen(url).read()
soup=BeautifulSoup(sauce,'html.parser')
l=[]
for string in soup:
    l.append(str(string))

print(l)    

#post_buzz = div.findAll("div",{"class":"postbuzz"})

# for element in index_list:
#     worksheet.write(row, col, element)
#     col=col+1


# row=row+1


# workbook.save('text.xls')



