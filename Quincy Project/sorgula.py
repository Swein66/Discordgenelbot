import discord
from discord.ext import commands
import requests
import datetime

class Sorgula(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.api_key = "YOUR_API_KEY" #Düzelt api icin dc den ulasabilirsin

    @commands.command(name="sorgula")
    async def user_sorgu(self, ctx, user: discord.User = None):
        
        if ctx.author.id != self.bot.owner_id and ctx.author.id != Kendi id in #Düzelt
            return await ctx.send(" **Komutu Sadece @kendinickin Kullanabilir**", delete_after=5) #Düzelt

        if user is None:
            return await ctx.send(" Lütfen sorgulanacak bir kullanıcı etiketleyin veya ID girin.", delete_after=5)

        await ctx.message.delete()
        bekle = await ctx.send(f" **{user.name}** veritabanında aranıyor...")

        url = f"https://app.findcord.com/api/user/{user.id}"
        headers = {"Authorization": self.api_key}

        try:
            response = requests.get(url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                await bekle.delete()

                embed = discord.Embed(
                    title="QUINCY SORGU SYSTEM",
                    color=0x2f3136,
                    timestamp=datetime.datetime.now()
                )

                findcord_notu = data.get('note', 'Sistemde kayıtlı notu yok.')
                
                embed.add_field(
                    name=" Kimlik",
                    value=f"```yaml\nİsim: {user.name}\nID: {user.id}```",
                    inline=False
                )

                embed.add_field(
                    name="Data Kaydı",
                    value=f"```fix\nNot: {findcord_notu}\nDurum: Sorgu Tamamlandı```",
                    inline=False
                )

                embed.set_thumbnail(url=user.display_avatar.url)
                embed.set_footer(text=f"Sorgulayan: {ctx.author.name}", icon_url=ctx.author.display_avatar.url)
                
                await ctx.send(embed=embed)

            else:
                await bekle.edit(content=f" **Hata:** Kullanıcı bulunamadı veya API hatası ({response.status_code})")

        except Exception as e:
            await bekle.edit(content=f" **Bağlantı Hatası:** Veriye erişilemiyor.")

async def setup(bot):
    await bot.add_cog(Sorgula(bot))