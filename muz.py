# A powerful and multi feature packed selfbot developed by muz
#  first off don't be a skid I release my tools for free, so the community can enjoy them rather than gatekeeping
# I hope you guys enjoy this release and join discord.gg/says for many more ^_^
# A detailted tutorial for this selfbot and my other one(s) can be found on my youtube
# https://www.youtube.com/@reapproved/videos
# CONTACT INFORMATION (if you run into any issues etc): @decmber31 on discord.


import discord
from discord.ext import commands
import asyncio
import os
import time
import requests
import random
from colorama import Fore, Style, init




TOKEN = "put your token in here"  # replace with your token
PREFIX = "?"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, self_bot=True, intents=intents)

ladder_mode = False  # Global toggle for ladder mode


@bot.event
async def on_ready():
    token = bot.http.token
    user = bot.user

    # Get server count
    guild_count = len(bot.guilds)

    # Get friend count
    headers = {"Authorization": token}
    try:
        r = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
        friends = [u for u in r.json() if u.get("type") == 1]
        friend_count = len(friends)
    except:
        friend_count = 0

    ascii_art = f"""{Fore.MAGENTA}
( ⠀⠀⠀⠀⠀⠀⠀⢀⣶⣾⣲⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣯⣳⡄
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣽⣾⣿⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⢈⣟⡟⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⡚⡋⡅⢸⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣏⠃⡟⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡵⠞⣫⠍⠡⠛⡗⠦⣼⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⢩⣉⡈⠈⡻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣀⠀⠀⣀⣤⡶⠋⠁⠋⡄⢩⡏⠃⠇⠁⠆⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣟⠇⣽⠧⡲⠁⡁⢌⡎⢷⡄⠀⠀⠀⠀⠀⠀⠀⣠⠞⠡⡀⠉⠳⣞⠙⠀⠄⠲⠇⡀⡈⠐⢍⡚⠀⠀⠃⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡾⠁⠑⠟⡎⢁⡀⠆⠠⠁⠧⡙⢦⡀⠀⠀⠀⢀⡼⠃⠈⠢⣌⠲⡄⠈⢯⡪⣟⠂⠏⠇⠄⠂⠨⠈⠀⣁⠈⡏⠀⠀⠀
⠀⠀⠀⠀⠀⣸⢋⠦⡄⠷⢶⠃⢋⠁⡉⢀⣀⣤⡭⠿⡶⠾⢶⡾⠡⡉⠢⢄⡀⠑⢌⠢⡊⣿⢍⠤⠀⠁⠂⠅⡁⠂⠐⠀⠄⡇⠀⠀⠀
⠀⠀⠀⠀⢠⡏⠁⠌⡆⡺⠙⠠⣢⡵⠞⠫⠋⠀⢀⠈⠢⢅⡞⠡⣀⠈⠑⠢⢍⠒⣄⡳⡌⢸⣆⠑⠐⠠⠀⠀⠁⠂⠀⠃⠈⡇⠀⠀⠀
⠀⠀⠀⠀⢾⠀⠊⡖⡂⣪⣴⠞⡛⡡⡄⠅⢀⠀⠄⠁⠁⣸⠀⠂⠤⣉⡒⠤⢄⣹⡟⠿⣾⠋⠉⠛⣶⠒⠛⠋⠉⠉⠙⠛⠲⠧⣤⡀⠀
⠀⠀⠀⠀⠈⠳⣇⡃⣰⣿⠃⠀⣻⣥⠤⠶⠾⠤⣅⡐⠀⠸⠷⣤⣀⣀⠉⠁⠒⠢⠍⢰⡇⠀⠀⣠⣟⣀⡭⠭⠍⣁⡒⠒⠤⢄⣀⠀⠀
⠀⠀⠀⠀⠄⠀⠈⣻⢿⡧⠇⡼⠏⠀⠀⠀⠀⠀⠀⠙⢦⠰⡀⠂⢉⠉⠙⠛⠛⠟⢻⠫⠛⣶⡶⠋⣐⠮⢟⡒⠤⣀⠈⠉⠒⠄⡾⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠃⢐⢅⣵⠃⢀⣤⡄⠀⠀⢠⣤⡀⠘⣇⠂⠅⠆⠄⠀⣢⠁⢉⠓⡀⠌⡔⢿⡜⠮⡓⢄⡈⠑⠠⣍⠒⠤⣼⠃⠀⠀
⠀⣄⡀⠀⠀⢰⠏⡡⠁⠂⠙⣇⢸⣿⠇⠀⠀⠸⣿⡗⣸⠏⠀⠇⠀⠐⠵⠧⢃⠀⠈⠀⠄⡅⠈⠻⣄⠉⠢⣉⠢⢄⡀⠉⣾⠃⠀⠀⠀
⠀⠈⠙⠀⠀⣾⠀⡈⢂⡴⠶⣿⣷⣦⠀⡄⢠⠀⣴⣾⡷⠖⠓⠶⢷⣀⠂⠁⠀⠪⡀⠀⠅⠐⠀⠀⠹⢷⣄⠈⠑⠦⢉⡾⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡇⠀⣿⡋⠀⠀⠀⠙⠿⣟⣿⣿⡿⠟⠉⠀⠀⠀⠁⠀⠉⠛⢦⣧⡀⠀⠀⠀⠁⠄⢄⢀⠀⠊⠛⢶⠶⠋⢀⣀⡄⠀⠀⠀
⠉⠉⠁⠀⠀⡇⣸⠃⣟⣦⣄⡀⠀⠀⠈⠙⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣦⠊⠠⠐⠊⡀⠂⠀⡐⠥⡾⠀⠀⠉⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⡿⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣴⣶⠄⠀⠀⠈⢿⡆⠈⠃⠠⠀⠀⠐⣸⠃⠀⢀⣀⡀⠀⠀⠀⠀
⠐⠚⠋⠀⠀⠘⣧⠀⠸⣿⣿⡿⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠁⠀⠀⠀⠀⠀⢿⡀⠄⠀⠂⢠⡾⠁⠀⠀⠀⠉⠙⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢷⡀⠈⠉⠀⠀⠀⠻⠿⠇⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠗⠀⣡⡼⠋⠀⠀⠀⢤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢳⡤⠤⣴⠲⡽⣖⣚⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣣⡴⠛⠁⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠏⠀⠀⢨⣾⠁⣀⡉⠙⠓⢦⣀⣀⣀⣀⣀⣀⣤⣤⣴⣶⣿⣿⣿⣝⣷⠛⢳⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣀⣀⣠⣾⣷⡿⣛⡻⣷⠄⣼⠭⡽⣿⣿⣅⡀⠀⣿⡟⠛⠻⣏⠉⠉⠙⠛⠋⠀⠀⣀⣴⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣏⠁⡞⣿⣟⠴⢜⣿⠷⠳⢾⣅⠀⠉⠛⣿⡷⣿⠿⣄⠀⠙⢦⡀⠀⠀⠀⠀⠸⢿⣿⣿⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠳⢬⣟⣯⢿⡃⠀⠀⠀⢩⣠⡴⠞⠁⠀⠻⣤⡽⠀⠀⠀⠙⢦⡀⠀⠀⢀⣼⣿⡿⠙⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢧⣀⠀⣀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣬⣷⣤⣴⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠿⢿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
{Style.RESET_ALL}
            MUZ CLIENT v1 {Fore.WHITE}| {Fore.MAGENTA}@85pw
"""




    info_box = f"""{Fore.MAGENTA}
╔════════════════════════════════════╗
║  {Fore.WHITE}M U Z   C L I E N T   V1               {Fore.MAGENTA}║
╠════════════════════════════════════╣
║ {Fore.WHITE}PREFIX    {Fore.MAGENTA}| {Fore.WHITE}{PREFIX}                      {Fore.MAGENTA}║
║ {Fore.WHITE}SERVERS   {Fore.MAGENTA}| {Fore.WHITE}{guild_count}                      {Fore.MAGENTA}║
║ {Fore.WHITE}FRIENDS   {Fore.MAGENTA}| {Fore.WHITE}{friend_count}                      {Fore.MAGENTA}║
║ {Fore.WHITE}CREATOR   {Fore.MAGENTA}| {Fore.WHITE}@decmber31                   {Fore.MAGENTA}║
║ {Fore.WHITE}SUPPORT   {Fore.MAGENTA}| {Fore.WHITE}hmu on discord       {Fore.MAGENTA}║
╚════════════════════════════════════╝
{Style.RESET_ALL}
"""



    print(ascii_art)
    print(info_box)


