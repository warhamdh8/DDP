#soal nomor 4
def bilangan(angka):
    for i in range(1,angka):
        if i % 2 != 0:
            print(i,end=", ")

bilangan(20)            

#soal nommor 3
print()
def nilai(n = 0):
    if n <= 60:
        print("tidak lulus")
    elif n > 60:
        print("lulus")  
    else :
        print("tidak diketahui")  

nilai(88)     
nilai() 


#soal nomor 2
def is_genap(n):
    return n %  2 == 0

print(is_genap(2))

#soal nomor 1
def celcius_ke_fahrenheit(celcius):
    return(celcius * 9/5) + 32

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))
