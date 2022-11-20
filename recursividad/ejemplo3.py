




def fact(num):
    if num == 0:
        return True
    else:
        return num * fact(num - 1)

def CoeBi(n, k):

    op = (fact(n))/(fact(k)*(fact(n-k)))

    return op

if __name__ == "__main__":
    acum = 0
    n = int(input("Ingrese el valor de N: "))
    k = int(input("Ingrese el valor de K: "))
    res = CoeBi(n, k)
    print("El resultado es:", res)