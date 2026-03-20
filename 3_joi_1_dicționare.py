# dată fiind structura de date
jlst = ["Jane", 20, ["reading", "hiking", "biking"]]

# creați (manual) un dicționar cu cheile
# "name", "age", "hobbies" și valorile de mai sus
d = {
    "name": jlst[0],
    "age": jlst[1],
    "hobbies": jlst[2],
}
print(d)

# faceți-o pe Jane să îmbătrânească un an.
d['age'] += 1

print(d)

# adăugați-i hobby-ul "jogging"
d["hobbies"].append("jogging")


# dată fiind structura de date
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

# obțineți o listă de dicționare 
# [
#     {"name": ..., "age":..., "hobbies": ....},
#     {"name": ..., "age":..., "hobbies": ....},
#     {"name": ..., "age":..., "hobbies": ....},
# ]

# ne construim o listă nouă:
ld = []

# acum o populăm:
for friend in friends:
    # fiecare element este un dicționar de forma
    d = {
        "name": friend[0],
        "age" : friend[1],
        "hobbies": friend[2],
    }
    ld.append(d)
print(ld)


# dat fiind dicționarul
occupations = {
    "Jane": "nurse",
    "Mike": "firefighter",
    "Anna": "DBA",
    "Sam": "prosecutor",
}

# modificați dicționarele din lista de mai sus
# astfel încât să adăugați cheia "occupation"
# cu valoarea respectivă.
for person in ld:
    name = person["name"]
    # obținem ocupația din dicționarul
    # `occupations``
    try:
        v = occupations[name]
    except KeyError:
        v = None
    
    person["occupation"] = v

print(ld)


# scrieți o funcție
def count_words(txt, insensitive=False):
    pass
# ce returnează un dicționar
# în care cheile sunt fiecare cuvânt din `txt`
# iar valorile sunt, respectiv, numărul de apariții
# al cuvântului.

# strategie:
# - ștergem toate caracterele de punctuație
# - facem split textului
# - începem să numărăm

import string

# this will be a translation table
# ca să putem face replace într-o singură operațiune
_TRANSLATION = str.maketrans(
    string.punctuation,
    " " * len(string.punctuation)
)

def count_words(txt, insensitive=False):
    if insensitive:
        txt = txt.casefold()

    # pattern de acumulare:
    # 1. aceasta este sursa de date:
    words = txt.translate(_TRANSLATION).split()

    # 2. ne instanțiem obiectul
    out = {}

    # 3. iterăm prin sursa de date:
    for word in words:
        try:
            old_value = out[word]
        except KeyError:
            old_value = 0

        out[word] = old_value + 1

    return out

print(count_words(open("data/it-was.txt").read()))
# (vă rog în producție nu faceți one-liner din open() și .read())


wcount = count_words(open("data/it-was.txt").read())
# this is how we iterate a dictionary:
for k, v in d.items():
    print(k, "»", v)
