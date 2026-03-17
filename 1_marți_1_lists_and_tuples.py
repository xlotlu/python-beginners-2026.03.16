# list and tuple are "sequences" (just like str)

# # iterația:
# for element in iterable:
#     print(element)
#     do_something_with(element)

# Dată fiind lista
l = [1, 2, 3, 4, 5]
# creați o listă nouă l2
# formată don pătratul numerelor din l

l2 = []
for num in l:
    square = num * num
    l2.append(square)

# Pattern de acumulare:
"""
1. am un iterabil sursă
2. instanțiez obiectul final
3. iterez prin sursă
4. îmi fac calculul pentru elementul curent
5. adaug (acumulez) la obiectul final
6. gata
"""

# Dată fiind lista
l = [1, 2, 3, 4, 5]
# aflați suma pătratelor elementelor din l
total = 0 
for num in l:
    square = num * num
    total += square
print(total)

# Dată fiind lista
lst = ["ala", "bala", "porto", "cala"]
# aflați de câte ori apare substring-ul "ala"
# în toate elementele listei
count = 0
for elem in lst:
    count += elem.count("ala")
print(count)

# Dată fiind lista de orașe
cities = ["Alba Iulia", "Arad", "Brașov",
          "Brăila", "București", "Cluj", "Timișoara"]
# creați o listă cu orașele care încep cu litera B
l2 = []
for city in cities:
    if city.startswith("B"):
        l2.append(city)
print(l2)


# Exercițiu
# dată fiind lista de tuple de forma (nume, vârstă)
candidates = [
    ("Andrei", 16),
    ("Gigel", 40),
    ("Andra", 21),
    ("Elena", 42),
    ("Bogdan", 84),
    ("Mara", 62),
    ("Ion", 34),
    ("Ioana", 12)
]
# creați două liste noi, `accepted` și `rejected`
# astfel încât persoanele cu vârsta între 18 și 60
# de ani sunt acceptate, iar restul respinse.

accepted = []
rejected = []

for name, age in candidates:
    if age >=18 and age < 60:
        accepted.append(name)
    else:
        rejected.append(name)

print("Persoanele acestea sunt acceptate: ", accepted)
print("Persoanele aceste sunt respinse:", rejected)

# Exercițiu:
# scrieți un funcție 
def remove_all_values(lst, v)
    pass

# ce modifică lista lst,
# ștergând elementul v

def remove_all_values(lst, v):
    while True:
        try:
            lst.remove(v)
        except ValueError:
            break


