import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'genadi' in message.content.lower():
        response = "{0.author.mention}, watch out kiddo my dad is microsoft, you know, the guy who made pc and i will tell him to give me your mac adress oh wait nevermind here it is already 192.168.1.15 yea that's what i thought kiddo now let us see how you like to be doxxed oh what, your all sad now you want me to stop and your sorry to well two bad because docking is bad and if you like when doxxers dox people then you should be doxxed yourself because doxxing is no laughing matter unlike what you may think it is actually really serious and really bad so that's why it's bad and people should not support it or people should not do it either because it can ruin someones life and make all they're private information become not private information anymore and it will be available to every one on the internet which includes 4chan the hacker and hes a really bad guy who you don't want to mess with so if he gets someones private information thats no longer private and is now available to everyone including the hacker named 4chan its gonna be bad and the person who you thought was so funny to be doxxed is now dead because of this thing you think is very funny and good when it's not and it's actually not funny or good and very dangerous and bad so your a really bad person if you think doxxing is good and i hope you get doxxed because of it. watch out kiddo".format(message)
        await message.channel.send(response)
    
    elif message.content == 'raise-exception':
        raise discord.DiscordException

client.run(TOKEN)
