import discord
import aiohttp

from discord.ext import commands

class Images:
    """Get images from the internet"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self):
        """Gets a random image of a cat, usually cute"""
        async with aiohttp.get('http://random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await self.bot.say(js['file'])

        return True


def setup(bot):
    bot.add_cog(Images(bot))
