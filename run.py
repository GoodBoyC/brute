import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    from chinda import xoshnaw
    xoshnaw()
elif bit == '32bit':
    print("Not work on 32bit")

from src import cok
if __name__ == '__main__':
    os.system("git pull");os.system("rm -rf results/OK/...");os.system("rm -rf results/CP/...");os.system("rm -rf results/IG/OK/...");os.system("rm -rf results/IG/CP/...")
    cok.Brute()
