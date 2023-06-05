import discord
from discord.ext import commands
from time import sleep
from discord.ext.commands import has_permissions
import json
import requests
import random
import asyncio
from bs4 import BeautifulSoup
import discord.reaction
import discord.emoji
import discord.role
from discord.utils import get
from asyncio import TimeoutError

#

intents = discord.Intents.all()
client = commands.Bot(command_prefix=".", intents=intents, case_insensitive=True)
client.remove_command("help")


@client.event
async def on_ready():
    activity = discord.Game(name='DIGITE ".help" PARA VER MEUS COMANDOS', type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("\n            BOT ONLINE!!\n")
    print(f" Nome Do Bot -> {client.user.name}")
    print(f" ID Do Bot -> {client.user.id}")
    print("----------Leonardo Alves----------")


@client.event
async def on_member_join(member):
    try:
        if int(member.guild.id) != int(1112833513482358794):
            return
        else:
            cidadao = member.guild.get_role(1112833841405644931)
            await member.add_roles(cidadao, reason="AutoRole")
    except Exception:
        pass
    
@client.listen()
async def on_message(message):
    if (
        f"<@{client.user.id}>" == message.content
        or f"<@!{client.user.id}>" == message.content
    ):
        eh = discord.Embed(
            title=' **Digite   ".help"   Para Ver Meus Comandos!**',
            colour=discord.Colour.from_rgb(0, 150, 150),
        )
        await message.channel.send(embed=eh)
        # await message.channel.send(f'Olá {message.author.mention}! Digite `.help` Para ver meus comandos!!!!')
    elif "🙉🙊🐒🐵🙈🙉🙊🐒" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} Querendo Travar Né? ")


@client.event
async def on_command_error(ctx, error):

    try:
        await ctx.message.delete()
    except Exception:
        pass

    guild = ctx.message.guild
    pensativo = client.get_emoji(763523696110469120)

    errorr = discord.Embed(
        title=f" {pensativo} _ERROR!_ {pensativo} ", colour=discord.Colour.dark_red()
    )

    if isinstance(error, discord.NotFound):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        return

    elif isinstance(error, commands.MissingPermissions):
        try:
            await ctx.message.delete()
        except Exception:
            pass

        error = str(error).lower()
        # print(f"perm: {error}")

        if "ban members" in error:
            permRequired = "Banir Membro(s)"
        elif "kick members" in error:
            permRequired = "Kickar Membro(s)"
        elif "manage roles" in error:
            permRequired = "Gerenciar Cargo(s)"
        elif "manage channels" in error:
            permRequired = "Gerenciar Canais"
        elif "manage messages" in error:
            permRequired = "Gerenciar Mensagens"
        elif "administrator" in error:
            permRequired = "Administrador"
        else:
            permRequired = error

        try:
            errorr.add_field(
                name="Houve Algum Erro:",
                value=f"Desculpe, Você Não Tem Permissão De {permRequired}",
                inline=False,
            )
            # errorr.set_footer(text=error, icon_url=f"{ctx.author.avatar}")
            errorr.set_footer(text=f"{ctx.author}  ->  {error}")
            err = await ctx.send(embed=errorr)
            await err.add_reaction("❌")

            def check1(reaction, user):
                return (
                    user == ctx.author
                    and str(reaction.emoji) in ["❌"]
                    and int(reaction.message.id) == int(err.id)
                )

            try:
                reaction, user = await client.wait_for(
                    "reaction_add", timeout=15.0, check=check1
                )
                if str(reaction.emoji) == "❌":
                    await err.delete()
                else:
                    pass
            except Exception:
                try:
                    await err.clear_reactions()
                except Exception:
                    pass
                pass
        except Exception:
            try:
                await err.clear_reactions()
            except Exception:
                pass
            pass
        return

    elif isinstance(error, commands.CommandNotFound):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        try:
            errorr.add_field(
                name="Houve Algum Erro:",
                value="Desculpe, Não Encontrei Nenhum Comando Com Esse Nome.",
                inline=False,
            )
            errorr.set_footer(text=error, icon_url=f"{ctx.author.avatar}")
            err = await ctx.send(embed=errorr)
            await err.add_reaction("❌")

            def check1(reaction, user):
                return (
                    user == ctx.author
                    and str(reaction.emoji) in ["❌"]
                    and int(reaction.message.id) == int(err.id)
                )

            try:
                reaction, user = await client.wait_for(
                    "reaction_add", timeout=15.0, check=check1
                )
                if str(reaction.emoji) == "❌":
                    await err.delete()
                else:
                    pass
            except Exception:
                try:
                    await err.clear_reactions()
                except Exception:
                    pass
                pass
        except Exception:
            try:
                await err.clear_reactions()
            except Exception:
                pass
            pass
        return

    elif isinstance(error, commands.BotMissingPermissions):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        try:
            errorr.add_field(
                name="Houve Algum Erro:",
                value="Desculpe, Eu Não tenho Permissão Para Executar esse Comando.",
                inline=False,
            )
            errorr.set_footer(text=error, icon_url=f"{ctx.author.avatar}")
            err = await ctx.send(embed=errorr)
            await err.add_reaction("❌")

            def check1(reaction, user):
                return (
                    user == ctx.author
                    and str(reaction.emoji) in ["❌"]
                    and int(reaction.message.id) == int(err.id)
                )

            try:
                reaction, user = await client.wait_for(
                    "reaction_add", timeout=15.0, check=check1
                )
                if str(reaction.emoji) == "❌":
                    await err.delete()
                else:
                    pass
            except Exception:
                try:
                    await err.clear_reactions()
                except Exception:
                    pass
                pass
        except Exception:
            try:
                await err.clear_reactions()
            except Exception:
                pass
            pass
        return

    elif isinstance(error, commands.MemberNotFound):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        try:
            errorr.add_field(
                name="Houve Algum Erro:",
                value="Desculpe, Usuàrio Não Encontrado.",
                inline=False,
            )
            errorr.set_footer(text=error, icon_url=f"{ctx.author.avatar}")
            err = await ctx.send(embed=errorr)
            await err.add_reaction("❌")

            def check1(reaction, user):
                return (
                    user == ctx.author
                    and str(reaction.emoji) in ["❌"]
                    and int(reaction.message.id) == int(err.id)
                )

            try:
                reaction, user = await client.wait_for(
                    "reaction_add", timeout=15.0, check=check1
                )
                if str(reaction.emoji) == "❌":
                    await err.delete()
                else:
                    pass
            except Exception:
                await err.clear_reactions()
                pass
        except Exception:
            await err.clear_reactions()
            pass
        return

    elif isinstance(error, commands.MissingRole):
        try:
            await ctx.message.delete()
        except Exception:
            pass
        try:
            errorr.add_field(
                name="Houve Algum Erro:",
                value="Desculpe, Você Não tem o Cargo Necessário Para Executar Esse Comando!",
                inline=False,
            )
            errorr.set_footer(text=error, icon_url=f"{ctx.author.avatar}")
            err = await ctx.send(embed=errorr)
            await err.add_reaction("❌")

            def check1(reaction, user):
                return (
                    user == ctx.author
                    and str(reaction.emoji) in ["❌"]
                    and int(reaction.message.id) == int(err.id)
                )

            try:
                reaction, user = await client.wait_for(
                    "reaction_add", timeout=15.0, check=check1
                )
                if str(reaction.emoji) == "❌":
                    await err.delete()
                else:
                    pass
            except Exception:
                await err.clear_reactions()
                pass
        except Exception:
            await err.clear_reactions()
            pass
        return

    else:
        pass

    try:
        errorr = discord.Embed(
            title=f" {pensativo} _ERROR!_ {pensativo} ",
            colour=discord.Colour.dark_red(),
        )
        errorr.add_field(name="Houve Algum Erro:", value=error, inline=False)
        err = await ctx.send(embed=errorr)
        await err.add_reaction("❌")
        try:
            reaction, user = await client.wait_for(
                "reaction_add", timeout=40.0, check=check1
            )
            if str(reaction.emoji) == "❌":
                await err.delete()
            else:
                pass
        except Exception:
            await err.clear_reactions()
            pass
    except Exception:
        await err.clear_reactions()
        pass


