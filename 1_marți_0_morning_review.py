#1. Repetați (concatenați) string-ul "tralala" de 7 ori.
print("tralala" * 7)

#2. Obțineți partea întreagă a împărțirii lui 17 la 4.
print(17 // 4)

#3. 8 la puterea a 3a?
print(8 ** 3)

#4. setați variabilele
name = "Jane"
is_student = True

# și folosiți-le într-un condițional care să facă print pe un branch
# la un string de forma "<name> is a student."
# și pe celălalt branch "<name> is not a student."

if is_student:
    print(name + " is a student.")
else:
    print(name + " is not a student.")
# apoi repetați codul folosind variabilele
name = "Andrew"
is_student = False

if is_student:
    print(name + " is a student.")
else:
    print(name + " is not a student.")


#5. scrieți o funcție cube(x) ce calculează x la puterea a 3a.

def cube(x):
    return x ** 3

#6. luați un număr întreg ca input de la utilizator,
# și folosind funcția cube() faceți print cu textul:
# "Cubul numărului <număr> este <cub>."

x = int(input("Un număr întreg: "))
x_cube = cube(x)
# folosiți:
# a) concatenare de string-uri
print("Cubul numărului " + x + " este " + x_cube + ".")
# b) metoda .format()
print("Cubul numărului este .")


#7. dat fiind string-ul
s = "Bună dimineața!"

# - obțineți al 7lea caracter din string
print(s[6])
# - obțineți penultimul caracter din string
print(s[-2])
# - verificați dacă începe cu "Bu"
print(s.startswith("Bu"))
# - verificați dacă se termină cu "aa"
print(s.endswith("aa"))
# - numărați apariția caracterului "a"
print("'a' apare de", s.count("a"), "ori")
# formatare cu argument pozițional
"'a' apare de {} ori".format(s.count("a"))
# formatare cu keyword arg
"'a' apare de {num} ori".format(num=s.count("a"))
# formatare cu f-string
count = s.count("a")
f"'a' apare de {count} ori"

# - găsiți poziția pe care apare substring-ul "dimi"
s.find("dimi")

#8. dat fiind string-ul
t = "===Column header==="
# extrageți numele coloanei fără caracterele "="
t.strip("=")

#9. dat fiind string-ul
t = "Column header"
# generați un string nou cu lungime de 25 de caractere
# pad-uit la stângă și la dreapta cu caracterul "#"
t.center(25, '#')

#10. dat fiind variabila globală
M_TO_FT = 3.28084
# scrieți două funcții feet_to_meters(ft) și meters_to_feet(m)
def feet_to_meters(ft):
    return ft / M_TO_FT

def meters_to_feet(m):
    return m * M_TO_FT


#11. Opțional [pentru cine a terminat tot]
# scrieți o funcție format_minutes(total_minutes)
# ce primește ca argument numărul de minute
# și returnează un string formatat "ore:minute"

def format_minutes(total_minutes):
    #hours = int(total_minutes / 60)
    hours = total_minutes // 60
    
    #minutes = total_minutes - (hours * 60)
    minutes = total_minutes % 60
    
    return f"{hours}:{minutes:02d}"
    
format_minutes(122) # 2:02


#12. [Extra-opțional] Scrieți o funcție
def get_seconds_from_now(timespec):
    pass
# ce returnează numărul de secunde din momentul curent
# până la următoarea apariție a orei respective
# date în timespec.
#
# timespec va avea formatul "HH:MM".
#
# țineți cont că următoarea apariție a orei respective
# poate fi azi sau mâine, depinzând de ora curentă.
# 
# gândiți-vă la utilitatea posibilă
# a unei astfel de funcții.
#
# îmbunătățire posibilă:
# timespec să fie variabil astfel: "HH" / "HH:MM" / "HH:MM:SS"