# LADDER MODE ON
@bot.command()
async def ladder(ctx):
    global ladder_mode
    await ctx.message.delete()
    ladder_mode = True
    print("🔩 Ladder Mode Enabled Twin — Everything you type will be laddered.")


# LADDER MODE OFF
@bot.command()
async def ladderend(ctx):
    global ladder_mode
    await ctx.message.delete()
    ladder_mode = False
    print("🛑 Ladder Mode Disabled Twin — You back to normal.")


# LADDER PACK WITH THRAX.TXT
@bot.command()
async def ladderpack(ctx, user: discord.User):
    await ctx.message.delete()
    try:
        with open("thrax.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("thrax.txt not found nigga.")
        return

    for line in lines:
        ladder_msg = "\n".join(line.split())
        try:
            await ctx.send(f"{user.mention}\n{ladder_msg}")
            await asyncio.sleep(0.3)
        except Exception as e:
            print(f"[ladderpack error] {e}")


@bot.event
async def on_message(message):
    global ladder_mode, caps_mode, bold_mode
    await bot.process_commands(message)

    

    # Auto React
    if message.author.id in autoreact_targets:
        emoji = autoreact_targets[message.author.id]
        try:
            await message.add_reaction(emoji)
        except discord.NotFound:
            pass  # ignore missing message error
        except Exception as e:
            print(f"[autoreact error] {e}")

    # AutoKill Logic
    if message.author.id in autokill_targets:
        line = random.choice(autokill_targets[message.author.id])
        try:
            await message.reply(f"{message.author.mention} {line}")
        except Exception as e:
            print(f"[autokill error] {e}")

    # Ladder Mode
    if ladder_mode and message.author.id == bot.user.id:
        if message.content.startswith("?"):
            return
        if "\n" in message.content:
            return
        ladder_msg = "\n".join(message.content.split())
        try:
            await message.delete()
            await message.channel.send(ladder_msg)
        except Exception as e:
            print(f"[ladder error] {e}")
        return

    # Caps Mode
    if caps_mode and message.author.id == bot.user.id:
        if message.content.startswith("?"):
            return
        try:
            await message.delete()
            await message.channel.send(message.content.upper())
        except Exception as e:
            print(f"[capsmode error] {e}")
        return

    # Bold Mode
    if bold_mode and message.author.id == bot.user.id:
        if message.content.startswith("?"):
            return
        lines = message.content.split("\n")
        formatted = []
        for line in lines:
            if line.startswith("# "):
                formatted.append(f"**{line[2:]}**")
            else:
                formatted.append(line)
        bold_msg = "\n".join(formatted)
        try:
            await message.delete()
            await message.channel.send(bold_msg)
        except Exception as e:
            print(f"[boldmode error] {e}")
        return

    # Mock Mode
    if message.author.id in mock_targets:
        mocked = mock_text(message.content)
        try:
            await message.channel.send(mocked)
        except Exception as e:
            print(f"[mockmode error] {e}")


mock_targets = []  # the user id(s) getting mocked.


def mock_text(text):
    result = ""
    upper = True
    for char in text:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char
    return result




@bot.command()
async def mockmode(ctx, user: discord.User):
    await ctx.message.delete()
    if user.id in mock_targets:
        print(f"Already mocking {user}")
    else:
        mock_targets.append(user.id)
        print(f"🤡 Now mocking {user}")


@bot.command()
async def stopmock(ctx, user: discord.User = None):
    await ctx.message.delete()
    if user:
        if user.id in mock_targets:
            mock_targets.remove(user.id)
            print(f"❌ Stopped mocking {user}")
        else:
            print("⚠️ Not mocking that user twin.")
    else:
        mock_targets.clear()
        print("🧹 Cleared all mock targets.")

# MUZ CLIENT 2025
@bot.command()
async def muz(ctx):
    await ctx.message.delete()

    ascii_art = (
f"{Fore.MAGENTA}"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠖⢢⠀⠁⠉⢃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠉⠑⠋⠉⢄⡀⠀⠁⠀⢘⠼⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠐⠒⠚⠀⢹⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⢀⠀⠀⠀⠀⠀⠰⠆⠀⣸⠗⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠹⣁⠄⠛⠀⠀⠘⠟⠀⠀⢀⣴⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡨⠾⠤⠤⣤⣤⡤⠶⠾⣟⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⠤⢴⠊⠁⠈⡿⢒⡋⣼⠳⡶⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀⠀⠀⠀⠀⣀⠎⠉⠀⠀⠀⠀⠀⠈⢶⣰⠾⢿⣾⡈⡆⢹⠷⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
        "⠀  @@decmber31      heh               ⠀⠀⠀⠀⠀\n"
        f"{Style.RESET_ALL}"
    )

    msg = (
        f"{Fore.MAGENTA}┏━━━{Fore.CYAN} General Commands {Fore.MAGENTA}━━━━━━━━━━━━━┓\n"
        f"{Fore.CYAN}?userinfo @user       {Fore.WHITE}→ grab user info\n"
        f"{Fore.CYAN}?avatar @user         {Fore.WHITE}→ grab user avatar\n"
        f"{Fore.CYAN}?say <msg>            {Fore.WHITE}→ say something\n"
        f"{Fore.CYAN}?purge <amount>       {Fore.WHITE}→ delete your messages\n"
        f"{Fore.MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"

        f"{Fore.MAGENTA}┏━━━{Fore.CYAN} Chat Tools {Fore.MAGENTA}━━━━━━━━━━━━━━━━━━┓\n"
        f"{Fore.CYAN}?ladder               {Fore.WHITE}→ ladder mode\n"
        f"{Fore.CYAN}?ladderend            {Fore.WHITE}→ end ladder mode\n"
        f"{Fore.CYAN}?ladderpack @user     {Fore.WHITE}→ ladder thrax.txt\n"
        f"{Fore.CYAN}?murder @user         {Fore.WHITE}→ send thrax.txt w/ delay\n"
        f"{Fore.CYAN}?murderfast @user     {Fore.WHITE}→ instant thrax spam\n"
        f"{Fore.CYAN}?autokill @user       {Fore.WHITE}→ auto reply w/ ar.txt\n"
        f"{Fore.CYAN}?stopautokill         {Fore.WHITE}→ stop autokill\n"
        f"{Fore.CYAN}?autoreact            {Fore.WHITE}→ reacts to your messages\n"
        f"{Fore.MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"

        f"{Fore.MAGENTA}┏━━━{Fore.CYAN} Status Commands {Fore.MAGENTA}━━━━━━━━━━━━━┓\n"
        f"{Fore.CYAN}?streaming <msg>      {Fore.WHITE}→ fake streaming status\n"
        f"{Fore.CYAN}?playing <msg>        {Fore.WHITE}→ fake playing status\n"
        f"{Fore.CYAN}?listening <msg>      {Fore.WHITE}→ fake listening status\n"
        f"{Fore.CYAN}?watching <msg>       {Fore.WHITE}→ fake watching status\n"
        f"{Fore.CYAN}?clearstatus          {Fore.WHITE}→ clear status\n"
        f"{Fore.MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n\n"

        f"{Fore.MAGENTA}┏━━━{Fore.CYAN} GC Tools {Fore.MAGENTA}━━━━━━━━━━━━━━━━━━━━━━┓\n"
        f"{Fore.CYAN}?gcfill               {Fore.WHITE}→ add tokens to gc\n"
        f"{Fore.CYAN}?gckill @user         {Fore.WHITE}→ gckill with tokens\n"
        f"{Fore.CYAN}?protection           {Fore.WHITE}→ name change loop\n"
        f"{Fore.MAGENTA}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"
    )

    await ctx.send(f"```{ascii_art}```")
    await ctx.send(f"```ansi\n{msg}```")


@bot.command()
async def streaming(ctx, *, text):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=text,
        url="https://twitch.tv/discord",  # can be any valid twitch url
    )
    await bot.change_presence(activity=stream)
    print(f"🎥 Streaming Status Set To: {text}")

