from datetime import datetime, timedelta
import src.utility.Global as Global

class EmbedPageManager:

    def __init__(self, pages, channel):
        self.pages = pages
        self.channel = channel

        self.page = 0
        self.start = datetime.now()
        self.message = None

        Global.pages.append(self)

    async def check_timer(self):
        if datetime.now() - self.start > timedelta(minutes=3):
            await self.message.delete()
            Global.pages.remove(self)

    async def createPages(self):
        pass
