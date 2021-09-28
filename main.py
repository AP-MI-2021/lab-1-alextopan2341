#Returneaza true daca e prim si false daca nu e prim
def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range (2,n):
            if n % i == 0:
                return False
        return True

#Returneaza produsul numerelor din lista lst.
def get_product(lst):
    p = 1
    for i in lst :
        p *= i
    return p
#Returneaza cmmdc prin impartiri repetate
def get_cmmdc_v1(x, y):
    while y != 0:
        t = y
        y = x%y
        x = t
    return x
#Returneaza cmmdc prin scaderi repetate
def get_cmmdc_v2(x, y):
    if x == 0:
        return y
    while y != 0 :
        if x > y:
            x -= y
        else:
            y -= x
    return x
def main():
    print("0. Exit")
    print("1. Numar prim")
    print("2. Produsul numerelor dintr-o lista")
    print("3. CMMDC prin impartiri repetate")
    print("4. CMMDC prin scaderi repetate")
    exer = int(input("Alegeti un exercitiu: "))
    while exer!= 0:
        if exer == 1:
            nr = int(input("Dati un numar: "))
            if is_prime (nr)== True:
                print("Numarul e prim")
            else:
                print("Numarul nu e prim")
        elif exer == 2:
            n = int(input("Dati lungimea sirului: "))
            l = []
            for i in range (0 , n) :
                el = int(input("Dati elementul: "))
                l.append(el)
            print(get_product(l))
        elif exer == 3:
            x = int(input("Primul numar este: "))
            y = int(input("Al doilea numar este:"))
            print(get_cmmdc_v1(x,y))
        elif exer == 4:
            x = int(input("Primul numar este: "))
            y = int(input("Al doilea numar este:"))
            print(get_cmmdc_v2(x, y))
        else:
            if exer>4:
                print("Acest exercitiu nu exista")
        print("0. Exit")
        print("1. Numar prim")
        print("2. Produsul numerelor dintr-o lista")
        print("3. CMMDC prin impartiri repetate")
        print("4. CMMDC prin scaderi repetate")
        exer = int(input("Alegeti un exercitiu: "))
main()