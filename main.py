import os
import nextcord as nc
from nextcord.ext import commands
from dotenv import load_dotenv
load_dotenv()





bot = commands.Bot()
guild = bot.get_guild(int(os.environ.get("SERVER_ID")))

@bot.slash_command(description="Bannt einen Member!", default_member_permissions=4)
async def ban(inter: nc.Interaction, user: nc.User, reason: str):
    em = nc.Embed(title="Erfolgreich!", color=nc.Colour.green())
    em.add_field(
        name="Du hast den Nutzer erfolgreich gebannt. Er hat die UserID",
        value=user.id)
    em.add_field(name="Der User den du gebannt hast ist beigetreten",
                 value=f'am {user.mutual_guilds}')
    em.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/3677/3677016.png")
    await inter.send(embed=em)
    em2 = nc.Embed(
        title="Du wurdest in dem Gerichtssaal mit dem Hammer abgeworfen!",
        color=nc.Colour.red())
    em2.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/9894/9894719.png")
    em2.add_field(name="Der Grund warum du gebannt wurdest.",
                  value=f"{reason}")
    em2.add_field(name="Der Zeitraum", value="∞")
    await user.send(embed=em2)
    await user.ban()


@bot.slash_command(description="Kickt einen User", default_member_permissions=2)
async def kick(inter: nc.Interaction, user: nc.User, reason: str):
    em = nc.Embed(title="Erfolgreich!", color=nc.Colour.green())
    em.add_field(
        name="Du hast den Nutzer erfolgreich gekickt. Er hat die UserID",
        value=user.id)
    em.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/3677/3677016.png")
    await inter.send(embed=em)
    em2 = nc.Embed(
        title="Wir finden du brauchst eine Auszeit!",
        description=
        "Wenn du auf den Server erneut kommst, bist du auf bewährung!",
        color=nc.Colour.red())
    em2.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/9894/9894719.png")
    em2.add_field(name="Der Grund warum du gekickt wurdest.",
                  value=f"{reason}")
    em2.add_field(name="Der Zeitraum",
                  value="-- Es gibt bei einem Kick keinen Zeitraum --")
    await user.send(embed=em2)
    await user.kick()

@bot.slash_command(description="Whisper to an User!", default_member_permissions=8192)
async def whisper(inter: nc.Interaction, user: nc.User, message: str):
    em = nc.Embed(title="Ein Moderator/Supporter/Admin flüstert dir zu:",
                  description=message,
                  color=0x0e51b5)
    em.set_author(name=inter.user, icon_url=inter.user.avatar.url)
    em.set_thumbnail(
        url="https://cdn-icons-png.flaticon.com/512/4710/4710801.png")
    await user.send(embed=em)
    await inter.user.send(
        content=
        f"Deine Nachricht die du an {user.mention} geschrieben hast sieht so aus:",
        embed=em)


bot.run(str(os.environ.get("BOT_TOKEN")))
