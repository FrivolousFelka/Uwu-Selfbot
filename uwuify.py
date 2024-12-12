import discord
import aiohttp
#Requires discord.py 1.7.3
#pip install discord.py=1.7.3


TOKEN = ""  

intents = discord.Intents.default()
intents.messages = True  

client = discord.Client(intents=intents, self_bot=True)

@client.event
async def on_ready():
    print(f"Bot connected as {client.user}")

@client.event
async def on_message(message):
    if message.author.id != client.user.id:
        return  
    
    try:

        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://uwu.pm/api/v1/uwu',
                json={'text': message.content}
            ) as response:
                data = await response.json()

   
        uwu_text = data.get('uwu', 'Error: No response text')
        await message.edit(content=uwu_text)
        
    except Exception as e:
        print(f"Error with API request: {e}")


client.run(TOKEN, bot=False)
