class GenTemplit:
    def __init__(self):
        self.apiTemplit = {
            'from': None,
            'to': None,
            'status': None,
            'description': None,
            'location': None,
            'time': None,
            'timestamp': None
        }

    def state(self, arrayData: list):
        length = len(arrayData)
        return length - length - 1

    @staticmethod
    async def LastCheckPoint(data: list, num: int):
        return data[num]

    async def generate(self, From: str, To: str, State: str, Description: str, Location: str, LastCheckPointTime: str, timestamp: str):
        """
        timestamp:
            Api 요청 시간
        origin:
            보내는 곳 또는 배송지
        destination:
            받는 곳
            최종 도착지 미 제공 택배사의 경우 null 반환
        state:
            현재 배송 상태
        description:
            현재 배송 추적 상세 정보
        location:
            베송 상품 현재 위치
        LastCheckPointTime:
            정보 갱신 시간
        """
        source = self.apiTemplit
        source['from'] = From
        source['to'] = To
        source['status'] = State
        source['description'] = Description
        source['location'] = Location
        source['time'] = LastCheckPointTime
        source['timestamp'] = timestamp
        return source
