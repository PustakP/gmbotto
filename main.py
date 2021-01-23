import discord
import random
from discord.ext import commands, tasks

import os
from flask import Flask 
from threading import Thread

from discord.ext.commands import CommandNotFound

app = Flask('discord bot')

@app.route('/')
def hello_world():
    return 'yes server working lmao'

def start_server():
  app.run(host='0.0.0.0',port=8080)
  
t = Thread(target=start_server)
t.start()


#idek why this is here
#class MyClient(discord.Client):
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#
#        self.bg_task = self.loop.create_task(self.my_background_task())
#    async def on_ready(self):
#
#      print('Bot is ready.')
#
#    async def my_background_task(self):
#        await self.wait_until_ready()
#        counter = 0
#        channel = self.get_channel(802203181588938813) 
#        
#        while not self.is_closed():
#            counter += 1
#            await channel.send(random.choice(b))
#            await asyncio.sleep(5) # task runs every 60 seconds


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [
    'https://cdn.discordapp.com/attachments/802203181588938813/802206630195363851/hey-you-good-morning-meme.png',
    'https://cdn.discordapp.com/attachments/802203181588938813/802206638953463808/a-little-push-good-morning-meme.png',
    'https://cdn.discordapp.com/attachments/802203181588938813/802206656527859722/ef2c2846824d86d97b96981291d45ddb--goodnight-texts-good-morning-texts.png',
    'https://cdn.discordapp.com/attachments/802203181588938813/802206674705186846/Z.png',
    'https://cdn.discordapp.com/attachments/802203181588938813/802206698194075668/HISoP19YPqJGtHfTMGT-xWiIwL80gvPo__2oWO7ZYGo.png',
    'https://cdn.discordapp.com/attachments/802203181588938813/802206717253386260/BN-XC577_0122GO_SOC_20180122114320.png',
    'https://cdn.discordapp.com/attachments/796777986392981574/802020734967873586/image0.jpg',
    'https://tenor.com/view/good-morning-tea-gif-8674682',
    'https://cdn.discordapp.com/attachments/796777986392981574/797722172734177280/images_36.jpeg',
    'https://cdn.discordapp.com/attachments/796777986392981574/797722008364253194/images_98.jpeg',
    'https://cdn.discordapp.com/attachments/796777986392981574/797722008602279977/images_97.jpeg',
    'https://tenor.com/view/%E0%B8%AD%E0%B8%A3%E0%B8%B8%E0%B8%93%E0%B8%AA%E0%B8%A7%E0%B8%B1%E0%B8%AA-%E0%B8%AA%E0%B8%A7%E0%B8%B1%E0%B8%AA%E0%B8%94%E0%B8%B5%E0%B8%95%E0%B8%AD%E0%B8%99%E0%B9%80%E0%B8%8A%E0%B9%89%E0%B8%B2-%D8%B5%D8%A8%D8%A7%D8%AD-%D8%A7%D9%84%D8%AE%D9%8A%D8%B1-good-morning-gif-15570120',
    'https://tenor.com/view/good-morning-sunrise-gif-8177317',
    'https://cdn.discordapp.com/attachments/796777986392981574/796971169487912980/IMG-20210108-WA0001.jpg',
    'https://tenor.com/view/good-morning-good-vibes-dancing-kid-girl-gif-16219018',
    'https://shayarifm.com/image-data/subah-hote-hi-good-morning-shayari-hindi.jpg',
    'https://cdn.discordapp.com/attachments/614421746900140035/802231820832997456/712621ff7d8719a882f45da12d3c947d.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802231823395586108/ek-naya-savera-ayaa-hai-suprabhat-status-and-shayari.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802231856342892604/x1080.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802231901980852314/30994-shayari-good-morning-images.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232014697922600/feba9b65f6956ca581f34ed183931ac0.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232079038808064/0fbf9212f2c356772d0071821b61b515.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232108630278164/maxresdefault.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232132512514088/best-cute-good-morning-images-pics_xlrg.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232173180223498/2Q.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232203387600896/Motivational-good-morning-pictures-1.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232234434232360/Cute-good-morning-Images-11.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232268356714536/95c70b1d890d9b6b0c4845766df23568.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232344936579122/d56df56cae159afedb8032e3a24ba6ef.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232381385211914/maxresdefault.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232471026270258/E0A4B6E0A581E0A4ADE0A4B8E0A58BE0A4AEE0A4B5E0A4BEE0A4B0_2233a4f1_1578882948134_cmprsd_40.png',
    'https://cdn.discordapp.com/attachments/614421746900140035/802232518015320094/22d8d2e801c0d849eb1ec2c33d8925de.png'
]

y = random.choice(x)
client = commands.Bot(command_prefix=['g','G'] , activity=discord.Activity(type=discord.ActivityType.watching, name="u say gm"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error



@tasks.loop(seconds=21600)
async def slow_count():
  channel = client.get_channel(int(796777986392981574))
  await channel.send(random.choice(b))



@client.event
async def on_ready():
  print('Bot is logged in as {0.user}'.format(client))
  slow_count.start()





#await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="u say gm"))


#while true:
#  send(random.choice(b))
#  time.sleep(21600)

#@client.event

#    channel = client.get_channel('796777986392981574')
    
flex = 2

#while 2 == flex:
#  channel.send(random.choice(b))
#  time.sleep(21600)
    



@client.command()
async def m(ctx):
    await ctx.send('***Good Morning!***')
    await ctx.send(random.choice(b))


client.run(os.getenv('TOKEN'))