# PLAYING STATUS
@bot.command()
async def playing(ctx, *, text):
    await ctx.message.delete()
    game = discord.Game(name=text)
    await bot.change_presence(activity=game)
    print(f"🎮 Playing Status Set To: {text}")


# LISTENING STATUS
@bot.command()
async def listening(ctx, *, text):
    await ctx.message.delete()
    listen = discord.Activity(type=discord.ActivityType.listening, name=text)
    await bot.change_presence(activity=listen)
    print(f"🎧 Listening Status Set To: {text}")


# WATCHING STATUS
@bot.command()
async def watching(ctx, *, text):
    await ctx.message.delete()
    watch = discord.Activity(type=discord.ActivityType.watching, name=text)
    await bot.change_presence(activity=watch)
    print(f"👀 Watching Status Set To: {text}")


# CLEAR STATUS
@bot.command()
async def clearstatus(ctx):
    await ctx.message.delete()
    await bot.change_presence(activity=None)
    print("❌ Cleared Status Twin.")

autoreact_targets = {}  # {user_id: emoji}


@bot.command()
async def autoreact(ctx, user: discord.User, emoji):
    await ctx.message.delete()
    autoreact_targets[user.id] = emoji
    print(f"Autoreacting to {user} with {emoji}")





@bot.command()
async def stopreact(ctx, user: discord.User):
    await ctx.message.delete()
    if user.id in autoreact_targets:
        del autoreact_targets[user.id]
        print(f"Stopped autoreacting to {user}")
    else:
        print("That user wasn't being autoreacted to twin.")


