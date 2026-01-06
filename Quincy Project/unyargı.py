import discord
from discord.ext import commands

class UnyargiSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unyargı", aliases=["unban"])
    @commands.has_permissions(ban_members=True)
    async def unyargi(self, ctx, user_id: int = None):
        """Belirtilen ID'ye sahip kullanıcının yasaklamasını kaldırır."""
        await ctx.message.delete()

        if user_id is None:
            return await ctx.send(" Lütfen yasaklaması kaldırılacak kişinin ID'sini girin. Örnek: `.unyargı 123456789`", delete_after=5)

        try:
            # Swéin
            user = await self.bot.fetch_user(user_id)
            await ctx.guild.unban(user)
            
            embed = discord.Embed(
                title=" YARGI KALDIRILDI",
                description=f" **{user.name}** (ID: {user_id}) kullanıcısının yasaklaması başarıyla kaldırıldı.",
                color=discord.Color.green()
            )
            # Swéin
            image_url = "https://media.discordapp.net/attachments/1255558616422875147/1255558616422875147/ex.png" #Düzelt
            embed.set_thumbnail(url=image_url) 
            
            await ctx.send(embed=embed, delete_after=10)
            
        except discord.NotFound:
            await ctx.send("❌ Bu kullanıcı yasaklılar listesinde bulunamadı.", delete_after=5)
        except Exception as e:
            await ctx.send(f"❌ Bir hata oluştu: {e}", delete_after=5)

async def setup(bot):
    await bot.add_cog(UnyargiSistemi(bot))