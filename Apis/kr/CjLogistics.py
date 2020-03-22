from scrapy import Selector
from app.util import headers, ReHeaders
from app.util import power
import aiohttp
import ujson


class CjLogistics:
    def __init__(self):
        self.loop = power
        self.GetCsrf = 'https://www.cjlogistics.com/ko/tool/parcel/tracking'
        self.ApiUrl = 'https://www.cjlogistics.com/ko/tool/parcel/tracking-detail'
        self.CsrfCss = f'#frmTrackingSearch > input[type=hidden]:nth-child(3)'
        self.headers = headers
        self.ReHeaders = ReHeaders

    async def GetCsrfCode(self, track_id):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(self.GetCsrf) as resp:
                html = await resp.text()

            soup = await self.loop.run_in_threadpool(lambda: Selector(text=html))
            base = await self.loop.run_in_threadpool(lambda: soup.css(self.CsrfCss))
            BaseResponse = await self.loop.run_in_threadpool(lambda: base.getall())
            a = BaseResponse[0][53:].replace('">', '')
            source = a
            params={
                '_csrf': source,
                'paramInvcNo': track_id
            }
            async with session.post(self.ApiUrl, params=params) as resps:
                res = await resps.json()
        return res