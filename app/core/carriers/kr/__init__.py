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
        self.source = CjLogistics()

    async def CjConverter(self, track_id):
        csrf = await self.source.GetCsrfCode(track_id=track_id)
        source = ujson.loads(ujson.dumps(csrf))
        ParcelDetailResultMap = source['parcelDetailResultMap']
        ResultList = ParcelDetailResultMap['resultList']

        Source = GenTemplit()
        # CurrentLength = Source.state(arrayData=ResultList)

        list_data = []
        so = list_data.append

        for CurrentData in ResultList:
            CurrentState = CurrentData['scanNm']
            CurrentDescription = CurrentData['crgNm']
            CurrentLocation = CurrentData['regBranNm']
            LastCheckPointTime = CurrentData['dTime']
            timestamp = await self.timestamp.stamp()
            d = [CurrentState, CurrentDescription,CurrentLocation, LastCheckPointTime, timestamp]
            so(d)

        One = await Source.generate(
            State=list_data[0][0],
            Description=list_data[0][1],
            Location=list_data[0][2],
            LastCheckPointTime=list_data[0][3],
            timestamp=list_data[0][4]
        )
        return One