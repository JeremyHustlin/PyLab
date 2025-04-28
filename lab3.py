# Lucrarea de laborator Nr. 3 – Programarea jocurilor în Python

# Scopul acestei lucrări este de a înțelege funcțiile lambda, sortarea avansată a datelor,
# definirea și utilizarea funcțiilor cu diferite tipuri de parametri și returnări.

# ----------------------
# Sarcina 1: Funcție lambda simplă
# ----------------------

# Se definește o funcție lambda care primește un nume și afișează un mesaj de salut.
# Lambda este o funcție anonimă, adică nu este definită cu 'def', ci cu cuvântul 'lambda'.
greet_user = lambda name: print("Hello My Dear,", name)

# Solicităm utilizatorului să introducă numele său
user_name = input("What is your name? ")

# Apelăm funcția lambda cu numele introdus
greet_user(user_name)

# ----------------------
# Sarcina 2: Sortarea unei liste de tupluri
# ----------------------

print("\n" + "#"*50)
print("Sarcina 2 – Sortarea tuplurilor")

# Definim o listă formată din 7 tupluri, fiecare având două elemente (numere întregi)
lista_tupluri = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15), (5, 2), (9, 45)]

# Sortăm lista după al doilea element al fiecărui tuplu
# Funcția 'sorted' primește un parametru 'key', căruia îi atribuim o funcție lambda
lista_sortata = sorted(lista_tupluri, key=lambda x: x[1])

# Afișăm lista sortată
print("Lista sortată după al doilea element:", lista_sortata)

# ----------------------
# Sarcina 3: Funcție lambda proprie
# ----------------------

print("\n" + "#"*50)
print("Sarcina 3 – Funcție lambda proprie")

# Definim o funcție lambda care calculează pătratul unui număr
# Este un exemplu de funcție simplă, ideală pentru utilizare rapidă
patrat = lambda x: x * x

# Afișăm rezultatul apelării funcției
print("Pătratul lui 6 este:", patrat(6))

# Explicație:
# Lambda poate fi folosită pentru a crea funcții scurte, fără a fi necesară o definiție completă cu 'def'.

# ----------------------
# Sarcina 4: Definirea diferitelor tipuri de funcții
# ----------------------

print("\n" + "#"*50)
print("Sarcina 4 – Tipuri de funcții")

# Funcție fără parametri și fără return
def salut():
    print("Salut! Aceasta este o funcție simplă fără parametri.")

# Funcție cu parametri și return
def aduna(a, b):
    return a + b

# Funcție cu parametri și valori implicite (default)
def descriere_joc(nume="Mario", gen="Aventura"):
    print(f"Jocul {nume} este de tip {gen}.")

# Apelăm fiecare funcție definită mai sus
salut()  # apel simplu
suma = aduna(5, 10)
print("Suma dintre 5 și 10 este:", suma)

# Apel cu parametri impliciți
descriere_joc()
# Apel cu alți parametri
descriere_joc("FIFA", "Sport")

# Explicații finale:
# - Funcțiile fără parametri sunt utile pentru mesaje generale.
# - Funcțiile cu return oferă rezultate ce pot fi folosite în alte calcule.
# - Parametrii cu valori implicite fac funcțiile mai flexibile și mai ușor de utilizat.
