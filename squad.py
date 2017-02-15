import discord
import aiohttp

from discord.ext import commands

DESC = '''A discord bot made specially for the everest discord featuring such
spicy memes as the testing noise, and others.

Made by alex
'''

if not discord.opus.is_loaded():
    discord.opus.load_opus('opus')

bot = commands.Bot(command_prefix='::', description=DESC)
state = {'voice': None}

@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

    await bot.change_presence(game=discord.Game(name='TIOS, lets pass those CAs'))

@bot.command(pass_context=True)
async def test(ctx):
    counter = 0
    tmp = await bot.say('Calculating messages...')
    async for log in bot.logs_from(ctx.message.channel, limit=1000):
        if log.author == ctx.message.author:
            counter += 1
    await bot.edit_message(tmp, 'You have contributed {} messages to {} in the last 1000 messages.'.format(counter, ctx.message.channel.mention))

    return True

@bot.command()
async def cat():
    async with aiohttp.get('http://random.cat/meow') as r:
        if r.status == 200:
            js = await r.json()
            await bot.say(js['file'])

    return True

@bot.command(pass_context=True)
async def summon(ctx):
    summoned_channel = ctx.message.author.voice_channel
    if summoned_channel is None:
        await bot.say('You ain\'t in a voice channel bitch')
        return False

    if state['voice'] is None:
        state['voice'] = await bot.join_voice_channel(summoned_channel)
        await bot.say('Joining {}'.format(summoned_channel))
    else:
        await state['voice'].move_to(summoned_channel)
        await bot.say('Moving to {}'.format(summoned_channel))

    return True

@bot.command()
async def leave():
    await bot.say('Leaving {}'.format(state['voice'].channel.name))
    await state['voice'].disconnect()

    return True

@bot.command(pass_context=True)
async def play(ctx, url):
    voice = state['voice']
    player = await voice.create_ytdl_player(url)
    state['player'] = player

    await bot.say('Playing {} as requested by {}'.format(url, ctx.message.author.name))
    player.start()

    return True

bot.run('MjgwOTcyODUyMTg5MjAwMzg1.C4WgUA.aQkJfNpfKTc2duIny3Dt9dWIQPA')
