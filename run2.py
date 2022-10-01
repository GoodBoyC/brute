import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    from chinda import xoshnaw
    xoshnaw()
elif bit == '32bit':
    print("Not work on 32bit")

from src import cok
Brute()
