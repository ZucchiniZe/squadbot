import discord
import aiohttp

from discord.ext import commands

initial_extensions = [
    'cogs.music',
    'cogs.images',
    'cogs.misc',
    'cogs.admin',
    'cogs.repl'
]

description = '''A discord bot made specially for the everest discord featuring such
spicy memes as the testing noise, and others.

Made by alex
'''

prefixes = ['?', '!', '::']
bot = commands.Bot(command_prefix=prefixes, description=description)

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

    await bot.change_presence(game=discord.Game(name='TIOS, lets pass those CAs'))

@bot.event
async def on_resume():
    print('resumed...')

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.NoPrivateMessage):
        await bot.send_message(ctx.message.author, 'This command cannot be used in private messages.')
    elif isinstance(error, commands.DisabledCommand):
        await bot.send_message(ctx.message.author, 'Sorry. This command is disabled and cannot be used.')
    elif isinstance(error, commands.CommandInvokeError):
        print('In {0.command.qualified_name}:'.format(ctx), file=sys.stderr)
        traceback.print_tb(error.original.__traceback__)
        print('{0.__class__.__name__}: {0}'.format(error.original), file=sys.stderr)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))


    bot.run('MjgwOTcyODUyMTg5MjAwMzg1.C4WgUA.aQkJfNpfKTc2duIny3Dt9dWIQPA')
