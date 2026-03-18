# NOTE:
# 
# - pe windows, când scrieți o cale de mână,
#   probabil veți vrea să folosiți r'raw string'
# - default este modul t (text) (se ocupă singur de encoding/decoding)
# - default este modul r (read)
# - modul 'w' trunchează fișierul!!
# - modul 'x' evită suprascrierea
#
# - .read() în mod repetat nu returnează content-ul
#   odată citit
# - un file pointer este iterabil. de obicei
#   nu vrem să facem .read()
#
# - vrem să folosim (mai tot timpul) context manager



# the very basics: reading through the file.
fp = open('/tmp/test.txt', encoding="utf-8")

for line in fp:
    line = line.removesuffix("\n")
    print("»", line)


# Exercițiu:
# scrieți o funcție
def grep(fname, word):
    pass
# ce printează liniile din fișierul "fname"
# ce conțin cuvântul "word"

def grep(fname, word):
    fp = open(fname, encoding="utf-8")

    for line in fp:
        if word in line:
            line = line.removesuffix("\n")
            print(line)

grep("/tmp/test.txt", "nou")

# modificați funcția pentru a putea seta encoding-ul,
# dar să fie default "utf-8"


def grep(fname, word, encoding="utf-8"):
    fp = open(fname, encoding=encoding)

    for line in fp:
        if word in line:
            line = line.removesuffix("\n")
            print(line)



# Exercițiu:
# scrieți conținutul docstring-ului funcției open
# (pe care îl accesați cu open.__doc__ )
# într-un fișier numit "open_docs.txt"
content = open.__doc__
fp = open("open_docs.txt", 'w')
fp.write(content)
fp.close()

# rescris cu context-manager:
with open("open_docs.txt", 'w') as fp:
    content = open.__doc__
    fp.write(content)


# Exercițiu:
# rescrieți funcția grep de mai sus
# folosind context manager
def grep(fname, word, encoding="utf-8"):
    with open(fname, encoding=encoding) as fp:
        for line in fp:
            if word in line:
                line = line.removesuffix("\n")
                print(line)

# Exercițiu:
# scrieți o funcție
def grepinto(fin, fout, word, encoding="utf-8"):
    pass
# ce caută "word" în fișierul "fin", și scrie
# fiecare linie găsită în fișierul "fout"

def grepinto(fin, fout, word, encoding="utf-8"):
    # with (
    #     open(fin, encoding=encoding) as fpin,
    #     open(fout, 'w', encoding=encoding) as fpout
    # ):
    with open(fin, encoding=encoding) as fpin, \
         open(fout, 'w', encoding=encoding) as fpout:
            # scriu dintr-o parte în alta
            for line in fpin:
                if word in line:
                    fpout.write(line)

# Exercițiu:
# scrieți o funcție
def cp(fin, fout, overwrite=False):
    pass
# ce copiază fișierul "fin" în locația "fout"

def cp(fin, fout, overwrite=False):
    mode = 'wb' if overwrite else 'xb'
    with open(fin, 'rb') as file_in, \
         open(fout, mode) as file_out:

        # varianta urâtă ce ocupă memoria
        #file_out.write(file_in.read())

        # varianta mai puțin urâtă
        # dar fără sens / fără control
        # pentru că nu știm cum se iterează un fișier binar
        for line in file_in:
            file_out.write(line)

# [OPȚIONAL] Temă pentru acasă:
# Faceți citirea și scrierea "chunked".
def cp(fin, fout, overwrite=False, chunk=4096):
    pass