from datetime import datetime, timedelta
import src.utility.Global as Global

from discord import Embed

class EmbedPageManager:

    def __init__(self, pages, channel, user, colour=None, thumbnail=None):
        self.pages = pages
        self.channel = channel

        self.page = 0
        self.start = datetime.now()
        self.message = None

        self.user = user
        self.thumbnail = thumbnail
        self.colour = colour

        Global.pages.append(self)

    async def check_timer(self):
        if datetime.now() - self.start > timedelta(minutes=3):
            await self.message.delete()
            Global.pages.remove(self)

    async def updatePages(self):
        pass

    async def createPages(self):
        embed = Embed()

        if self.colour is not None:
            embed.colour = int(self.colour, 0)

        if self.thumbnail is not None:
            embed.set_thumbnail(url=self.thumbnail)

        title = ""
        text = ""
        index = 0
        for p in self.pages:
            if index == self.page:
                title = p
                for item in self.pages[p]:
                    text += f"- {item}"
            index += 1

        embed.add_field(name=title, value=text)

        self.message = await self.channel.send(embed)
