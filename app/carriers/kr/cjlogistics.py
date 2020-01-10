import requests
import json
import sys
from bs4 import BeautifulSoup
import lxml

class CJ_logistics_KR:
    def __init__(self):
        """
        ```
        CJ 대한통훈 | CJ logistics 배송 조회 모듈
        **난 몰라 RST 마크업 안지킬 꺼임**

        track_id:
            CJ 대한통훈 운송장 코드
        
        status
            :information_received => 상품준비중
            :at_pickup => 상품인수
            :in_transit => 상품이동중
            :in_transit => 상품이동중 // 배송지 도착이지만 제공하지 않음
            :in_transit => 상품이동중
            :out_for_delivery => 배송출발
            :delivered => 배달완료
        ```

        """
        # 브라우저 인증을 위해 User-Agent 값을 Headers에 입력한다
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        }
        
        # API 클라이언트 검증 우회를 위한 쿠키를 얻기 위한 URL
        self.cookies_get = 'https://www.cjlogistics.com/ko/tool/parcel/tracking'
        
        # CJ 대한통훈 배송 조회 API URL
        self.api_url = 'https://www.cjlogistics.com/ko/tool/parcel/tracking-detail'
        
        # API JSON 템플릿
        self.shippingInfo_templit = {
            'timestemp': None,
            'from': None,
            'to': None,
            'DeliveryStatus': None,
            'description': None,
            'location': None,
            'date': None,
            'time': None
        }


    # def get_cookies(self):
    #    """CJ 대한통훈 배송조회 페이지에서 쿠키를 얻는다"""
    #    cookies = requests.get(
    #        url=self.cookies_get,
    #        headers=self.headers
    #    ).cookies
    #    # 디버깅 목적으로 쿠키를 출력한다
    #    print(str(cookies))
    #
    #    # cookies 값을 반환한다
    #    return cookies

    
    def query(self, track_id):
        """
        ## 배송조회 API Call
            def query(self, track_id):
            
            track_id는 운송장 코드를 의미 합니다.
            
            cjlogistics = CJ_logistics_KR()
            query_data = cjlogistics.query(track_id)
            print(str(query_data))
            return query_data
            
            **Response 값은 json 이다**        
        """
        # cjlogistics = CJ_logistics_KR()
        # cookies = cjlogistics.cookies_get()

        # CSRF : Cross-site request forgery
        # node.js ver > _csrf: $('input[name=_csrf]').val()
        # https://ko.wikipedia.org/wiki/사이트_간_요청_위조
        # https://stackoverflow.com/questions/13567507/passing-csrftoken-with-python-requests

        client = requests.session()
        _html = client.get(
            url=self.cookies_get,
            headers=self.headers
        ).content

        soup = BeautifulSoup(_html, 'lxml')
        base = soup.select('#frmTrackingSearch > input[type=hidden]:nth-child(3)')
        _csrf = base[0]['value']
        # print(str(_csrf))
        query_data = client.post(
            url=self.api_url,
            headers={
                'Referer': 'https://www.cjlogistics.com/ko/tool/parcel/tracking',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
            },
            params={
                '_csrf': _csrf,
                'paramInvcNo': track_id
            }
        ).json()
        return query_data

cjlogistics = CJ_logistics_KR()
#print(str(cjlogistics.query(track_id="626035220295")))