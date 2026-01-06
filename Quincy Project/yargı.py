import discord
from discord.ext import commands

class YargiSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="yargı")
    @commands.has_permissions(ban_members=True)
    async def yargi(self, ctx, member: discord.Member = None, *, reason="KOVULDU."):
        # Swéin
        try:
            await ctx.message.delete()
        except:
            pass

        if member is None:
            return await ctx.send(" Yargılanacak birini etiketle!", delete_after=5)

        # Swéin
        if member.top_role >= ctx.author.top_role and ctx.author.id != ctx.guild.owner_id:
            return await ctx.send(" Senden üstte veya seninle aynı roldeki birini banlayamazsın!", delete_after=5)

        # Swéin
        member_name = str(member)
        member_id = member.id

        # Swéin
        try:
            # Swéin
            await member.ban(reason=reason)
            
            # Swéin
            embed = discord.Embed(
                title="KOVULDU",
                description=f" **{member_name}** (ID: {member_id}) sunucudan yasaklandı.\n**Sebep:** {reason}",
                color=0x000000
            )
            
            # Swéin
            image_url = "https://media.discordapp.net/attachments/1255558616422875147/1255558616422875147/ex.png" #Düzelt
            embed.set_image(url=image_url)
            
            await ctx.send(embed=embed)

        except discord.Forbidden:
            await ctx.send(" Botun yetkisi bu üyeyi yasaklamaya yetmiyor (Botun rolü üyenin altında olabilir).", delete_after=5)
        except Exception as e:
            # Swéin
            print(f"Yargı Hatası: {e}")
            await ctx.send(f" Bir hata oluştu: {e}", delete_after=5)

async def setup(bot):
    await bot.add_cog(YargiSistemi(bot))