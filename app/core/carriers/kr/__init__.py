from app.util.ext.Performance import Performance
from app.util.GenTemplit import GenTemplit
from .CjLogistics import CjLogistics
from app.util.TimeStamp import TimeStamp
import ujson


class CjLogisticsProcessor:
    """CJ Logistics | CJ 대한통운
    """
    def __init__(self):
        self.loop = Performance()
        self.timestamp = TimeStamp()

    async def CjConverter(self, track_id):
        a = CjLogistics()
        sourc = await a.GetCsrfCode(track_id=track_id)
        source = ujson.loads(ujson.dumps(sourc))
        ParcelDetailResultMap = source['parcelDetailResultMap']
        ResultList = ParcelDetailResultMap['resultList']


        Source = GenTemplit()
        CurrentLength = Source.state(arrayData=ResultList)
        global d

        for CurrentData in ResultList:
            CurrentState = CurrentData['scanNm']
            CurrentDescription = CurrentData['crgNm']
            CurrentLocation = CurrentData['regBranNm']
            LastCheckPointTime = CurrentData['dTime']
            timestamp = await self.timestamp.stamp()
            d = [CurrentState, CurrentDescription,CurrentLocation, LastCheckPointTime, timestamp]
        One = await Source.generate(
            From="배송 업체에서 정보를 제공하지 않습니다.",
            To="배송 업체에서 정보를 제공하지 않습니다.",
            State=d[0],
            Description=d[1],
            Location=d[2],
            LastCheckPointTime=d[3],
            timestamp=d[4]
        )
        return One