import requests
from bs4 import BeautifulSoup
tables = BeautifulSoup(requests.get('https://www.ibiblio.org/mutopia/piece-list.html').text).find_all('table',{'class':"simple_table"})
for table in tables:
    hrefs = table.find_all('a')
    for href in hrefs:
        internal_hrefs = BeautifulSoup(requests.get('https://www.ibiblio.org/mutopia/'+href['href']).text).find_all('a')
        for internal_href in internal_hrefs:
            if internal_href['href'].endswith('.mid'):
                mid_file = requests.get('https://www.ibiblio.org/mutopia/' + internal_href['href'].replace('../',''))
                with open(internal_href['href'].replace('../','').split('/')[-1], mode='wb') as jpg:
                    jpg.write(mid_file.content)
