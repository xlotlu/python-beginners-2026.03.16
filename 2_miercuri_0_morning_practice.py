# A. Dată fiind structura de date
# formată dintr-o listă de [name, age. hobbies]
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# 1. Schimbați vârsta lui Jane la 21

# 2. Adăugați hobby-urilor Annei "reading" și "cooking"

# 3. Ștergeți-i lui Mike hobby-ul de la indexul 1

# 4. Adăugați un prieten nou:
["Georgie", 22, ["reading", "cooking", "running"]]

# 5. Scrieți o funcție
def find_by_hobby(friends, hobby):
    pass
# ce, primind o listă de prieteni în formatul de mai sus
# și un hobby ca string, returnează o listă nouă
# cu prietenii care au acel hobby.

def find_by_hobby(flist, hobby):
    # creăm lista pe care o vom returna
    out = []
    # iterăm printre prieteni
    for friend in flist:
        # ne uităm printre hobby-uri
        hobbies = friend[2]

        # vedem dacă hobby-urile conțin pe cel căutat
        if hobby in hobbies:
            # dacă da, adăugam la lista returnată
            out.append(friend)

    return out


# 6. Scrieți o funcție
def find_by_age(friends, min_age, max_age):
    pass
# ce filtrează, la fel, după vârstă.
# Folosiți funcțiile `find_by_age` și `find_by_hobby`
# pentru a găsi prietenii cu vârstă între 20 și 30 de ani
# pasionați de "hiking".


# 7. [extra] adăugați tuturor persoanelor cu vârsta peste 30 de ani
#    hobby-ul "knitting".
#    folosiți funcția find_by_age() de mai sus pentru filtrare.


# B. Dată fiind lista de orașe

cities = [
    'Arad',
    'Brașov',
    'Cluj-Napoca',
    'Constanța',
    'Focșani',
    'Iași',
    'Oradea',
    'Pitești',
    'Satu Mare',
    'Sibiu',
    'Timișoara',
 ]

# 1. creați o listă cu primele 3 orașe
cities[3:]

# 2. creați o listă cu ultimele 3 orașe
cities[:3]

# 3. creați o listă cu orașele de la indexul 2 la 5 (inclusiv)
cities[2:6]

# 4. creați o listă cu ultimele 3 orașe în ordine inversă
cities[:-4:-1]

# 5. creați o listă nouă cu toate elementele în ordine inversă
cities[::-1]
