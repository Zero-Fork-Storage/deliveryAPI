import requests
import json
import re
import lxml
from bs4 import BeautifulSoup

"""
class EpostKr:
    def __init__(self):
        pass
"""

url = "https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm"
resp = requests.post(
    url=url,
    headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    },
    params={
        'sid1': '6066252805008'
    }
)

soup = BeautifulSoup(resp.content, 'lxml')
informationTable = soup.select('.table_col:nth-child(2)')[0]
array = []
for row in informationTable.find_all('td'):
    row2 = re.sub('<.+?>', '',str(row)).strip()
    nospace = re.sub('&nbsp;| |\t|\r|', '', row2).replace('\n', ' ')
    array.append(nospace)
array = ' '.join(array).split()
print(array)
    


progressTable = soup.select('.table_col:nth-child(1)')
#print(progressTable)
