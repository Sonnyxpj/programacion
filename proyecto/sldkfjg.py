import os

def clear(): #limpia la consola 
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
