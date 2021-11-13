x = (int(input("Napiš základ \n")))
y = (int(input("Napiš mocnitele \n")))
def vypocet(): 
    import math
    vysledek = math.pow(x,y)
    print(vysledek)

vypocet()
