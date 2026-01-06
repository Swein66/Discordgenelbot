import discord
from discord.ext import commands

class TamYasakla(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="tamyasakla")
    @commands.has_permissions(administrator=True)
    async def tamyasakla(self, ctx, member: discord.Member = None, *, reason="Global yasaklama."):
        await ctx.message.delete()

        if member is None:
            return await ctx.send("⚠️ Yasaklanacak üyeyi belirt!", delete_after=5)

        # Swéin
        if member.top_role >= ctx.author.top_role and ctx.author.id != ctx.guild.owner_id:
            return await ctx.send(" Bu üye senden daha yüksek veya eşit bir role sahip!", delete_after=5)

        try:
            await member.ban(reason=reason)
            await ctx.send(f" **{member.name}** kullanıcısına tam yasaklama uygulandı.", delete_after=10)
        except Exception as e:
            await ctx.send(f" Hata: {e}", delete_after=5)

async def setup(bot):
    await bot.add_cog(TamYasakla(bot))