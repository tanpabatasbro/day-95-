print("mengecek bilangan prima")

while True:
    a = int(input("Masukkan Angka : "))

    def bilangan_prima(a):
        if a ==1:
            return 'bukan bilangan prima'
        for i in range(2, a):
            if a % i == 0 :
                return 'bukan bilangan prima'
            elif a ==1:
                return 'bukan bilangan prima'
        return 'bilangan prima'

    print(bilangan_prima(a))
    
    z = input("Lanjut (y/n)? : ")
    if z =="n":
        break