const Discord = require("discord.js");
const {client, GatewayIntentBits } = require('discord.js');

const axios = require('axios');

client.("message", async message => {
    if(message.content.startsWith("?rizz")) {
        // Get the text to send to the ChatGPT API
        const text = message.content.slice(6);
        
        // Make a request to the ChatGPT API
        const headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer YOUR_API_KEY"
        }
        const data = {
            "prompt": text,
            "temperature": 0.5
        }
        const response = await axios.post("https://api.openai.com/v1/engines/davinci/completions", data, { headers });
        
        // Get the response from the API
        const responseText = response.data.choices[0].text;
        
        // Send the response to the channel
        message.channel.send(responseText);
    }
});

client.login("MTA0NTU5MzcyNDkzMzEyNDExOA.GWWNyx.7HmkZGVb8sKNpXjHjNFuZfAooJjAo7C1XqIMhE");