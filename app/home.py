from flask import Flask
from flask_restful import Resource
from flask_restful import reqparse
from app.carriers.de.dhl import de_dhl
from app.carriers.kr.cjlogistics import cjlogistics
from app.carriers.ext.templit_source import Templit
from datetime import datetime


class DeliveryApiRouter(Resource):
    def __init__(self):
        """
        ```
        self.deliveryCompanyList: list
        ```
            ------------------------------
            |  code |     company
            ------------------------------
            |   0   |       DHL   
            ------------------------------
            |   1   |    CJ Logistics
            ------------------------------
            |   2   |      준비중
            ------------------------------
            |   3   |      준비중
            ------------------------------
            |   4   |      준비중
            ------------------------------
            |   5   |      준비중
            ------------------------------
            |   6   |      준비중
            ------------------------------
            |   7   |      준비중
            ------------------------------
            |   8   |      준비중
            ------------------------------

        """
        self.deliveryCompanyList: list = [
            "DHL", "CJ Logistics"
        ]
    
    def get(self):
        try:
            global parser
            now = datetime.now()
            nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
            parser = reqparse.RequestParser()
            parser.add_argument('code', type=int)
            parser.add_argument('track_id', type=str)
            args = parser.parse_args()
            _code: int = args['code']
            _track_id: str = args['track_id']
            if self.deliveryCompanyList[_code] == "DHL":
                print(_track_id)
                da = de_dhl().query(track_id=args['track_id'])
                results = da['results']
                state = results[0]
                checkpoints = state['checkpoints']
                dhlData = Templit(arraydata=checkpoints)
                last_checkpoint = checkpoints[0]
                return dhlData.generate(
                    timestemp=nowDatetime,
                    origin=state['origin']['value'],
                    destination=state['destination']['value'],
                    currenntstate=state['delivery']['status'],
                    currenntdescription=last_checkpoint['description'],
                    currenntlocation=last_checkpoint['location'],
                    lastcheckpointtime=last_checkpoint['time']
                )
            elif self.deliveryCompanyList[_code] == "CJ Logistics":
                print(_track_id)
                cjlogis = cjlogistics.query(track_id=_track_id)
                parcelDetailResultMap = cjlogis['parcelDetailResultMap']
                resultList = parcelDetailResultMap['resultList']
                cjData = Templit(arraydata=resultList)
                currentval = cjData.state()
                currentdata = resultList[currentval]
                currenntstate = currentdata['scanNm']
                currenntdescription = currentdata['crgNm']
                currenntlocation = currentdata['regBranNm']
                lastcheckpointtime = currentdata['dTime']
                return cjData.generate(
                    timestemp=nowDatetime,
                    origin="배송 업체에서 정보를 제공하지 않습니다.",
                    destination="배송 업체에서 정보를 제공하지 않습니다.",
                    currenntstate=currenntstate,
                    currenntdescription=currenntdescription,
                    currenntlocation=currenntlocation,
                    lastcheckpointtime=lastcheckpointtime
                )

        except Exception as e:
            return {'error': str(e)}
