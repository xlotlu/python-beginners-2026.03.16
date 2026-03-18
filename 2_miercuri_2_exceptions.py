try:
    cod 
except:
    # catch-all
    alt_cod

# ^^ nu vrem să facem asta, ascunde orice eroare

try:
    cod # preferabil cât mai limitat
        # și mai specific
except IndexError: # exact excepția pe care o targhetați
    alt_cod


lst = [1, 2, 3]

try:
    v = lst[5]
except IndexError:
    v = None


try:
    cod 
except ExceptionType1:
    ceva
except ExceptionType2:
    altceva
# ...

try:
    cod 
except ExceptionType1:
    ceva
else:
    altceva # care merge doar în cazul în care totul a fost ok


try:
    cod 
except:
    handle_it()
finally:
    cleanup() # cod care se rulează întotdeauna


try:
    cod 
except:
    handle_it()
else:
    ok_code()
finally:
    cleanup()