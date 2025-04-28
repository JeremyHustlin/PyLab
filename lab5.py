import re  # pentru validarea denumirilor cu expresii regulate

# Lista globală de cumpărături
shopping_list = []

# Funcție pentru afișarea listei curente
def show_list():
    if not shopping_list:
        print("Lista este goală.")
    else:
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")

# Funcție pentru adăugarea unui produs în listă
def add_item():
    product = input("Introduceți denumirea produsului: ").strip()

    # Validare cu expresii regulate: doar litere + spații unice între cuvinte
    if not re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', product):
        print("Denumirea este invalidă! Se acceptă doar litere și spațiu între cuvinte.")
        return

    # Verificare dacă produsul există deja (ignorând majuscule/minuscule)
    if product.lower() in [p.lower() for p in shopping_list]:
        print("Produsul deja există în listă.")
    else:
        shopping_list.append(product)
        print("Produs adăugat cu succes.")

# Funcție pentru ștergerea unui produs din listă
def delete_item():
    metoda = input("Doriți să ștergeți după (1) poziție sau (2) denumire?: ").strip()

    if metoda == "1":
        try:
            index = int(input("Introduceți poziția produsului (de la 1 în sus): "))
            if index < 1 or index > len(shopping_list):
                print("Poziție invalidă.")
            else:
                removed = shopping_list.pop(index - 1)
                print(f"Produsul '{removed}' a fost șters.")
        except ValueError:
            print("Introduceți un număr valid.")
    elif metoda == "2":
        name = input("Introduceți denumirea produsului de șters: ").strip().lower()
        for item in shopping_list:
            if item.lower() == name:
                shopping_list.remove(item)
                print(f"Produsul '{item}' a fost șters.")
                return
        print("Produsul nu a fost găsit în listă.")
    else:
        print("Opțiune invalidă pentru ștergere.")

# Meniul principal care rulează într-un ciclu până la alegerea opțiunii 4
def menu():
    while True:
        print("\nAlegeți o opțiune:")
        print("1 - Afișare listă")
        print("2 - Adăugare produs")
        print("3 - Ștergere produs")
        print("4 - Ieșire")

        opt = input("Introduceți opțiunea (1-4): ").strip()

        if opt == "1":
            show_list()
        elif opt == "2":
            add_item()
        elif opt == "3":
            delete_item()
        elif opt == "4":
            print("Program încheiat.")
            break
        else:
            print("Opțiune invalidă. Încercați din nou.")

# Apelare funcție principală
menu()