@client.event
async def on_guild_join(guild):
    entreiii = discord.Embed(
        title=f" :pushpin: NOVO SERVIDOR! :pushpin: ", colour=discord.Colour.dark_red()
    )
    entreiii.add_field(name="Nome:", value=f"{guild.name}", inline=False)
    entreiii.add_field(name="ID:", value=f"{guild.id}", inline=False)
    entreiii.add_field(name="Dono:", value=f"{guild.owner.mention}", inline=False)
    entreiii.add_field(name="Membros:", value=f"{guild.member_count}", inline=False)
    await client.get_user(637428569559269426).create_dm()
    await client.get_user(637428569559269426).dm_channel.send(embed=entreiii)

    try:
        g = client.get_guild(1112833513482358794)
        NewSv = g.get_channel(1112835495936938094)
        await NewSv.send(embed=entreiii)
    except Exception:
        pass


@client.event
async def on_guild_remove(guild):
    saiii = discord.Embed(
        title=f" :pushpin: SAIDA SERVIDOR! :pushpin: ", colour=discord.Colour.dark_red()
    )
    saiii.add_field(name="Nome:", value=f"{guild.name}", inline=False)
    saiii.add_field(name="ID:", value=f"{guild.id}", inline=False)
    saiii.add_field(name="Dono:", value=f"{guild.owner.mention}", inline=False)
    saiii.add_field(name="Membros:", value=f"{guild.member_count}", inline=False)
    await client.get_user(637428569559269426).create_dm()
    await client.get_user(637428569559269426).dm_channel.send(embed=saiii)


@client.command(aliases=["bi", "bot", "binfo"])
async def botinfo(ctx):
    try:
        await ctx.message.delete()
        # guilds = await client.fetch_guilds(limit=None).flatten()
        try:
            guilds = [guild async for guild in client.fetch_guilds(limit=None)]
            qntd = []
            for server in guilds:
                qntd.append(server)
                pass

            mf = client.get_emoji(763231027509461032)
            panda = client.get_emoji(763523935920324618)
            own = client.get_user(637428569559269426)
            bHelp = discord.Embed(
                title=f" {panda} **INFORMAÇÕES DO BOT** {panda} ",
                description="**[CONVITE](https://discord.com/api/oauth2/authorize?client_id=1112615109764849756&permissions=8&scope=bot)**",
                colour=discord.Colour.from_rgb(169, 110, 7),
            )
            bHelp.add_field(
                name="Criador:",
                value=f"{mf}{own.mention}",
                inline=False,
            )
            bHelp.add_field(
                name="Site:",
                value=f"{mf}**https://leonardo-alves.com**",
                inline=False,
            )
            bHelp.add_field(
                name="Linguagem:", value=f"{mf}`BOT Feito Em PYTHON!`", inline=False
            )
            bHelp.add_field(
                name="Quantidade De Servidores:",
                value=f"{mf}`{len(qntd)}`",
                inline=False,
            )
            bHelp.add_field(
                name="Quantidade De Usuàrios:",
                value=f"{mf}`{len(client.users)}`",
                inline=False,
            )
            bHelp.set_footer(
                text=f"Comando Solicitado Por: {ctx.author.name} | {ctx.author.id}\nPing: {round(client.latency * 1000)}ms",
                icon_url=f"{ctx.author.avatar}",
            )
            await ctx.send(embed=bHelp)
        except Exception as binfoError:
            print(f"BotInfo Erro:   {binfoError}")
    except discord.NotFound:
        pass
    except Exception:
        pass

@client.command(aliases=["p", "latency"])
async def ping(ctx):
    await ctx.message.delete()
    mine = client.get_emoji(763533912650678302)

    ePing = discord.Embed(
        title=f" {mine} **Ping** {mine} ", colour=discord.Colour.from_rgb(0, 100, 255)
    )
    ePing.add_field(
        name="Latencia:", value=f"**{round(client.latency * 1000)}ms**", inline=False
    )
    await ctx.send(embed=ePing)


