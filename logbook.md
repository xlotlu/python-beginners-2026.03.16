# Concepte:

reprezentare a unei variabile = ce scrie programatorul
vs.
output = ce așteaptă operatorul uman

---

# data types:

 int
 float
 str
 bool
 list

sequences: str, list, tuple.
  - accesibile după index
  - au metodele .count() și .index()
  - sunt iterabile
  - suportă operatorul `in`


---

# !de citit o dată!

Styleguide (PEP-8)
https://peps.python.org/pep-0008/

Documentație basic datatypes
https://docs.python.org/3/library/stdtypes.html

String formatting
https://docs.python.org/3/library/string.html#formatstrings


---

string: "un string"
 --> reprezentare: 'un string'
string: 'un string'
 --> reprezentare: 'un string'

string: "un ' string"
 --> reprezentare: "un ' string"

string: "un ' string \" mai special"
 --> reprezentare: un \' string " mai special'


---

variabila: un simbol care pointează către ceva stocat în memorie

poate conține caractere alfanumerice și underscore. nu poate începe cu număr.

---

# operatori:

 matematici, noi:
   **  ridicare la putere
   //  partea întreagă a împărțirii
   %   restul împărțirii

 == testează egalitate
 <
 >
 <=
 >=

 is testează că avem de-a face cu același obiect


 boolean:
   or
   and
   not
   in

---

# concepte fundamentale

mutabilitate

în Python totul este un obiect
  adică: are atribute (o proprietate atașată obiectului) și metode (funcții atașate obiectului)

în Python totul este o referință

---

# funcția:

 - scopul său este reutilizarea de logică aplicată unui input, și returnarea unui output
 - primește argumente separate de virgulă
 - poate returna un rezultat
 - poate avea side-effects (output în consolă, scriere pe disc, scriere în rețea etc.)

argumentele sunt de obicei de un număr dat
argumentele pot fi și nelimitate
argumentele pot avea valori default

---

# debugging essentials:

print()
help()
type()

---

# str: metode uzuale

split()

upper() / lower()
count()
find() / index()
startswith() / endswith()

split()

replace()
strip()

format()


!? join()

---

# Important exception types

SyntaxError
NameError # când nu există o variabilă
TypeError # în mai multe situații: argumente improprii la chemarea funcției
IndexError
ValueError # apare în mai multe situații
KeyError  # când dicționarul nu are cheia

---

# Installing packages

pip install ipython
pip install openpyxl
# dacă faceți heavy writing cu scriere de fișiere excel, instalați și
pip install lxml

---

# Utilizat VSCode:

Ctrl+/      (un)comment selection
Ctrl+F5     run python program
Shift+Enter execute selection in python shell


---

# Utilizat ipython

# dacă vreți autoreload la development
%load_ext autoreload
%autoreload 2

---

# Essential Wisdom:

There are 2 really complicated problems in computing:
- naming things
- cache invalidation
- off-by-one errors

OCD = obsessive-compulsive disorder

RTFM = read the f... manual
STFW = search the effing web

PEBKAC = problem exists between computer and chair
"user error, replace user and press any key"


https://www.youtube.com/watch?v=Cbk980jV7Ao [Validation]

https://marshallbrain.com/manna1 [Manna, short novel]


>>> import this