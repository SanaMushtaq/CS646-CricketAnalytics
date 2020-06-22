from bs4 import BeautifulSoup  # import beautifulsoup4
import requests
import csv
import re
import pandas as pd


from getCountryCode import *


class Scrape():

    def fetchData(self, country):
        countryCode = getCountryCode(country)

        urlPt1 = "http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;page="
        urlPt2 = ";spanmax1=03+Nov+2019;spanmin1=03+Nov+1999;spanval1=span;team="
        urlPt3 = ";template=results;type=team;view=results"

        response = requests.get(urlPt1 + '1' + urlPt2 + countryCode + urlPt3)

        content = BeautifulSoup(response.content, "html.parser")

        noOfPgs = int(re.search(r'\d+$', content.select('td.left')[5].text).group())

        file = open(country + '.csv', "a+")

        for i in range(1, noOfPgs + 1):
            response = requests.get(urlPt1 + str(i) + urlPt2 + countryCode + urlPt3)
            content = BeautifulSoup(response.content, "html.parser")
            for caption in content.find_all('caption'):
                if caption.get_text() == 'Match results':
                    table = caption.find_parent('table', {'class': 'engineTable'})
            # match_results= [['Team', 'Result', 'Margin', 'Toss', 'Bat', 'Opposition', 'Ground', 'Date']]
            match_results = []
            for tr in table.find_all('tr'):
                tds = tr.find_all('td')
                count = 0
                row = []
                for i in tds:
                    count += 1
                    if i.text:
                        if count == 4:
                            continue
                        row.append(i.text)
                match_results.append(row);
            match_results = [x for x in match_results if x]
            with open(country + '.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(match_results)
            csvfile.close()
        return pd.read_csv(file)