@client.command(aliases=["motiva", "motivar", "motivacao", "motivação"])
async def motivacional(ctx):
    await ctx.message.delete()
    c = client.get_emoji(763231203691462676)
    frases = [
        "Não deixe para amanhã o que você pode fazer hoje.",
        "Motivação é a arte de fazer as pessoas fazerem o que você quer que elas façam porque elas o querem fazer.",
        "Não deixe um amor passado lhe corroer por dentro!",
        "Toda ação humana, quer se torne positiva ou negativa, precisa depender de motivação.",
        "Lute. Acredite. Conquiste. Perca. Deseje. Espere. Alcance. Invada. Caia. Seja tudo o quiser ser, mas acima de tudo, seja você sempre.",
        "No meio da dificuldade encontra-se a oportunidade.",
        "A verdadeira motivação vem de realização, desenvolvimento pessoal, satisfação no trabalho e reconhecimento.",
        "Pedras no caminho? Eu guardo todas. Um dia vou construir um castelo.",
        "Tudo o que um sonho precisa para ser realizado é alguém que acredite que ele possa ser realizado.",
        "O que me preocupa não é o grito dos maus. É o silêncio dos bons.",
        "Quando você quer alguma coisa, todo o universo conspira para que você realize o seu desejo.",
        "Você precisa fazer aquilo que pensa que não é capaz de fazer.",
        "O sucesso é ir de fracasso em fracasso sem perder entusiasmo.",
        "Lute com determinação, abrace a vida com paixão, perca com classe e vença com ousadia, porque o mundo pertence a quem se atreve e a vida é muito para ser insignificante.",
        "Nossa maior fraqueza está em desistir. O caminho mais certo de vencer é tentar mais uma vez.",
        "Eu acredito em você e na sua capacidade porque conheço o seu esforço e a sua motivação. Não desista! ",
        "Assim como os pássaros, precisamos aprender a superar os desafios que nos são apresentados, para alçarmos voos mais altos.",
        "Se ao enfrentar os problemas da vida lhe parecer que está escalando uma montanha impossível, lembre-se que a paisagem que avistará no topo compensará qualquer esforço seu.",
        "Alcançar o que se deseja dá trabalho, mas não pare de lutar porque está cansado; pare apenas quando tiver triunfado!",
        "Aquele que tentou e não conseguiu, é superior àquele que não tentou.",
        "Comece de novo se for necessário, mas jamais desista de lutar pelos seus sonhos!",
        "Não se desanime diante dos obstáculos, eles são sempre uma oportunidade de você sair mais forte de uma situação.",
        "Neste jogo da vida o maior vencedor é aquele que luta até ao fim.",
        "Se é difícil é porque vale a pena e um dia pode ser maravilhoso.",
        "Acredite nas suas capacidades e lute todos os dias para que elas sobressaiam no seu trabalho.",
        "Desistir é para os fracos ou para quem já não acredita mais no impossível!",
        "Fique tranquilo! Amanhã você vai achar um jeito de sorrir daquilo que hoje lhe fez chorar.",
        "Dispense qualquer fraqueza, entregue-se à coragem e corra atrás dos seus sonhos.",
        "Às vezes, uma pesada derrota é o ponto de partida ideal para nos renovarmos e partirmos em busca de grandes sucessos.",
        "Porque na vida não existem limites ou condições dê a volta por cima em todas as situações!",
        "Nunca deixe que nenhum limite tire de você a ambição da auto-superação.",
        "A força de vontade fica quietinha cochilando dentro de você, mas quando os seus sonhos começarem a falar mais alto, ela acorda.",
        "De tanto lutar para nunca se sentir perdido, um dia você acabará por encontrar o rumo certo.",
    ]
    frase = random.choice(frases)
    rst = discord.Embed(
        title=f" {c} **{frase}** {c} ", colour=discord.Colour.from_rgb(251, 56, 294)
    )
    await ctx.send(embed=rst)


# \u200b


