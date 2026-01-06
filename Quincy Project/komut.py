import discord
from discord.ext import commands
import datetime

class KomutRehberi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="komut")
    async def yardim(self, ctx):
        """Klasördeki tüm dosyalara göre hazırlanmış rehber."""
        await ctx.message.delete()

        embed = discord.Embed(
            title="QUINCY PANEL",
            description="Botun tüm sistemleri aktif durumdadır.",
            color=0x2b2d31,
            timestamp=datetime.datetime.now()
        )

        embed.add_field(
            name=" Güvenlik",
            value=(
                "`.yargı @üye` - yasaklama sistemini .\n"
                "`.tamyasakla @üye` - Tam yasaklama uygular.\n"
                "`.guard aç/kapat` - Sunucu koruma sistemini açar.\n"
                "`.sorgula @üye` - Owner Özel." 
                "`.log aç #kanal` - Log sistemini aktif eder.\n"
                "`.log kapat` - Log sistemini devre dışı bırakır.\n "
                "`.unyargı [kullanıcı ID]` - Belirtilen kullanıcının yasaklamasını kaldırır.\n"
                "`.snipe` - Son silinen mesajı gösterir.\n"
            ),
            inline=False
        )

        embed.add_field(
            name=" Müzik & Ses",
            value=(
                "`.play [şarkı]` - Müzik çalar (Bitince kanalda kalır).\n"
                "`.stop` - Müziği durdurur ve kanaldan çıkar.\n"
            ),
            inline=False
        )

        embed.add_field(
            name="Duyuru",
            value=(
                "`.embed [mesaj]` - Yazdığınız mesajı şık bir kutu içine alır.\n"
                "`.dmall [mesaj]` - Sunucudaki herkese özel mesaj gönderir."
            ),
            inline=False
        )

        embed.add_field(
            name="Yönetim",
            value=(
                "`.nuke` - Kanalı silip temiz bir şekilde tekrar açar.\n"
                "`.rol ver @üye @rol` - Üyeye rol tanımlar.\n"
                "`.rol al @üye @rol` - Üyeden rolü geri alır."
            ),
            inline=False
        )

        embed.set_thumbnail(url=self.bot.user.display_avatar.url)
        embed.set_footer(text="Quincy v3.1 | Tüm Modüller Hazır")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(KomutRehberi(bot))