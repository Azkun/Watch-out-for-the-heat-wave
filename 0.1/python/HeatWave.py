# Finish by Geshi_San, thanks Geshi !

import threading, time, subprocess, os


print(" __          ______ _______ _    ___          __")
print(" \ \        / / __ \__   __| |  | \ \        / /")
print("  \ \  /\  / / |  | | | |  | |__| |\ \  /\  / / ")
print("   \ \/  \/ /| |  | | | |  |  __  | \ \/  \/ /  ")
print("    \  /\  / | |__| | | |  | |  | |  \  /\  /   ")
print("     \/  \/   \____/  |_|  |_|  |_|   \/  \/    ")
print("#----------------------------------------------------------------------------------#")
print("Welcome to the Python version of WOTHW ! This version is in bêta, so be indulgent.")
print("Python version developped by GeshiSan")
print("Propriety of BlackBotFR and GlitchBot, do not redistribute")
print("#----------------------------------------------------------------------------------#")
print("")
print("Program is running ! In 3 hours you will be noticed.")

def foo():
    print("Starting Launch.vbs !")
    filepath = 'launch.vbs'
    os.startfile(filepath)
    
WAIT_TIME_SECONDS = 10800

ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    foo()
    
#output:
#Tue Oct 16 17:29:40 2018
#Tue Oct 16 17:29:42 2018
#Tue Oct 16 17:29:44 2018