@client.command(aliases=["k", "kickar", "chutar"])
@commands.has_permissions(kick_members=True)
async def kick(ctx, usuario: discord.Member, *, motivo="Não Inserido!"):
    channel = ctx.message.channel
    await ctx.message.delete()
    guild = ctx.message.guild
    sim = client.get_emoji(763523690985816115)
    nao = client.get_emoji(763523692696174593)

    kick = discord.Embed(
        title=" :warning: KICK! :warning: ", colour=discord.Colour.dark_gold()
    )
    kick.add_field(name="Deseja Kickar:", value=f"{usuario.mention} ?", inline=False)
    kick.add_field(
        name="VERIFICAÇÃO VALIDA POR:", value="```25 Segundos!```", inline=False
    )
    kick.set_footer(
        text=f"Kick Sendo Aplicado Por: {ctx.author} | {ctx.author.id}",
        icon_url=f"{ctx.author.avatar}",
    )
    kickmsg = await ctx.send(embed=kick)
    await kickmsg.add_reaction(str(sim))
    await kickmsg.add_reaction(str(nao))

    def check(reaction, user):
        # checka se foi o autor que reagiu!
        return user == ctx.author and str(reaction.emoji) in [str(sim), str(nao)]

    try:
        reaction, user = await client.wait_for(
            "reaction_add", timeout=25.0, check=check
        )
        if str(reaction.emoji) == str(sim):
            emb111 = discord.Embed(
                title="  **VOCÊ FOI KICKADO!!**  ", colour=discord.Colour.red()
            )
            emb111.add_field(
                name="Autor:",
                value=f"{ctx.author.mention} | {ctx.author.id}",
                inline=True,
            )
            emb111.add_field(name="Motivo:", value=f"{motivo}", inline=False)
            emb111.set_footer(
                text=f"Grupo: {ctx.guild.name} | {ctx.guild.id}",
                icon_url=f"{guild.icon}",
            )
            try:
                await usuario.create_dm()
                pv = await usuario.dm_channel.send(embed=emb111)
                await usuario.kick(
                    reason=f"Banido Por {ctx.author} || MOTIVO: {motivo}"
                )
            except discord.Forbidden:
                try:
                    await pv.delete()
                    await kickmsg.delete()
                except Exception:
                    pass
                await ctx.send(
                    f"{ctx.author.mention} **Não Tenho Permissão Para Kickar Esse Usuário!**"
                )
            except discord.NotFound:
                pass
            except Exception:
                pass
            kick1 = discord.Embed(
                title=" :warning: KICK! :warning: ", colour=discord.Colour.dark_gold()
            )
            kick1.add_field(
                name="🔨Moderador:",
                value=f"{ctx.author.mention} {ctx.author.id}",
                inline=True,
            )
            kick1.add_field(
                name="👤Usuàrio Kickado:",
                value=f"{usuario.mention} {usuario.id}",
                inline=True,
            )
            kick1.add_field(name="📜Motivo:", value=f"{motivo}", inline=False)
            kick1.set_footer(
                text=f"Kick Aplicado Por: {ctx.author.name} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
            await kickmsg.edit(embed=kick1)
            await kickmsg.clear_reactions()
        elif str(reaction.emoji) == str(nao):
            kick2 = discord.Embed(
                title=" :warning: CANCELAMENTO DE KICK! :warning: ",
                colour=discord.Colour.dark_gold(),
            )
            kick2.add_field(
                name="Usuàrio Quase Kicado:", value=f"{usuario.mention} !", inline=False
            )
            kick2.set_footer(
                text=f"Kick Quase Aplicado Por: {ctx.author.name} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
            await kickmsg.edit(embed=kick2)
            await kickmsg.clear_reactions()
    except asyncio.TimeoutError:
        kick3 = discord.Embed(
            title=" :warning: KICK! (EXPIRADO 👎) :warning: ",
            colour=discord.Colour.dark_gold(),
        )
        kick3.add_field(
            name="Usuàrio Quase Kickado:", value=f"{usuario.mention}", inline=False
        )
        kick3.set_footer(
            text=f"Comando Dado Por: {ctx.author} | {ctx.author.id}",
            icon_url=f"{ctx.author.avatar}",
        )
        await kickmsg.edit(embed=kick3)
        await kickmsg.clear_reactions()
    except Exception:
        pass


@client.command(aliases=["b", "banir"])
@commands.has_permissions(ban_members=True)
async def ban(ctx, usuario: discord.Member, *, motivo="Não Inserido!"):
    try:
        guild = ctx.message.guild
        eban = client.get_emoji(763523657493512202)
        sim = client.get_emoji(763523690985816115)
        nao = client.get_emoji(763523692696174593)
        await ctx.message.delete()
        emb = discord.Embed(
            title=" :warning: BANIMENTO! :warning: ", colour=discord.Colour.gold()
        )
        emb.add_field(name="Deseja Banir:", value=f"{usuario.mention} ?", inline=False)
        emb.add_field(
            name="VERIFICAÇÃO VALIDA POR:", value="```30 Segundos!```", inline=False
        )
        emb.set_footer(
            text=f"Ban Sendo Aplicado Por: {ctx.author} | {ctx.author.id}",
            icon_url=f"{ctx.author.avatar}",
        )
        botmsg = await ctx.send(embed=emb)
        await botmsg.add_reaction(str(sim))
        await botmsg.add_reaction(str(nao))

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in [
                str(sim),
                str(nao),
            ]  # checka se foi o autor que reagiu!

        try:
            reaction, user = await client.wait_for(
                "reaction_add", timeout=30.0, check=check
            )
            if str(reaction.emoji) == str(sim):
                emb11 = discord.Embed(
                    title="  **VOCÊ FOI BANIDO!!**  ", colour=discord.Colour.red()
                )
                emb11.add_field(
                    name="Autor:",
                    value=f"{ctx.author.mention} | {ctx.author.id}",
                    inline=True,
                )
                emb11.add_field(name="Motivo:", value=f"{motivo}", inline=True)
                emb11.set_footer(
                    text=f"Grupo:: {ctx.guild.name} | {ctx.guild.id}",
                    icon_url=f"{guild.icon}",
                )
                try:
                    await usuario.create_dm()
                    pv = await usuario.dm_channel.send(embed=emb11)
                    await usuario.ban(
                        reason=f"Banido Por {ctx.author} || MOTIVO: {motivo}"
                    )
                except discord.Forbidden:
                    try:
                        await pv.delete()
                        await botmsg.delete()
                    except Exception:
                        pass
                    await ctx.send(
                        f"{ctx.author.mention} **Não Tenho Permissão Para Banir Esse Usuário!**"
                    )
                except discord.NotFound:
                    pass
                except Exception:
                    pass

                emb1 = discord.Embed(
                    title=" :warning: BANIMENTO! :warning: ",
                    colour=discord.Colour.gold(),
                )
                emb1.add_field(
                    name="🔨Moderador:",
                    value=f"{ctx.author.mention} | {ctx.author.id}",
                    inline=True,
                )
                emb1.add_field(
                    name="👤Usuàrio Banido:",
                    value=f"{usuario.mention} | {usuario.id}",
                    inline=True,
                )
                emb1.add_field(name="📜Motivo:", value=f"{motivo}", inline=False)
                emb1.set_footer(
                    text=f"Ban Aplicado Por: {ctx.author} | {ctx.author.id}",
                    icon_url=f"{ctx.author.avatar}",
                )
                await botmsg.edit(embed=emb1)
                await botmsg.clear_reactions()
                await botmsg.add_reaction(f"{eban}")
            elif str(reaction.emoji) == str(nao):
                emb2 = discord.Embed(
                    title=" :warning: CANCELAMENTO DE BANIMENTO! :warning: ",
                    colour=discord.Colour.gold(),
                )
                emb2.add_field(
                    name="Usuàrio Quase Banido:",
                    value=f"{usuario.mention} !",
                    inline=False,
                )
                emb2.set_footer(
                    text=f"Ban Quase Aplicado Por: {ctx.author} | {ctx.author.id}",
                    icon_url=f"{ctx.author.avatar}",
                )
                await botmsg.edit(embed=emb2)
                await botmsg.clear_reactions()
        except asyncio.TimeoutError:
            emb3 = discord.Embed(
                title=" :warning: BANIMENTO! (EXPIRADO 👎) :warning: ",
                colour=discord.Colour.gold(),
            )
            emb3.add_field(
                name="Usuàrio Quase Banido:", value=f"{usuario.mention}", inline=False
            )
            emb3.set_footer(
                text=f"Comando Dado Por: {ctx.author} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
            await botmsg.edit(embed=emb3)
            await botmsg.clear_reactions()
    except discord.NotFound:
        pass
    except Exception:
        pass


@client.command(aliases=["u", "desbanir"])
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, user):
    await ctx.message.delete()
    if user.isdigit():
        idUSER = user
        try:
            user = int(user)
            user = await client.fetch_user(user)
            unbann = discord.Embed(
                title=" :warning: DESBANIMENTO! :warning: ",
                colour=discord.Colour.orange(),
            )
            unbann.add_field(
                name="Usuàrio:", value=f"{user}  |  {idUSER}", inline=False
            )
            unbann.set_footer(
                text=f"Desbanido por: {ctx.author} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
            unbann2 = discord.Embed(
                title=" :warning: ERRO EM DESBANIR! :warning: ",
                colour=discord.Colour.orange(),
            )
            unbann2.add_field(name="ID:", value=f"{user}", inline=False)
            unbann2.set_footer(
                text=f"Tentativa De Desbanir por: {ctx.author} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
        except discord.NotFound:
            return await ctx.send(embed=unbann2)
        else:
            await ctx.guild.unban(user)
            await ctx.send(embed=unbann)


@client.command(aliases=["c", "limpar", "cls", "clean"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, quantidade=1):
    guild = ctx.message.guild
    qntd = int(quantidade) + 1
    lx = client.get_emoji(763523917519257601)
    await ctx.channel.purge(limit=(int(qntd)))
    clsss = discord.Embed(
        title=f" {lx} **CHAT LIMPO!** {lx} ", colour=discord.Colour.red()
    )
    clsss.add_field(
        name="Chat Limpor Por:", value=f"{ctx.author.mention}", inline=False
    )
    clsss.set_thumbnail(url=ctx.author.avatar)
    clsss.set_footer(text=f"Foram Limpas Com Sucesso: {str(quantidade)} Mensagens!")
    await ctx.send(embed=clsss)


@client.command(aliases=["avatar", "userphoto"])
async def foto(ctx, user: discord.Member):
    emojis = ["❤️", "🍭", "👻", "💫", "⚔️", "👹", "😎", "😻"]
    emoj = random.choice(emojis)
    await ctx.message.delete()
    url = user.avatar
    urll = str(url)
    ftt = discord.Embed(
        title=f"     {user.name}  ",
        description="**Clique No Nome Para Baixar a Imagem!**",
        url=f"{urll}",
        colour=discord.Colour.dark_purple(),
    )
    ftt.set_image(url=f"{user.avatar}")
    env = await ctx.send(embed=ftt)
    await env.add_reaction(emoj)


@client.command(aliases=["abraco", "abraço", "abracar", "abraçar"])
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    panda = client.get_emoji(763523935920324618)
    gifs = [
        "data:image/jpeg;base64,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",
        "https://i.pinimg.com/originals/79/f3/99/79f399d5428bd150859d278bbaa318ad.gif",
        "https://i.pinimg.com/originals/a5/44/f0/a544f08631565a5b990a97a77dc9e499.gif",
        "https://64.media.tumblr.com/tumblr_maf0uwybuP1qzd219o1_500.gif",
        "https://i.pinimg.com/originals/2d/2e/fe/2d2efefb331649e95dd48cdbbccdf706.gif",
        "https://steamuserimages-a.akamaihd.net/ugc/276221870388647094/AD53F99D7479BDF5B9253A018FA682FBFA238B39/",
        "https://img.wattpad.com/b0d06efae33306bbc7ddbf367c581f2e5aa56fdf/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f5047657a63664f4d764a4e3077773d3d2d3730313331393939332e313538376237323266313561336261373536303732303233333535322e676966?s=fit&w=720&h=720",
        "https://sfc.euamo.moe/jp/src/1487202183127.gif",
        "https://em.wattpad.com/7f94c4259f3537d2954934af28e135e6623252a8/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f42457a6f70475952676e51462d673d3d2d34342e313538616632633937316263346165613232393437363431323934372e676966?s=fit&w=720&h=720",
        "https://i.imgur.com/O6X8nOo.gif",
        "https://media.giphy.com/media/kR8Ijlk4Az4jK/giphy.gif",
        "https://pa1.narvii.com/6486/88571a68d4a0a56570df3de75fd53c010b51c410_hq.gif",
        "https://3.bp.blogspot.com/-kk7LSuKAm4Q/UrERF_hFAwI/AAAAAAAAAWA/gDThqXGEpLE/s1600/tumblr_me64tuKjcN1rxui9eo1_500.gif",
        "https://64.media.tumblr.com/1fa1d5d2d2a923a76d3cb1f9a69bcafb/tumblr_mgq4oi5NOv1rsv495o1_250.gifv",
        "https://pa1.narvii.com/6827/87f999aaafb1658146d9cacd9240653feaa17ee0_hq.gif",
        "https://img4.wikia.nocookie.net/__cb20131222135104/dragonball/images/b/b4/Hugging.gif",
        "https://pa1.narvii.com/7305/5119a5759e686bb1e7cf25d266831f6dc9fe7f3br1-500-300_hq.gif",
        "https://gifman.net/wp-content/uploads/2019/06/casal-apaixonado-07.gif",
        "https://64.media.tumblr.com/tumblr_ljyfins8NL1qedewno1_500.gif",
        "https://64.media.tumblr.com/71d30ee1c0f9d844a1343ef9506aa8b6/tumblr_mq7yhw1EMg1rpr64go1_500.gifv",
        "https://pa1.narvii.com/6365/a47db5289d994181166838c750f6e5058b88b612_hq.gif",
        "https://cdn.lowgif.com/full/0a2a6bc5e89289e1-imagem-de-anime-romance-and-anime-couple-all-things-anime.gif",
    ]
    gif = random.choice(gifs)
    ab = discord.Embed(
        title=f"{panda} **{ctx.author.name}**    *Abraçou:*    **{user.name}** {panda}",
        colour=discord.Colour.from_rgb(216, 0, 255),
    )
    ab.set_image(url=str(gif))
    await ctx.send(embed=ab)


@client.command(aliases=["bj", "beijar", "beijo"])
async def kiss(ctx, user: discord.Member):
    panda = client.get_emoji(763523935920324618)
    await ctx.message.delete()
    bjs = [
        "https://media.discordapp.net/attachments/701283714662924348/753308522434789516/animebeijando.gif",
        "https://i.pinimg.com/originals/b0/37/a0/b037a0d27fc2fce28cd279561ec89825.gif",
        "https://em.wattpad.com/ea6d0c9e1478321c337b0fc6f7d48c9523be84f5/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f49585f7a6c636953695f364742413d3d2d3638312e313565333661343964383164393536353336333936363333393938332e676966",
        "https://i.pinimg.com/originals/af/c3/00/afc30074164c97655ea37833fe1a86e2.gif",
        "https://em.wattpad.com/d3089117835bb4352424efc9a91646ceee4fee18/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f51586c706958635f6f33675448773d3d2d3638312e313565333661323039393830316637303736333335333832363137302e676966",
        "https://pa1.narvii.com/6407/c5c62efd45527b8ab2fbd80ebcebb69697485658_hq.gif",
        "https://64.media.tumblr.com/9acffef12ec20f159c217846b4b6ca4e/tumblr_nmmd8t3Lur1qc02n4o4_500.gifv",
        "https://www.intoxianime.com/wp-content/uploads/2017/06/gif1-4.gif",
        "https://64.media.tumblr.com/bc45ad8984b7f0e85450d0e89374e644/tumblr_n0l3ppewio1rhcyq5o1_400.gif",
        "https://em.wattpad.com/b052e484b86c6884c0a53c4603473770eb7b4fdc/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f30616136745259667057693344413d3d2d3638312e313565333662343738663532643762383531333439373337333930362e676966",
        "https://pa1.narvii.com/6370/e916d03f931ccb0f3429dee8a57b2d611f8d0b4d_hq.gif",
        "https://64.media.tumblr.com/2bbeb57901f4a62bc8bc268d8122db9a/tumblr_okry1lbeWq1qcsnnso1_540.gifv",
    ]
    bj = random.choice(bjs)
    bjj = discord.Embed(
        title=f"{panda} **{ctx.author.name}**    *Beijou:*    **{user.name}** {panda}",
        colour=discord.Colour.from_rgb(216, 0, 255),
    )
    bjj.set_image(url=str(bj))
    await ctx.send(embed=bjj)


@client.command(aliases=["ui"])
async def userinfo(ctx, user: discord.Member):
    await ctx.message.delete()
    barata = client.get_emoji(763533912663261254)
    mf = client.get_emoji(763231027509461032)
    uf = discord.Embed(
        title=f"{barata} **{user.name}** {barata}", colour=discord.Colour.blue()
    )
    uf.add_field(name="ID:", value=f"{mf}`{user.id}`", inline=False)
    uf.add_field(name="CRIAÇÃO:", value=f"{mf}`{user.created_at}`", inline=False)
    uf.add_field(name="TOP CARGO:", value=f"{mf}{user.top_role.mention}", inline=False)
    # uf.add_field(name="PERMISSÕES:", value=f'{mf}`{user.permissions_in(ctx.message.channel)}`', inline=False)
    uf.set_thumbnail(url=f"{user.avatar}")
    uf.set_footer(
        text=f"Comando Solicitado por: {ctx.author} | {ctx.author.id}",
        icon_url=f"{ctx.author.avatar}",
    )
    await ctx.send(embed=uf)


@client.command(aliases=["lk"])
@commands.has_permissions(manage_messages=True)
async def lock(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    channel = ctx.message.channel
    barata = client.get_emoji(763533912663261254)
    ulk = discord.Embed(
        title=f"{barata} **INICIANDO!!** {barata}", colour=discord.Colour.red()
    )

    msg = await ctx.send(embed=ulk)
    for role in guild.roles:
        try:
            await channel.set_permissions(role, read_messages=True, send_messages=False)
            print(role)
        except Exception:
            pass
    ulk2 = discord.Embed(
        title=f"{barata} **SUCESSO!!** {barata}", colour=discord.Colour.red()
    )
    await msg.edit(embed=ulk2)


@client.command(aliases=["ulk"])
@commands.has_permissions(manage_messages=True)
async def unlock(ctx):
    await ctx.message.delete()
    barata = client.get_emoji(763533912663261254)
    guild = ctx.message.guild
    channel = ctx.message.channel
    ulk = discord.Embed(
        title=f"{barata} **INICIANDO!!** {barata}", colour=discord.Colour.red()
    )

    msg = await ctx.send(embed=ulk)
    for role in guild.roles:
        try:
            await channel.set_permissions(role, read_messages=True, send_messages=True)
            # ulkR = discord.Embed(
            #     title = f"{barata} **INICIANDO!!** {barata}",
            #     description=f'Role -> **{role}**',
            #     colour = discord.Colour.red()
            #     )
            # await msg.edit(embed=ulkR)
            # print(role)
        except Exception:
            pass

    ulk2 = discord.Embed(
        title=f"{barata} **SUCESSO!!** {barata}", colour=discord.Colour.red()
    )
    await msg.edit(embed=ulk2)


@client.command(aliases=["si", "svinfo"])
async def serverinfo(ctx):
    guild = ctx.message.guild
    await ctx.message.delete()
    dd = client.get_emoji(763532922874626089)
    eoff = client.get_emoji(770691594327294032)
    eo = client.get_emoji(770691485506338816)
    eau = client.get_emoji(770691565785055234)
    enp = client.get_emoji(770691508206567476)
    eb = client.get_emoji(770692631742906409)
    dev = client.get_emoji(770691738086932490)
    np = [member for member in guild.members if member.status == discord.Status.dnd]
    on = [member for member in guild.members if member.status == discord.Status.online]
    aus = [member for member in guild.members if member.status == discord.Status.idle]
    off = [
        member for member in guild.members if member.status == discord.Status.offline
    ]
    bot = [member for member in guild.members if member.bot == True]
    svii = discord.Embed(
        title=f" {dd} Informações Do Servidor {dd} ",
        description="",
        colour=discord.Colour.from_rgb(0, 255, 0),
    )
    svii.add_field(name="Nome:", value=f"{guild.name}", inline=False)
    svii.add_field(name="ID:", value=f"{guild.id}", inline=False)
    svii.add_field(name="Data De Criação:", value=f"{guild.created_at}", inline=False)
    # svii.add_field(name="Região:", value=f"{guild.region}", inline=False)
    svii.add_field(name=f"{dev}Criador:", value=f"{guild.owner.mention}", inline=False)
    svii.add_field(
        name="Quantidade De Membros:", value=f"{guild.member_count}", inline=False
    )
    svii.add_field(name=f"{eo}Online:", value=f"{len(on)}", inline=True)
    svii.add_field(name=f"{enp}Ocupados:", value=f"{len(np)}", inline=True)
    svii.add_field(name=f"{eau}Ausentes:", value=f"{len(off)}", inline=True)
    svii.add_field(name=f"{eoff}Offline:", value=f"{len(off)}", inline=True)
    svii.add_field(name=f"{eb}Bots:", value=f"{len(bot)}", inline=True)
    svii.set_thumbnail(url=f"{guild.icon}")
    svii.set_footer(
        text=f"Comando Solicitado Por: {ctx.author.name} | {ctx.author.id}",
        icon_url=f"{ctx.author.avatar}",
    )
    sviio = await ctx.send(embed=svii)


@client.command(aliases=["geolocation"])
async def geoip(ctx, *, ipAddress="nd"):
    await ctx.message.delete()
    pensativo = client.get_emoji(747184879820865636)
    if ipAddress == "nd":
        errorr1 = discord.Embed(
            title=f" {pensativo} _ERROR!_ {pensativo} ",
            colour=discord.Colour.from_rgb(255, 0, 0),
        )
        errorr1.add_field(
            name="Insira Um Ip VÁLIDO!:", value="Ex: 127.0.0.1", inline=False
        )
        await ctx.send(embed=errorr1)
    else:
        earth = client.get_emoji(763523692055101442)
        astronaut = client.get_emoji(763523942895583233)
        r = requests.get(f"https://freegeoip.app/json/{ipAddress}")
        ctc = json.loads(r.text)
        ip = ctc["ip"]
        cidade = ctc["city"]
        cep = ctc["zip_code"]
        pais = ctc["country_code"]
        reg = ctc["region_name"]
        longitude = ctc["longitude"]
        fuso = ctc["time_zone"]
        latitude = ctc["latitude"]
        foda = discord.Embed(
            title=f" {earth}  Localização de: {ip} {earth} ",
            colour=discord.Colour.from_rgb(255, 255, 255),
        )
        foda.add_field(name="IP", value=f"{astronaut}> {ip}", inline=False)
        foda.add_field(name="País", value=f"{astronaut}> {pais}", inline=False)
        foda.add_field(name="Cidade", value=f"{astronaut}> {cidade}", inline=False)
        foda.add_field(name="Região", value=f"{astronaut}> {reg}", inline=False)
        foda.add_field(name="Cep", value=f"{astronaut}> {cep}", inline=False)
        foda.add_field(name="Fuso Horário", value=f"{astronaut}> {fuso}", inline=False)
        foda.add_field(name="Latitude", value=f"{astronaut}> {latitude}", inline=False)
        foda.add_field(
            name="Longitude", value=f"{astronaut}> {longitude}", inline=False
        )
        foda.set_footer(
            text=f"Pedido por: {ctx.author.name} | {ctx.author.id}",
            icon_url=f"{ctx.author.avatar}",
        )
        await ctx.send(embed=foda)

@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, usuario: discord.Member):
    try:
        guild = ctx.message.guild
        await ctx.message.delete()
        ov = discord.PermissionOverwrite()
        ov.send_messages = False
        ov.read_messages = True
        ov.speak = False
        ov.read_message_history = True
        ov.mention_everyone = False

        roleov = discord.Permissions(
            send_messages=False,
            read_messages=True,
            speak=False,
            read_message_history=True,
            mention_everyone=False,
        )
        mutedRole = discord.utils.get(guild.roles, name="〄 𝙈𝙪𝙩𝙚𝙙 〄")

        if not mutedRole:
            mutedRole = await guild.create_role(
                name="〄 𝙈𝙪𝙩𝙚𝙙 〄",
                reason="Cargo Muted.",
                permissions=roleov,
                colour=discord.Colour(0xFF0000),
            )
        await usuario.add_roles(mutedRole, reason=f"Mutado Por: {ctx.author.name}")
        await ctx.message.channel.set_permissions(
            mutedRole, overwrite=ov, reason="Cargo De Mute."
        )

        mub = discord.Embed(
            title=f" **Usuàrio  {usuario.name}  Mutado Com SUCESSO!!**",
            colour=discord.Color.from_rgb(255, 0, 0),
        )
        await ctx.send(embed=mub)
    except Exception:
        pass


@client.command()
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, usuario: discord.Member):
    try:
        guild = ctx.message.guild
        await ctx.message.delete()
        ov = discord.PermissionOverwrite()
        ov.send_messages = False
        ov.read_messages = True
        ov.speak = False
        ov.read_message_history = True
        ov.mention_everyone = False

        roleov = discord.Permissions(
            send_messages=False,
            read_messages=True,
            speak=False,
            read_message_history=True,
            mention_everyone=False,
        )
        mutedRole = discord.utils.get(guild.roles, name="〄 𝙈𝙪𝙩𝙚𝙙 〄")

        if not mutedRole:
            mutedRole = await guild.create_role(
                name="〄 𝙈𝙪𝙩𝙚𝙙 〄",
                reason="Cargo Muted.",
                permissions=roleov,
                colour=discord.Colour(0xFF0000),
            )
        await usuario.remove_roles(
            mutedRole, reason=f"DesMutado Por: {ctx.author.name}"
        )
        await ctx.message.channel.set_permissions(
            mutedRole, overwrite=ov, reason="Cargo De Mute."
        )

        unb = discord.Embed(
            title=f" **Usuàrio  {usuario.name}  Desmutado Com SUCESSO!!**",
            colour=discord.Color.from_rgb(0, 255, 0),
        )
        await ctx.send(embed=unb)
    except Exception:
        pass

@client.command(aliases=["addcargo", "addc", "addr", "adicioanrcargo", "adicionarrole"])
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member: discord.Member, *, RoleToADD):
    try:
        mf = client.get_emoji(763231027509461032)
        pensativo = client.get_emoji(763523696110469120)
        corazaum = client.get_emoji(763231203691462676)
        alert = client.get_emoji(763231048841953310)
        guild = ctx.message.guild
        try:
            roleeID = RoleToADD.replace("<@&", "").replace(">", "")
            roleID = ctx.message.guild.get_role(int(roleeID))
            if roleID >= ctx.author.top_role:
                q = discord.Embed(
                    title=f"{alert} **Você Não Tem Permissão, Pois o Cargo é Acima Do Seu!** {alert}",
                    colour=discord.Colour.from_rgb(255, 0, 0),
                )
                await ctx.send(embed=q)
                return
            await member.add_roles(roleID)

            embed = discord.Embed(
                title=f" {mf} **Adição De Cargo!** {mf} ",
                color=discord.Colour.from_rgb(255, 0, 255),
            )
            embed.set_thumbnail(url=guild.icon)
            embed.add_field(
                name=f"{alert}Informações:",
                value=f"{corazaum} **Cargo Dado Por: **{ctx.author.mention}\n\n{corazaum} **Cargo Recebido: **{roleID.mention}\n\n{corazaum} **Dado Para: **{member.mention}\n",
                inline=False,
            )
            embed.set_footer(
                text=f"Cargo Adicionado Por: {ctx.author.name} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
            await ctx.send(embed=embed)
            return
        except Exception:
            for role in ctx.guild.roles:
                if str(RoleToADD.lower()) in str(role.name.lower()):
                    roleNAME = discord.utils.get(ctx.guild.roles, name=str(role))
                    if roleNAME >= ctx.author.top_role:
                        q = discord.Embed(
                            title=f"{alert} **Você Não Tem Permissão, Pois o Cargo é Acima Do Seu!** {alert}",
                            colour=discord.Colour.from_rgb(255, 0, 0),
                        )
                        await ctx.send(embed=q)
                        return
                    await member.add_roles(roleNAME)

                    embed = discord.Embed(
                        title=f" {mf} **Adição De Cargo!** {mf} ",
                        color=discord.Colour.from_rgb(255, 0, 255),
                    )
                    embed.set_thumbnail(url=guild.icon)
                    embed.add_field(
                        name=f"{alert}Informações:",
                        value=f"{corazaum} **Cargo Dado Por: **{ctx.author.mention}\n\n{corazaum} **Cargo Recebido: **{roleNAME.mention}\n\n{corazaum} **Dado Para: **{member.mention}\n",
                        inline=False,
                    )
                    embed.set_footer(
                        text=f"Cargo Adicionado Por: {ctx.author.name} | {ctx.author.id}",
                        icon_url=f"{ctx.author.avatar}",
                    )
                    await ctx.send(embed=embed)
                    return
            await member.add_roles(RoleToADD)
    except AttributeError:
        q = discord.Embed(
            title=f"{pensativo} **Não Encontrei NENHUM Cargo Com Esse Nome!** {pensativo}",
            colour=discord.Colour.from_rgb(0, 120, 255),
        )
        await ctx.send(embed=q)
    except Exception:
        pass


@client.command(
    aliases=[
        "removecargo",
        "rmc",
        "rmr",
        "removercargo",
        "removerrole",
        "rmrole",
        "rmcargo",
    ]
)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member: discord.Member, *, RoleToADD):
    try:
        mf = client.get_emoji(763231027509461032)
        pensativo = client.get_emoji(763523696110469120)
        corazaum = client.get_emoji(763231203691462676)
        alert = client.get_emoji(763231048841953310)
        guild = ctx.message.guild
        try:
            roleeID = RoleToADD.replace("<@&", "").replace(">", "")
            roleID = ctx.message.guild.get_role(int(roleeID))
            if roleID >= ctx.author.top_role:
                q = discord.Embed(
                    title=f"{alert} **Você Não Tem Permissão, Pois o Cargo é Acima Do Seu!** {alert}",
                    colour=discord.Colour.from_rgb(255, 0, 0),
                )
                await ctx.send(embed=q)
                return
            await member.remove_roles(roleID)

            embed = discord.Embed(
                title=f" {mf} **Remoção De Cargo!** {mf} ",
                color=discord.Colour.from_rgb(255, 0, 255),
            )
            embed.set_thumbnail(url=guild.icon)
            embed.add_field(
                name=f"{alert}Informações:",
                value=f"{corazaum} **Cargo Removido Por: **{ctx.author.mention}\n\n{corazaum} **Cargo Removido: **{roleID.mention}\n\n{corazaum} **Removido De: **{member.mention}\n",
                inline=False,
            )
            embed.set_footer(
                text=f"Cargo Removido Por: {ctx.author.name} | {ctx.author.id}",
                icon_url=f"{ctx.author.avatar}",
            )
            await ctx.send(embed=embed)
            return
        except Exception:
            for role in ctx.guild.roles:
                if str(RoleToADD.lower()) in str(role.name.lower()):
                    roleNAME = discord.utils.get(ctx.guild.roles, name=str(role))
                    if roleNAME >= ctx.author.top_role:
                        q = discord.Embed(
                            title=f"{alert} **Você Não Tem Permissão, Pois o Cargo é Acima Do Seu!** {alert}",
                            colour=discord.Colour.from_rgb(255, 0, 0),
                        )
                        await ctx.send(embed=q)
                        return
                    await member.remove_roles(roleNAME)

                    embed = discord.Embed(
                        title=f" {mf} **Remoção De Cargo!** {mf} ",
                        color=discord.Colour.from_rgb(255, 0, 255),
                    )
                    embed.set_thumbnail(url=guild.icon)
                    embed.add_field(
                        name=f"{alert}Informações:",
                        value=f"{corazaum} **Cargo Removido Por: **{ctx.author.mention}\n\n{corazaum} **Cargo Removido: **{roleNAME.mention}\n\n{corazaum} **Removido De: **{member.mention}\n",
                        inline=False,
                    )
                    embed.set_footer(
                        text=f"Cargo Removido Por: {ctx.author.name} | {ctx.author.id}",
                        icon_url=f"{ctx.author.avatar}",
                    )
                    await ctx.send(embed=embed)
                    return
            await member.add_roles(RoleToADD)
    except AttributeError:
        q = discord.Embed(
            title=f"{pensativo} **Não Encontrei NENHUM Cargo Com Esse Nome!** {pensativo}",
            colour=discord.Colour.from_rgb(0, 120, 255),
        )
        await ctx.send(embed=q)
    except Exception:
        pass


@client.command(aliases=["sugerir"])
async def sugestao(ctx, *, msg):
    await ctx.message.delete()
    sg = client.get_emoji(737555132765437972)
    sgtsss = discord.Embed(
        title=f" {sg}  SUGESTÃO!  {sg} ", colour=discord.Colour.dark_orange()
    )
    sgtsss.add_field(name="Sugestao:", value=f"{msg}", inline=False)
    sgtsss.add_field(name="Enviada Por:", value=f"{ctx.author}", inline=False)
    await client.get_user(708240142179106889).create_dm()
    await client.get_user(708240142179106889).dm_channel.send(embed=sgtsss)
    sgtss = discord.Embed(title=f" {sg} SUCESSO! {sg} ", colour=discord.Colour.orange())
    sgtss.add_field(
        name="Sugestao Enviada Com SUCESSO!",
        value="Obrigado Pela Colaboração!",
        inline=False,
    )
    await ctx.send(embed=sgtss)


@client.command(aliases=["falar", "digitar"])
@commands.has_permissions(administrator=True)
async def say(ctx, *, mensagem):
    await ctx.message.delete()
    await ctx.send(mensagem)

client.run("BOT TOKEN HERE")
