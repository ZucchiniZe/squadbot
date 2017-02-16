import discord

from discord.ext import commands

class Misc:
    """Misc commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def msgcount(self, ctx):
        """Calculates the number of messages the caller has sent to the current channel"""
        counter = 0
        tmp = await self.bot.say('Calculating messages...')

        async for log in self.bot.logs_from(ctx.message.channel, limit=1000):
            if log.author == ctx.message.author:
                counter += 1

        await self.bot.edit_message(tmp, 'You have contributed {} messages to {} in the last 1000 messages.'.format(counter, ctx.message.channel.mention))

        return True

def setup(bot):
    bot.add_cog(Misc(bot))
