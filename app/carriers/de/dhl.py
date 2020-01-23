import requests
import datetime
import json


class de_dhl:
    def __init__(self):
        self.api_url = 'https://www.logistics.dhl/shipmentTracking'
        self.STATUS_ID_MAP = {
            'picked up': {'id': 'at_pickup', 'text': '상품인수'},
            'delivered': {'id': 'delivered', 'text': '배송완료'}
        }
        self.shippingInfo_templit = {
            'from': {
                "origin": None
            },
            'to': {
                'destination': None
            },
            'state': {
                'DeliveryStatus': None,
                'description': None,
                'location': None,
                'date': None,
                'time': None
            }
        }
                
    def query(self, track_id):
        resp = requests.get(
            url=self.api_url,
            params={
                'AWB': track_id,
                'countryCode': 'g0',
                'languageCode': 'ko'
            },
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
            }
        )

        #print(resp.status_code)
        if resp.status_code != 200:
            print("ERROR")
            return ("ERROR")
        data = resp.json()
        # print(data)
        return data

        
        
    
    
