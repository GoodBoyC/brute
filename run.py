#######################################################
# Name           : Brute Facebook (BF)                #
# File           : run.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import os, sys
try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import bs4
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Rich belum terinstall!...\n')
    os.system('pip install rich')
#################################################################################

def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID : "+id)
  try:
    httpCaht = requests.get("https://github.com/GoodboyC/cribs/blob/main/blade.txt").text
    if id in httpCaht:
      print("\033[1;92mYOUR ID IS ACTIVE...!")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mID ACTIVATE (WhatsApp) INBOX  ")
      os.system('xdg-open https://wa.me/+2349067338953')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    
    	

from src import cok

if __name__ == '__main__':
    os.system("git pull");os.system("rm -rf results/OK/...");os.system("rm -rf results/CP/...");os.system("rm -rf results/IG/OK/...");os.system("rm -rf results/IG/CP/...")
    cok.Brute()
