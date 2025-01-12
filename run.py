import os
import platform
os.system('clear')
os.system("git pull")
b = platform.architecture()[0]
if b == '64bit':
    import MX1.cpython-404.so
    
elif b == '32bit':
    import MX2.cpython-404.so

