import discord
import pickledb
import copy

from discord.ext import commands

class Sounds:
    """A thing that saves and recalls sound scripts"""

    def __init__(self, bot):
        self.bot = bot
        self.db = pickledb.load('sounds.db', False)

    def save(self):
        return self.db.dump()

    def __unload(self):
        pass

    @commands.group(pass_context=True, aliases=('sb',))
    async def soundbank(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say('Invalid command for soundbank')

    @soundbank.command()
    async def save(self, name : str, url : str):
        self.db.set(name, url)
        await self.bot.say('Saved {}'.format(name))

    @soundbank.command()
    async def get(self, name : str):
        url = self.db.get(name)
        await self.bot.say('Got {}, url: {}'.format(name, url))

    @soundbank.command(pass_context=True)
    async def play(self, ctx, name : str):
        url = self.db.get(name)
        msg = copy.copy(ctx.message)
        msg.content = '?play {}'.format(url)
        await self.bot.process_commands(msg)

    @commands.command()
    async def savesb(self):
        saved = self.db.dump()
        if saved:
            await self.bot.say('Database saved')

def setup(bot):
    bot.add_cog(Sounds(bot))