@bot.command()
async def dm(ctx, *, msg):
    await ctx.message.delete()
    token = bot.http.token
    headers = {"Authorization": token}

    try:
        r = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers)
        if r.status_code != 200:
            print("[x] Failed to get friends list.")
            return
        friends = [u for u in r.json() if u.get("type") == 1]
    except Exception as e:
        print(f"[dm error] {e}")
        return

    friend_ids = [f["id"] for f in friends]
    print(f"[+] Sending DMs to {len(friend_ids)} friends.")

    for i in range(0, len(friend_ids), 10):
        batch = friend_ids[i:i+10]
        for friend_id in batch:
            try:
                # Create DM Channel
                dm = requests.post(
                    "https://discord.com/api/v9/users/@me/channels",
                    headers=headers,
                    json={"recipient_id": friend_id}
                )
                if dm.status_code != 200:
                    print(f"[x] Failed DM channel for {friend_id}")
                    continue

                channel_id = dm.json()["id"]

                # Send Message
                send = requests.post(
                    f"https://discord.com/api/v9/channels/{channel_id}/messages",
                    headers=headers,
                    json={"content": msg}
                )

                if send.status_code == 200:
                    print(f"[✓] Sent DM to {friend_id}")
                else:
                    print(f"[x] Failed to send to {friend_id} ({send.status_code})")

            except Exception as e:
                print(f"[dm error] {e}")

        await asyncio.sleep(2)  # Cooldown between batches


