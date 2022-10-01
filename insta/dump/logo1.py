#######################################################
# Name           : Brute Facebook (BF)                #
# File           : logo.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import sys, os, datetime, random

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from datetime import datetime
from rich.panel import Panel

reed = "[bold red]"
blue = "[bold blue]"

class Logo:

    def __init__(self):
        if "linux" in sys.platform.lower():
            try:os.system("clear")
            except:pass
        elif "win" in sys.platform.lower():
            try:os.system("cls")
            except:pass
        else:
            try:os.system("clear")
            except:pass
        WAR = random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
        prints(Panel(f"""{WAR}  
    ██████╗██╗  ██╗██╗███╗   ██╗██████╗  █████╗ 
   ██╔════╝██║  ██║██║████╗  ██║██╔══██╗██╔══██╗
   ██║     ███████║██║██╔██╗ ██║██║  ██║███████║
   ██║     ██╔══██║██║██║╚██╗██║██║  ██║██╔══██║
   ╚██████╗██║  ██║██║██║ ╚████║██████╔╝██║  ██║
    ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
 {WAR}version: 0.4[/]"""))
   
