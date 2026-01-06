import discord
from discord.ext import commands

class MusicStop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="stop")
    async def stop(self, ctx):
        """Müziği durdurur ve bot kanaldan çıkar."""
        await ctx.message.delete()
        
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            
            embed = discord.Embed(
                description=" **Müzik durduruldu ve ses kanalından ayrılındı.**",
                color=0xe74c3c
            )
            await ctx.send(embed=embed, delete_after=5)
        else:
            await ctx.send(" Bot zaten bir ses kanalında değil.", delete_after=5)

async def setup(bot):
    await bot.add_cog(MusicStop(bot))