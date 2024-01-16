import random

ti = input("Vnesi svojo potezo ")

Oton = random.randint(1, 3)

if ti == "kamen":
    print("Tvoja poteza je kamen")
elif ti == "papir": 
    print("Tvoja poteza je papir")
elif ti == "skarje":
    print("Tvoja poteza so škarje")


if Oton == 1: 
    print("Poteza Otona je kamen")
elif Oton == 2: 
    print("Poteza Otona je papir") 
else: 
    print("Poteza Otona so škarje")



if ti == "kamen" and Oton == 1:
    print("Izenačeno je")
elif ti == "papir" and Oton == 2:
    print("Izenačeno je")
elif ti == "škarje" and Oton == 3:
    print("Izenačeno je")
elif ti == "škarje" and Oton == 2:
    print("Ti si zmagal")
elif ti == "papir" and Oton == 1:
    print("Ti si zmagal")
elif ti == "kamen" and Oton == 3:
    print("Ti si zmagal")
elif Oton == 1 and ti == "škarje":
    print("Oton je zmagal")
elif Oton == 2 and ti == "kamen":
    print("Oton je zmagal")
elif Oton == 3 and ti == "papir":
    print("Oton je zmagal")
else:
    print("Napačen vnos ali izenačeno.")