caps_mode = False  # toggle for caps


@bot.command()
async def capsmode(ctx, mode):
    global caps_mode
    await ctx.message.delete()
    if mode.lower() == "on":
        caps_mode = True
        print("🔠 Caps Mode Enabled Twin — Everything you type will be UPPERCASE.")
    elif mode.lower() == "off":
        caps_mode = False
        print("🔠 Caps Mode Disabled Twin — You back to normal.")
    else:
        print("Usage: ?capsmode on / off")


bold_mode = False  # toggle for bold


@bot.command()
async def boldmode(ctx, mode):
    global bold_mode
    await ctx.message.delete()
    if mode.lower() == "on":
        bold_mode = True
        print("** Bold Mode Enabled Twin — Lines starting with # will be bolded.")
    elif mode.lower() == "off":
        bold_mode = False
        print("** Bold Mode Disabled Twin — Back to normal.")
    else:
        print("Usage: ?boldmode on / off")


@bot.command()
async def unbold(ctx):
    global bold_mode
    await ctx.message.delete()
    bold_mode = False
    print("** Bold Mode Disabled Twin — Back to normal.")


@bot.command()
async def uncaps(ctx):
    global caps_mode
    await ctx.message.delete()
    caps_mode = False
    print("🔠 Caps Mode Disabled Twin — Back to normal.")


