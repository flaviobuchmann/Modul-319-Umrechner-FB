#===== Grad in Bogenmass =====
def grad_in_bogenmass(grad):
    import math
    return grad * (math.pi / 180)

#===== Bogenmass in Grad =====
def bogenmass_in_grad(bogenmass):
    import math
    return bogenmass * (180 / math.pi)

#===== Fahrenheit in Celsius =====
def fahrenheit_in_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

#===== Celsius in Fahrenheit =====
def celsius_in_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

#===== Primzahlfunktion =====
def Primzahlfunktion():
    zahl = int(input("Geben Sie eine Zahl ein: "))
    if zahl > 1:
        for i in range(2, int(zahl/2)+1):
            if (zahl % i) == 0:
                print(f"{zahl} ist keine Primzahl.")
                break
        else:
            print(f"{zahl} ist eine Primzahl.")
    else:
        print(f"{zahl} ist keine Primzahl.")

#===== Fakultät =====
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n-1)
