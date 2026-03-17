# Exercițiu:
# Scrieți un script care cere numele utilizatorului
# și face output string-ului "Salut <nume>"

print("Cum te numești?")
nume = input()
print("Salut", nume)


# Exercițiu:
# Scrieți un script care cere numele utilizatorului
# și vârsta sa și, dacă are mai mult de 16 ani,
# îi spune "Ești acceptat"

name = input("Your Name? ")
age = input("Your Age? ")

if int(age) > 16:
    print("Salut " + name + " ești acceptat")


# Exercițiu:
# Cereți numele utilizatorului și dacă numele său începe
# cu un caracter între A și M, îi scrieți:
#    "ești la începutul catalogului"
# altfel:
#    "ești la sfârșitul catalogului"

# 1. aflăm primul caracter
# 2. îl comparăm


name = input("Cum te numesti? ")
first_letter = name[0].upper() # we normalize the char

if 'A' <= first_letter <= 'M':
    print("ești la începutul catalogului")
elif 'N' <= first_letter <= 'Z':
    print("ești la sfârșitul catalogului")
else:
    print("verifică-ți numele")


# Exercițiu:
# Scrieți salutul potrivit momentului zilei astfel:
# - între 5  (inclusiv) și 10 (exclusiv): Bună dimineața
# - între 10 (inclusiv) și 18 (exclusiv): Bună ziua
# - între 18 (inclusiv) și 22 (exclusiv): Bună seara
# - între 22 (inclusiv) și  5 (exclusiv): Noapte bună

hour = int(input("Cât este ceasul? " ))

if 5 < hour < 10: 
    salut = "Bună dimineața"
elif 10 <= hour < 18:
    salut = "Bună ziua"
elif 18 <= hour <= 22:
    salut = "Bună seara"
elif 0 <= hour < 5 or 22 <= hour < 24:
    salut = "Noapte bună"

print(salut)