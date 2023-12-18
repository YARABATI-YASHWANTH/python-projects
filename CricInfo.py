import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-cricket-world-cup-2023-24-15338"

r = requests.get(url)

#print(r.text)

soup = BeautifulSoup(r.text,'html.parser')

# print(soup.prettify())
tab = soup.find('table')
# print(tab.text)
runs = []
# print(tab.text)
for val in tab.find_all('strong'):
    runs.append(val.text)
    # print(val.text)
while runs.count('-')>0:
    runs.remove('-')
# print(runs)
runs=runs[1:]
runs= list(map(int,runs))
print(runs)


