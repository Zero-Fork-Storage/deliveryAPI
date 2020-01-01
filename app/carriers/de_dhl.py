import requests
import datetime
import json


class de_dhl:
    def __init__(self):
        self.api_url = 'https://www.logistics.dhl/shipmentTracking'
        self.at_pickup = ['at_pickup', '상품인수']
        self.delivered = ['delivered', '배송완료']
        self.STATUS_ID_MAP = {
            'picked up': {'id': 'at_pickup', 'text': '상품인수'},
            'delivered': {'id': 'delivered', 'text': '배송완료'}
        }
    def getTime(self, location, date, time):
        dateObj = datetime.



    def query(self, track_id):
        resp = requests.get(
            url=self.api_url,
            params={
                'AWB': track_id,
                'countryCode': 'g0',
                'languageCode': 'en'
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
            }
        )
        print(resp.status_code)
        if resp.status_code != 200:
            print("ERROR")
            return
        
        return resp
        
    def get(self, track_id):
        data = de_dhl().query(track_id).json()
        results = data['results']
        info = results[0]

        shippingInfo = {
            'from': {
                'name': info['origin']['value']
            },
            'to': {
                'name': info['destination']['value']
            },
            'state': { 'id': 'information_received', 'text':'접수완료' },
            'progresses': []
        }
        return shippingInfo

app = de_dhl()
print(app.get("7706689793"))

        
        
    
    
