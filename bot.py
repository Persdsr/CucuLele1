import disnake
from disnake.ext import commands
import os

bot = commands.Bot(command_prefix='!', intents=disnake.Intents.all())
bot.remove_command('help')
bot.remove_command('stop')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('MTA1NTkyMzI5MTYyNzQ3NTA1NA.GFB4lt.EDxfo3NR4_ZR-J-jsYtEnjKUn0u3A8tOIvjkQU')