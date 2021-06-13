# importing the libraries
from bs4 import BeautifulSoup
import requests
import pathlib
from datetime import datetime

url="http://117.232.67.141/birth_death_tn/DashDistDivVP.jsp?Yr=2021&Dist=CHENNAI&Div=CORPORATION"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "lxml")

#parse the content for table
BD_table = soup.find("table", attrs={"class": "bordered"})

#remove header and final row
for tdcol in BD_table.select('td[colspan="9"]'):
    tdcol.decompose()
hr_tag = soup.th
hr_tag.decompose()

filename = datetime.now().strftime("%Y-%m-%d")

#print(filename)

#print table
#print(BD_table)
# open the file in w mode
# set encoding to UTF-8
with open("daily-data/", filename +".html", "w", encoding = 'utf-8') as file:

    # prettify the soup object and convert it into a string
    file.write(str(BD_table))
