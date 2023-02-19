import discord
import requests

client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print("Bot has successfully started!")


@client.event
async def on_message(message):
    if message.content.startswith("!rizz"):
        # send to the AI
        text = message.content[6:]
        print("Someone used the command")
        
        # Make a request to the AI
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"
        }
        data = {
            "prompt": text,
            "temperature": 0.5
        }
        response = requests.post("https://api.openai.com/v1/engines/davinci/completions", headers=headers, json=data)
        
        # Get the response from the AI
        response_text = response.json()["choices"][0]["text"]
        
        # Send the response to the user
        await message.channel.send(response_text)


client.run("MTA0NTU5MzcyNDkzMzEyNDExOA.GWWNyx.7HmkZGVb8sKNpXjHjNFuZfAooJjAo7C1XqIMhE")