# Importing the required modules
from bs4 import BeautifulSoup
import requests
import time
import datetime
from datetime import date, timedelta
import csv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#set start date and end date for the scrape with added delay
START_DATE = date(2010, 1, 1)
END_DATE = date(2021, 5, 31)
RESTART_DELAY = 3
REQUEST_DELAY = 2

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def death_count(url):


    # Make a GET request to fetch the raw HTML content
    html_content = (url).text

    # Parse the html content
    soup = BeautifulSoup(html_content, "lxml")

    # length of a.linkgreen

    deaths = len(soup.select("a.linkgreen"))
    print(deaths)

    return deaths


def scrape_now(start_date, end_date):
    csvfile = open('./delhi.csv', 'a')
    csvwriter = csv.writer(csvfile)

    for current_running_date in daterange(start_date, end_date):
        current_running_date_str = current_running_date.strftime("%d/%m/%Y")

        print("Running for {current_running_date_str}".format(
                current_running_date_str=current_running_date_str
            )
        )
        #North delhi male

        #url_m=requests.get(f"https://111.93.47.72/csbndmc/rbd/onlinedeathcertificates.php?searchoption_f=2&format=MCDOLIR&dod_f={current_running_date_str}&sex_f=M&dcname_f=&trmchk=1&submit=submit", verify=False)

        #North delhi female

        #url_f=requests.get(f"https://111.93.47.72/csbndmc/rbd/onlinedeathcertificates.php?searchoption_f=2&format=MCDOLIR&dod_f={current_running_date_str}&sex_f=F&dcname_f=&trmchk=1&submit=submit", verify=False)

        #south delhi male

        #url_m=requests.get(f"https://111.93.47.72/csbsdmc/rbd/onlinedeathcertificates.php?searchoption_f=2&format=MCDOLIR&dod_f={current_running_date_str}&sex_f=M&dcname_f=&trmchk=1&submit=submit", verify=False)

        #south delhi female

        #url_f=requests.get(f"https://111.93.47.72/csbsdmc/rbd/onlinedeathcertificates.php?searchoption_f=2&format=MCDOLIR&dod_f={current_running_date_str}&sex_f=F&dcname_f=&trmchk=1&submit=submit", verify=False)


        #east delhi male

        url_m=requests.get(f"https://111.93.47.72/csbedmc/rbd/onlinedeathcertificates.php?searchoption_f=2&format=MCDOLIR&dod_f={current_running_date_str}&sex_f=M&dcname_f=&trmchk=1&submit=submit", verify=False)

        #east delhi female

        url_f=requests.get(f"https://111.93.47.72/csbedmc/rbd/onlinedeathcertificates.php?searchoption_f=2&format=MCDOLIR&dod_f={current_running_date_str}&sex_f=F&dcname_f=&trmchk=1&submit=submit", verify=False)



         #write output to csv file
        csvwriter.writerow([current_running_date_str, death_count(url_m), death_count(url_f)])

    csvfile.close()

if __name__ == "__main__":
    print("start_date {} and end_date {}".format(START_DATE, END_DATE))
    scrape_now(START_DATE, END_DATE)
