import os
import math
def clear(): #limpia la consola 
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def leibniz(n):
    i = 0
    pi4 = 0 
    while i < n:
        pi4 = pi4 + ((-1)**i)/((2 * i) + 1)
        i += 1
    
    return pi4 * 4

def wallis(n):
    
    i = 1
    pi2 = 1
    while i <= n:
        pi2 =  pi2 * ((2*i)/((2*i)-1)) * ((2*i)/((2*i)+1))
        i += 1
    return pi2 * 2

def euler(n):

    pi2 = 0
    i = 0
    
    while i < n:
        pi2 = pi2 +((2**math.factorial(i))*math.factorial(i)**2)/(math.factorial(2*i+1))
        i +=1
    return pi2 *2 


if __name__ == "__main__":
    clear()
    print(leibniz(50))
    print(wallis(50))
    print(euler(50))
    