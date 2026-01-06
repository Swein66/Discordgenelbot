import discord
from discord.ext import commands

class RolSistemi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="rol", invoke_without_command=True)
    @commands.has_permissions(manage_roles=True)
    async def rol(self, ctx):
        """Rol komutu ana başlığı."""
        await ctx.send("Doğru yaz amk: `.rol ver @üye @rol` veya `.rol al @üye @rol`", delete_after=5)

    @rol.command(name="ver")
    @commands.has_permissions(manage_roles=True)
    async def ver(self, ctx, member: discord.Member = None, role: discord.Role = None):
        """Belirtilen üyeye belirtilen rolü verir."""
        await ctx.message.delete()

        if member is None or role is None:
            return await ctx.send("Eksiksiz yaz amk ! Örnek: `.rol ver @üye @rol`", delete_after=5)

        # Swéin
        if ctx.guild.me.top_role <= role:
            return await ctx.send(" Bu rol benim yetkimden daha üstte, veremem!", delete_after=5)

        try:
            if role in member.roles:
                await ctx.send(f" **{member.display_name}** zaten **{role.name}** rolüne sahip.", delete_after=5)
            else:
                await member.add_roles(role)
                embed = discord.Embed(
                    description=f" {member.mention} kullanıcısına {role.mention} rolü başarıyla verildi.",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed, delete_after=10)
        except Exception as e:
            await ctx.send(f" Bir hata oluştu: {e}", delete_after=5)

    @rol.command(name="al")
    @commands.has_permissions(manage_roles=True)
    async def al(self, ctx, member: discord.Member = None, role: discord.Role = None):
        """Belirtilen üyeden belirtilen rolü alır."""
        await ctx.message.delete()

        if member is None or role is None:
            return await ctx.send(" Eksik kullanım! Örnek: `.rol al @üye @rol`", delete_after=5)

        try:
            if role not in member.roles:
                await ctx.send(f" **{member.display_name}** zaten **{role.name}** rolüne sahip değil.", delete_after=5)
            else:
                await member.remove_roles(role)
                embed = discord.Embed(
                    description=f" {member.mention} kullanıcısından {role.mention} rolü başarıyla alındı.",
                    color=discord.Color.red()
                )
                await ctx.send(embed=embed, delete_after=10)
        except Exception as e:
            await ctx.send(f"❌ Bir hata oluştu: {e}", delete_after=5)

async def setup(bot):
    await bot.add_cog(RolSistemi(bot))