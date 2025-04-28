print("\n" + "#"*50)
print("Calculator: Vârsta pisicii în ani omenești\n")

raspuns = input("Pisica are sub un an? (Da/Nu): ").strip().lower()

# Cazul 1: Pisica are sub un an
if raspuns in ["da", "yes"]:
    # Dicționar bazat pe tabel
    varsta_pisic = {
        1: "6 luni",
        2: "10 luni",
        3: "2 ani",
        4: "5 ani",
        5: "8 ani",
        6: "14 ani",
        7: "15 ani",
        8: "16 ani",
        9: "16 ani",
        10: "17 ani",
        11: "17 ani"
    }

    while True:
        try:
            luni = int(input("Câte luni are pisicul tău? (1-11): "))
            if luni in varsta_pisic:
                print(f"Pisicul tău are echivalentul a {varsta_pisic[luni]} în ani omenești.")
                break
            else:
                print("Te rog să introduci un număr între 1 și 11.")
        except ValueError:
            print("Introdu date corecte, adică un număr întreg.")

# Cazul 2: Pisica are peste un an
elif raspuns in ["nu", "no"]:
    while True:
        try:
            ani = int(input("Câți ani are pisica? (1-34): "))
            if 1 <= ani < 35:
                if ani == 1:
                    echiv = 18
                elif ani == 2:
                    echiv = 25
                elif 3 <= ani <= 15:
                    echiv = 25 + (ani - 2) * 4
                else:
                    echiv = 25 + 13 * 4 + (ani - 15) * 3

                print(f"În ani omenești, pisica ta are aproximativ {echiv} ani.")
                break
            else:
                print("Introdu un număr între 1 și 34.")
        except ValueError:
            print("Introdu o valoare validă (număr întreg).")

else:
    print("Răspuns invalid. Scrie 'Da' sau 'Nu'.")
