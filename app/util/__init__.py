from .TimeStamp import TimeStamp
from app.util.ext.Performance import Performance

timestamp = TimeStamp()
power = Performance()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}
ReHeaders = {
    "Content-Type": "application/json;charset=UTF-8",
    'Referer': 'https://www.cjlogistics.com/ko/tool/parcel/tracking',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}