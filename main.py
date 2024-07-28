import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='prefixo_do_bot', intents=intents)

@bot.event
async def on_ready():
    print(f'A aplicação {bot.user} está online!')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.CustomActivity(name="Opa!"))

@bot.command(aliases=['latency', 'ms', 'p'])
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.reply(f'Pong! `{latency}ms`')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user.mentioned_in(message):
        await message.channel.send(f'Fala,  {message.author.mention}! Como você está?')

    await bot.process_commands(message)

bot.run('token_do_bot')
