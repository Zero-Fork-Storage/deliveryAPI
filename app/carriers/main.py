from datetime import datetime

from kr.cjlogistics import cjlogistics
from de.dhl import de_dhl
from ext.templit_source import Templit

class CarriersRouter:
    def __init__(self, track_id: str, company: any):
        self.track_id = track_id
        self.company = company
        self.co_list = [
            {
                "code": 1000,
                "name": "kr_cjlogistics"
            },
            {
                "code": 1001,
                "name": "dl_dhl"
            }
        ]
    def select(self):
        if self.company:
            source: dict = cjlogistics.query(track_id=self.track_id)
            resultList: list = source['parcelDetailResultMap']['resultList']

            onebone = Templit(resultList)
            
            stateNum: int = onebone.state()
            last: dict = onebone.lastCheckPoint(data=resultList, num=stateNum)
            """
            {
                "nsDlvNm": "", 
                "crgNm": "보내시는 고객님으로부터 상품을 인수받았습니다", 
                "crgSt": "11", 
                "dTime": "2019-10-18 17: 44: 49.0", 
                "empImgNm": "EMP_IMG_NM", 
                "regBranId": "1585", 
                "regBranNm": "경기동두천", 
                "scanNm": "집화처리"
            }
            """
            now = datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            stateTrackking: dict = onebone.generate(
                timestemp=str(nowDatetime),
                origin="배송업체에서 제공하지 않는 정보입니다",
                destination="배송업체에서 제공하지 않는 정보입니다",
                currenntstate=last['scanNm'],
                currenntdescription=last['crgNm'],
                currenntlocation=last['regBranNm'],
                lastcheckpointtime=last['dTime']
            )
            return stateTrackking