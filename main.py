import discord
import difflib
import re
from colorama import Fore, Style
import os
from requests_html import HTMLSession

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):
    try:
        embeds = message.embeds
        for embed in embeds:
            kimage = embed.to_dict()
            title = kimage.get('title')
            pimage = kimage.get('image')
            imagePath = pimage.get('url')
            googlePath = 'https://www.google.com/searchbyimage?image_url='
            url = googlePath + imagePath + "&as_sitesearch=myanimelist.net"

            session = HTMLSession()
            r = session.get(url)
            nest = r.html.absolute_links

            final = difflib.get_close_matches("https://myanimelist.net/character/", nest)

            name = re.search(r'(https:\/\/myanimelist.net\/)(character\/)([A-Za-z0-9-]+\/)([A-Za-z0-9À-ȕ-_]+)', final[0])
            
            if (title == 'A wild Waifu/Husbando appears!' and message.author.id == 727954884028268545 and message.guild.id != 727943425374290001):
                await message.channel.send("k.claim " + name.group(4).replace("_", " "))
                print(Fore.GREEN +"Claimed!")
                print(Style.RESET_ALL)

    except AttributeError:
        print(Fore.BLUE +"Not KaguyaBot Embed")
        print(Style.RESET_ALL)

    except IndexError:
        print(Fore.RED +"Not In Search Result")
        print(Style.RESET_ALL)

client.run(os.environ['token'])