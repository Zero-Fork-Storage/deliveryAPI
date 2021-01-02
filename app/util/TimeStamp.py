from datetime import datetime
import time
import asyncio


class TimeStamp:
    def __init__(self):
        """timestamp"""
        self.loop = asyncio.get_event_loop()

    async def stamp(self):
        timestamp = await self.loop.run_in_executor(None, time.mktime, datetime.today().timetuple())
        return timestamp