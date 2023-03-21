pytania = ["Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:", "W jakich okolicznościach czytasz książki najczęściej?", "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?"]
odp1 = ["oglądanie telewizji/filmów/seriali", "czytanie książek/czasopism", "słuchanie muzyki"]
odp2 = ["podczas podróży", "w czasie wolnym (po pracy, na urlopie)", "podczas pracy/nauki (to ich element)"]
odp3 = ["chęć poszerzenia wiedzy", "czytanie mnie relaksuje/odpręża", "fakt, że czytanie jest modne"]
flag = True

print("Pytanie: " + pytania[0] + "\n")
for x in odp1:
    print("Odpowiedź: " + x + "\n")


while flag:
    odp = input("podaj odpowiedćź")
    for x in odp1:
        if x == odp:
            flag = False
flag = True

print("Pytanie: " + pytania[1] + "\n")
for x in odp2:
    print("Odpowiedź: " + x + "\n")


while flag:
    odp = input("podaj odpowiedćź")
    for x in odp2:
        if x == odp:
            flag = False
flag = True

print("Pytanie: " + pytania[2] + "\n")
for x in odp3:
    print("Odpowiedź: " + x + "\n")


while flag:
    odp = input("podaj odpowiedćź")
    for x in odp3:
        if x == odp:
            flag = False
flag = True

