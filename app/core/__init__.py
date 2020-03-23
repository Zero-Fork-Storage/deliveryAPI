from app.util.ext.Performance import Performance
from app.models.jsonModel import ResponseModel
from .carriers.kr import CjLogisticsProcessor
from .carriers.kr import CjLogisticsProcessor


class Routing:
    def __init__(self):
        self.loop = Performance()
        self.source = CjLogisticsProcessor()

    async def excute(self, track_id):
        a = CjLogisticsProcessor()
        v = await a.CjConverter(track_id=track_id)
        R = ResponseModel(**v)
        return v

"""
{
'from': R.From,
'to': R.To,
'status': R.DeliveryStatus,
'description': R.Description,
'location': R.Location,
'time': R.Time,
'timestamp': R.TimeStamp
}
        """