@bot.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    deleted = 0

    async for message in ctx.channel.history(limit=amount + 1):
        if message.author.id == bot.user.id:
            try:
                await message.delete()
                deleted += 1
            except Exception as e:
                print(f"[purge error] {e}")

    print(f"🗑️ Purged {deleted} messages twin.")



@bot.command()
async def murder(ctx, user: discord.User):
    await ctx.message.delete()

    try:
        with open("thrax.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("thrax.txt not found twin.")
        return

    for line in lines:
        try:
            await ctx.send(f"{user.mention} {line}")
            await asyncio.sleep(1)  # 1 second delay per line
        except Exception as e:
            print(f"[murder error] {e}")


@bot.command()
async def murderfast(ctx, user: discord.User):
    await ctx.message.delete()

    try:
        with open("thrax.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("thrax.txt not found twin.")
        return

    for line in lines:
        try:
            await ctx.send(f"{user.mention} {line}")
        except Exception as e:
            print(f"[murderfast error] {e}")


autokill_targets = {}  # user_id : ar.txt lines


def load_ar_lines():
    try:
        with open("ar.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return ["you're getting packed twin"]


@bot.command()
async def autokill(ctx, user: discord.User):
    await ctx.message.delete()
    autokill_targets[user.id] = load_ar_lines()
    print(f"🔪 Autokilling {user} — Auto replying from ar.txt")


@bot.command()
async def stopautokill(ctx, user: discord.User = None):
    await ctx.message.delete()
    if user:
        if user.id in autokill_targets:
            del autokill_targets[user.id]
            print(f"❌ Stopped autokilling {user}")
    else:
        autokill_targets.clear()
        print("🧹 Cleared all autokill targets")


@bot.command()
async def userinfo(ctx, user: discord.User = None):
    await ctx.message.delete()
    user = user or ctx.author
    created = user.created_at.strftime("%Y-%m-%d %H:%M:%S")
    text = (
        f"Username   : {user}\n"
        f"ID         : {user.id}\n"
        f"Created At : {created}\n"
        f"Bot?       : {user.bot}"
    )
    await ctx.send(f"```{text}```")


@bot.command()
async def avatar(ctx, user: discord.User = None):
    await ctx.message.delete()
    user = user or ctx.author
    await ctx.send(user.avatar_url)



@bot.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def gcfill(ctx):
    await ctx.message.delete()

    if not isinstance(ctx.channel, discord.GroupChannel):
        await ctx.send("❌ This only works in group chats twin.")
        return

    try:
        with open("tokens.txt", "r", encoding="utf-8") as f:
            tokens = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("tokens.txt not found twin.")
        return

    print(f"[+] Adding {len(tokens)} tokens to GC {ctx.channel.id}")

    for token in tokens:
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }

        try:
            r = requests.put(
                f"https://discord.com/api/v9/channels/{ctx.channel.id}/recipients/{ctx.author.id}",
                headers=headers
            )

            if r.status_code == 204 or r.status_code == 200:
                print(f"[✓] Added token ending with {token[-10:]}")
            else:
                print(f"[x] Failed to add token ending with {token[-10:]} ({r.status_code})")

        except Exception as e:
            print(f"[gcfill error] {e}")

        await asyncio.sleep(1.5)  # cooldown per join


@bot.command()
async def gckill(ctx, user: discord.User):
    await ctx.message.delete()

    try:
        with open("tokens.txt", "r", encoding="utf-8") as f:
            tokens = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("tokens.txt not found twin.")
        return

    try:
        with open("gckill.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("gckill.txt not found twin.")
        return

    print(f"[+] Sending gckill in GC {ctx.channel.id} to {user}")

    for line in lines:
        for token in tokens:
            headers = {
                "Authorization": token,
                "Content-Type": "application/json"
            }

            payload = {
                "content": f"{user.mention} {line}"
            }

            try:
                r = requests.post(
                    f"https://discord.com/api/v9/channels/{ctx.channel.id}/messages",
                    headers=headers,
                    json=payload
                )

                if r.status_code == 200 or r.status_code == 204:
                    print(f"[✓] Token sent gckill msg")
                else:
                    print(f"[x] Failed to send with token ({r.status_code})")

            except Exception as e:
                print(f"[gckill error] {e}")

        await asyncio.sleep(1)  # 1s delay between each line


@bot.command()
async def protection(ctx):
    await ctx.message.delete()

    if not isinstance(ctx.channel, discord.GroupChannel):
        print("❌ This command only works in group chats twin.")
        return

    try:
        with open("protection.txt", "r", encoding="utf-8") as f:
            names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("protection.txt not found twin.")
        return

    print(f"[+] Starting protection name cycle in GC {ctx.channel.id}")

    for name in names:
        try:
            await ctx.channel.edit(name=name)
            print(f"[✓] Changed GC name to: {name}")
            await asyncio.sleep(2)  # delay between name changes
        except Exception as e:
            print(f"[protection error] {e}")

def loading_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = f"""{Fore.MAGENTA}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⢠⠋⠉⠉⠒⠲⢤⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣀⢀⡠⠖⠋⠉⠀⠀⠀⠀⠉⠉⠢⣄⠀⠀⠀⢀⠼⠤⠇⠀
⠀⠀⠀⣀⠔⠊⠁⠀⢨⠏⠀⠀⠀⣠⣶⣶⣦⠀⠀⠀⠀⠀⠱⣄⡴⠃⠀⠀⠀⠀
⢸⣉⠿⣁⠀⠀⠀⢀⡇⠀⠀⠀⠀⢿⣽⣿⣼⡠⠤⢄⣀⠀⠀⢱⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢦⡀⢸⠀⠀⠀⡠⠒⠒⠚⠛⠉⠀⢠⣀⡌⠳⡀⡌⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⣆⠀⢰⠁⣀⣀⠀⠀⣀⠀⠈⡽⣧⢀⡷⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡤⢄⠀⠈⠢⣸⣄⢽⣞⡂⠀⠈⠁⣀⡜⠁⣩⡷⠿⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢯⣁⡸⠀⠀⠀⡬⣽⣿⡀⠙⣆⡸⠛⠠⢧⠀⡿⠯⠆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⡀⠀⠀⡤⠤⣵⠁⢸⣻⡤⠏⠀⠀⠀⠀⢹⠀⠀⠀⡊⠱⣀⠀⠀⠀
⠀⠀⢀⠜⠀⢘⠀⠀⠱⠲⢜⣢⣤⣧⠀⠀⠀⠀⠀⢴⠇⠀⠀⠀⠧⠠⠜⠀⠀⠀
⠀⠀⠘⠤⠤⠚⠀⠀⠀⠀⠀⠀⢸⠁⠁⠀⣀⠎⠀⠻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣀⣀⡴⠤⠄⠴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Style.RESET_ALL}
        MUZ CLIENT v1
           by @@decmber31"""

    print(ascii_art)
    print(Fore.MAGENTA + "\nLoading Modules", end="")
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="", flush=True)
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

loading_screen()
bot.run(TOKEN, bot=False)


