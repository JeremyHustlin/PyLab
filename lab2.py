# Sarcina 1
sarcina = "Sarcina 1"
print(sarcina)
# Definirea unei liste
lista = [10, 20, 30, 40, 50]
print("Prima valoare:", lista[0])
print("A treia valoare:", lista[2])

# Înlocuirea unei valori
lista[1] = 25
print("Lista după modificare:", lista)

# Tăietură de elemente
sub_lista = lista[1:4]
print("Sub-listă extrasă:", sub_lista)

# Aplicarea unor metode, funcții și operatori
lista.append(60)  # Metoda append()
print("Lista după append:", lista)

lungime_lista = len(lista)  # Funcția len()
print("Lungimea listei:", lungime_lista)

suma_elemente = sum(lista)  # Funcția sum()
print("Suma elementelor listei:", suma_elemente)

print("Verificare apartenență (operator 'in'):", 30 in lista)
print("Concatenare liste (operator '+'):", lista + [70, 80])
print("Repetiție listă (operator '*'):", lista * 2)

# Definirea unui tuplu
tuplu = (100, 200, 300, 400, 500)
print("Tipul variabilei tuplu:", type(tuplu))
print("Prima valoare din tuplu:", tuplu[0])
print("Ultima valoare din tuplu:", tuplu[-1])

# Tăietură de elemente din tuplu
sub_tuplu = tuplu[1:4]
print("Sub-tuplu extras:", sub_tuplu)

# Aplicarea unor funcții asupra tuplului
print("Numărul de apariții ale lui 200 în tuplu:", tuplu.count(200))
print("Indexul valorii 300 în tuplu:", tuplu.index(300))
print("Lungimea tuplului:", len(tuplu))

# Definirea unui set
multime = {1, 2, 3, 3, 4, 5, 5}
print("Elementele mulțimii:", multime)  # Elimină duplicatele

# Aplicarea unei metode și unei funcții
multime.add(6)  # Metoda add()
print("Mulțimea după adăugare:", multime)

print("Lungimea mulțimii:", len(multime))  # Funcția len()

# Definirea unui dicționar cu chei text și numerice
dict_text = {"nume": "Alex", "varsta": 25, "oras": "Chisinau"}
dict_numeric = {1: "unu", 2: "doi", 3: "trei"}

# Accesarea elementelor
print("Nume din dicționar:", dict_text["nume"])
print("Valoarea cheii 2 în dicționar numeric:", dict_numeric[2])

# Aplicarea unor metode și funcții
dict_text.update({"profesie": "inginer"})  # Metoda update()
print("Dicționar actualizat:", dict_text)

dict_numeric.pop(1)  # Metoda pop()
print("Dicționar numeric după eliminare:", dict_numeric)

print("Cheile dicționarului text:", dict_text.keys())  # Funcția keys()
print("Valorile dicționarului text:", dict_text.values())  # Funcția values()

# Conversia unui tip de date
lista_to_tuplu = tuple(lista)  # Conversie listă -> tuplu
print("Lista convertită în tuplu:", lista_to_tuplu)

dict_to_list = list(dict_text.items())  # Conversie dicționar -> listă de tupluri
print("Dicționar convertit în listă:", dict_to_list)

# Explicație: Conversia este utilă pentru protejarea datelor (ex. listă -> tuplu) sau manipulare ușoară (ex. dicționar -> listă de tupluri pentru iterare).

# Sarcina 2
print("#"*50)
sarcina2 = "Sarcina 2"
print(sarcina2)
# Definirea listelor
preturi = [100, 250, 75]
produse = ["Laptop", "Telefon", "Mouse"]

# Afișarea informațiilor despre produse și prețuri
print("Lista produse și prețuri:")
for i in range(len(produse)):
    print("Produs: {} - Preț: {} EUR".format(produse[i], preturi[i]))

# Solicitarea vârstei utilizatorului
varsta = int(input("Introduceți vârsta dvs.: "))
varsta_viitoare = varsta + 5

# Afișarea rezultatului
print("În 5 ani veți avea " + str(varsta_viitoare) + " ani.")

# Utilizarea operatorului 'in' și 'not in'
element = "Laptop"
if element in produse:
    print(element, "se află în lista de produse.")
else:
    print(element, "nu se află în lista de produse.")

nr_verificare = 500
if nr_verificare not in preturi:
    print(nr_verificare, "nu se află în lista de prețuri.")
