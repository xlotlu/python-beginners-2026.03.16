# Modificați funcția grep() de ieri pentru a returna
# o listă de linii, în loc de a face print

def grep(fname, word, encoding="utf-8"):
    result = []
    with open(fname, encoding=encoding) as fp:
        for line in fp:
            if word in line:
                line = line.removesuffix("\n")
                result.append(line)
    return result


# Scrieți o funcție
def writeinto(filename, content, overwrite=False, encoding="utf-8"):
    pass
# care scrie în fișierul `filename` string-ul `content`,
# refuzând să înlocuiască fișierul dacă `overwrite` = False.

def writeinto(filename, content, overwrite=False, encoding="utf-8"):
    mode = "w" if overwrite else "x"

    with open(filename, mode, encoding=encoding) as fp:
        fp.write(content)

try:
    writeinto("test.txt", open.__doc__)
except FileExistsError:
    print("Fișierul există deja")


# Scrieți o funcție
def count_str(filename, str, insensitive=True):
    pass
# ce numără aparițiile lui `str` în fișierul `filename`.
#
# implementați 2 variante:
# - una în care citiți tot conținutul în memorie,

def count_str(filename, str, insensitive=True):
    with open(filename) as f:
        content = f.read()
        if insensitive:
            content = content.casefold()
            str = str.casefold()
        return content.count(str)

# - și alta în care iterați linie cu linie.
def count_str(filename, str, insensitive=True):
    if insensitive:
        str = str.casefold()

    count = 0
    with open(filename) as f:
        for line in f:
            if insensitive:
                line = line.casefold()
            count += line.count(str)

    return count

#
# testați-o pe fișierul 'it-was.txt'.
count_str("data/it-was.txt", "it", insensitive=False)
count_str("data/it-was.txt", "WAS")


# [Opțional] Scrieți o funcție
def count_word(filename, word, insensitive=True):
    pass
# ce numără aparițiile cuvântului `word` în fișierul `filename`.

import string
_TRANSLATION = str.maketrans(
    string.punctuation,
    " " * len(string.punctuation)
)
def count_word(filename, word, insensitive=True):
    if insensitive:
        word = word.casefold()

    with open(filename) as f:
        content = f.read()
        if insensitive:
            content = content.casefold()

        # we replace all non-word characters
        # with spaces
        content = content.translate(_TRANSLATION)
        # we split the content by spaces
        words = content.split()

        return words.count(word)