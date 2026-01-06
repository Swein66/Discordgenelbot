import discord
from discord.ext import commands

class NukeKomutu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="nuke")
    @commands.has_permissions(manage_channels=True) # Swéin
    async def nuke(self, ctx):
        """Kanalı siler ve aynı ayarlarla tekrar oluşturarak mesajları temizler."""
        
        # Swéin
        position = ctx.channel.position
        new_channel = await ctx.channel.clone(reason="Nuke komutu kullanıldı.")
        
        # Swéin
        await ctx.channel.delete()
        
        # Swéin
        await new_channel.edit(position=position)
        
        # Swéin
        embed = discord.Embed(
            title="NUKE ATILDI",
            description=f"Bu kanal **{ctx.author.name}** tarafından temizlendi.",
            color=0xff0000
        )
        embed.set_image(url="istediğin foto link") #Düzelt
        
        await new_channel.send(embed=embed, delete_after=10)

async def setup(bot):
    await bot.add_cog(NukeKomutu(bot))