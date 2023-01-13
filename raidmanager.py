import discord

class RaidManager:
    
    def __init__(self):
        pass

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
