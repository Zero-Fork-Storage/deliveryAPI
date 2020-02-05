import lxml
from bs4 import BeautifulSoup

class Templit:
    def __init__(self, arraydata: list):
        self.arraydata = arraydata
        self.apiTemplit = {
            'timestemp': None,
            'from': None,
            'to': None,
            'DeliveryStatus': None,
            'description': None,
            'location': None,
            'time': None,
            'trace': None
        }

    def state(self):
        length = len(self.arraydata)
        return length - length - 1

            
    
    def lastCheckPoint(self, data: list, num: int):
        return data[num]

    def generate(self, timestemp: str, origin: str, destination: str, currenntstate: str, currenntdescription: str, currenntlocation: str, lastcheckpointtime: str, trace: list):
        """
        timestemp:
            Api 요청 시간
        origin:
            보내는 곳 또는 배송지
        destination:
            받는 곳
            최종 도착지 미 제공 택배사의 경우 null 반환
        currenntstate: 
            현재 배송 상태
        currenntdescription:
            현재 배송 추적 상세 정보
        currenntlocation:
            베송 상품 현재 위치
        lastcheckpointtime:
            정보 갱신 시간
        """
        complete_templit = self.apiTemplit
        complete_templit['timestemp'] = timestemp
        complete_templit['from'] = origin
        complete_templit['to'] = destination
        complete_templit['DeliveryStatus'] = currenntstate
        complete_templit['description'] = currenntdescription
        complete_templit['location'] = currenntlocation
        complete_templit['time'] = lastcheckpointtime
        complete_templit['trace'] = trace
        return complete_templit

class Crawler(BeautifulSoup):
    def __init__(self, content):
        self.DATA = content

    def soup(self):
        _soup = BeautifulSoup(self.DATA, 'lxml')
        return _soup