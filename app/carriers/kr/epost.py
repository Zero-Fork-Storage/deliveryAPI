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
        'sid1': ''
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
def editList(l, n):
    for i in range(0, len(l)-5, n):
        yield l[i:i + n]

progressTable = soup.select('.table_col:nth-child(1)')[0]
# print(progressTable)
progressTableArray = []
for row3 in progressTable.find_all('td'):
    row4 = re.sub('<.+?>', '',str(row3)).strip()
    nospace2 = re.sub('&nbsp;| |\t|\r|', '',row4).replace('\n', ' ')
    nospace2 = re.sub('\([^)]*\)', '', nospace2)
    progressTableArray.append(nospace2)
progressTableArray = ' '.join(progressTableArray).strip().split()

progressTableResult = list(editList(progressTableArray, 4))
print(progressTableResult)

