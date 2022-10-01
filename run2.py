import os, platform
bit = platform.architecture()[0]
if bit == '64bit':
    from main import chinda
    chinda()
elif bit == '32bit':
    print("Not work on 32bit")
