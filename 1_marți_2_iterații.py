# # iterația cu for:
# for element in iterable:
#     print(element)
#     do_something_with(element)

for x in range(5):
    print("processing", x)
    if x > 3:
        break
    else:
        print("! ! ! !", x)
print("am ieșit din for")


for x in range(7):
    print("ceva tot timpul cu", x)
    if x < 3:
        continue
        
    print("fac o grămadă de chestii cu", x)
print("am ieșit din for")


# dată fiind lista de tuple de forma (city, distance)
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 170),
    ('Craiova', 230),
    ('Galați', 250),
    ('Oradea', 600),
    ('Ploiești', 60),
    ('Brăila', 200),
    ('Arad', 530),
    ('Pitești', 120),
    ('Sibiu', 280),
    ('Bacău', 300),
    ('Târgu Mureș', 340),
    ('Baia Mare', 600),
    ('Buzău', 110),
    ('Satu Mare', 640),
    ('Suceava', 450),
    ('Focșani', 190),
]

# obțineți o listă cu primele 5 orașe găsite,
# cu distanța mai mică de 300km

close_cities = []
for city, distance in cities:
    if distance < 300:
        close_cities.append(city)
        
        if len(close_cities) == 5:
            break
print(close_cities)

# rescriem folosind continue
close_cities = []
for city, distance in cities:
    if distance >= 300:
        # we are not interested
        continue # so doing early exit

    close_cities.append(city)
        
    if len(close_cities) == 5:
        break
print(close_cities)

# dată fiind lista cities de mai sus
# creați o listă nouă first_cities
# ce conține primele 5 elemente din lista inițială.
#
# folosiți while pentru asta

# # iterația cu while:
# while condition:
#    do_something()
#    if ...:
#       break
first_cities = []

idx = 0
while idx < 5:
    first_cities.append(cities[idx])
    idx += 1
print(first_cities)



# dată fiind lista cities creați o listă
# a orașelor cu distanța mai mică de 300km,
# în timp ce eliberați memoria de elementele
# din lista inițială.
#
# a) folosiți while pentru asta;
# b) țineți cont că lista goală în context boolean
#    este False;
# c) folosim pop pe lista inițială.

close_cities = []
while cities:
    city = cities.pop()
    close_cities.append(city)

# scrieți o funcție
def wait(seconds):
    pass

# ce așteaptă numărul dat de secunde
# și la fiecare secundă face print
# cu stringul "waiting..."
#
# implementați o versiune cu while
# și o versiune cu for.

from time import sleep

def wait(seconds):
    counter = 0
    while counter < seconds:
        print("waiting...")
        sleep(1)
        counter += 1

def wait(seconds):
    while seconds > 0:
        print("waiting...", seconds)
        sleep(1)
        seconds -= 1
wait(5)

def wait(seconds):
    for s in range(seconds, 0, -1):
        print("waiting...", s)
        sleep(1)
wait(3)
