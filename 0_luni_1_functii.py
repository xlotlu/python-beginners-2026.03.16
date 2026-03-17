# Exercițiu:
# scrieți o funcție ce returnează string-ul corect
# pentru momentul curent al zilei

import datetime

#hour = datetime.datetime.now().hour # NU AICI!

def get_greeting():
    hour = datetime.datetime.now().hour

    if 5 <= hour < 10:
        return "buna dimineata"
    elif 10 <= hour < 18:
        return "buna ziua"
    elif 18 <= hour < 22:
        return "buna seara"
    else:
        return "noapte buna"

print(get_greeting())


# Exercițiu:
# scrieți o funcție

def greet_user():
    pass
# care cere numele utilizatorului,
# și face print cu salutul potrivit momentului zilei
# și numele său.
# Folosiți funcția anterioară get_greeting().


def greet_user():
    # 1. aflu numele
    # 2. aflu momentul zilei
    # 3. fac output cu combinația lor
    name = input("Introduceti numele: ")
    greeting = get_greeting()
    print(greeting + " " + name)

greet_user()


## String formatting:
#
# email_template = """
# Salut {nume},
 
# Te anunțăm că la data {date}
# trebuie să returnezi {sum} lei.
# """
# print(email_template.format(nume="Gigel", date=datetime.date.today(), sum=2022.54))


# Exercițiu:
# scrieți o funcție
def get_diff(v1, v2):
    pass
# ce returnează diferența dintre argumentele date
# ca număr pozitiv

def get_diff(v1, v2):
    if v1 > v2:
        return v1 - v2
    else:
        return v2 - v1


# Exercițiu:
# promptați utilizatorul pentru vârsta sa
# și pentru vârsta prietenului său.
# faceți output-ul corect după caz astfel:
# - "ești mai în vârstă cu <x> ani decât prietenul tău"
# - "prietenul tău este mai în vârstă cu <x> ani decât tine"
# - "tu și prietenul tău aveți aceeași vârstă"
#
# folosiți metoda .format()

def prompt_for_age():
    age1 = input("Vârsta ta? ")
    age2 = input("Vârsta prietenului tău? ")

    age1 = int(age1)
    age2 = int(age2)

    diff = get_diff(age1, age2)

    if age1 > age2:
        print(
            "ești mai în vârstă cu {} ani decât prietenul tău".format(diff)
        )
    elif age2 > age1:
        print(
            "prietenul tău este mai în vârstă cu {} ani decât tine".format(diff)
        )
    else:
        # ages are equal
        print("tu și prietenul tău aveți aceeași vârstă")

prompt_for_age()

## implementare alternativă, cerând și numele:

def prompt_for_age_with_name():
    # luăm datele de la utilizator
    name1 = input("First person's name: ")
    age1 = input("First person's age: ")
    age1 = int(age1)

    name2 = input("Second person's name: ")
    age2 = input("Second person's age: ")
    age2 = int(age2)

    # aflăm diferența lor de vârstă
    diff = get_diff(age1, age2)
    
    # dacă au aceeași vârstă fac output la un mesaj
    if diff == 0:
        print ("{person1} și {person2} au aceeași vârstă".format(person1=name1, person2=name2))
    else:
        # altfel, mesaj comun pentru ambele situații
        msg = "{person1} este mai în vârstă decât {person2} cu {diff} ani"

        if age1 > age2:
            print(msg.format(person1=name1, person2=name2, diff=diff))
        else:
            print(msg.format(person1=name2, person2=name1, diff=diff))

prompt_for_age_with_name()