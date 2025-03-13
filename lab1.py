# Sarcina 1
sarcina = "Sarcina 1"
print(sarcina)
# Cerința 1: Afișarea unui mesaj de salut
nume = input("Introduceți numele dvs.: ")
print("Salut, " + nume + "! Bine ai venit la laborator.")

# Cerința 2: Definirea variabilelor
numar_intreg = 42
numar_real = 3.14
text_scurt = "Python"
text_lung = """Acesta este un text care
ocupă mai multe rânduri
pentru a exemplifica variabilele text."""

# Cerința 3: Afișarea tipului a două variabile
tip_intreg = type(numar_intreg)
tip_ID = id(nume)
tip_text = type(text_scurt)
print("Tipul variabilei numar_intreg:", tip_intreg)
print("Tipul variabilei text_scurt:", tip_text)
print("Tipul variabilei tip_ID:", tip_ID)


# Cerința 4: Afișarea lungimii unui șir de text
lungime_text = len(text_scurt)
print("Lungimea textului scurt este:", lungime_text)

# Cerința 5: Transformarea textului în litere mari
text_mare = text_scurt.upper()
print("Text în litere mari:", text_mare)

# Cerința 6: Tăierea unui subșir
taiere_text = text_scurt[1:4]
print("Subșir extras:", taiere_text)

# Cerința 7: Afișarea unui mesaj formatat
print("Variabilă întreagă: {}, variabilă reală: {:.2f}".format(numar_intreg, numar_real))
print(f"Text scurt: {text_scurt}, Text lung: {text_lung}")

# Sarcina 2
print("#"*50)
sarcina2 = "Sarcina 2"
print(sarcina2)
# a)
txt = "More results from text..."
substr = txt[4:12]
print(substr)
print(substr.strip()) 
# b)
txt = "More results from text..."
print(txt.split())
# c)
age = 36
txt = "My name is Mary, and I am {}"
print(txt.format(age))

