# Kysytään käyttäjältä hyttiluokka
luokka = input("Anna hyttiluokka (LUX, A, B, C): ").upper()

# Tarkistetaan hyttiluokka ja annetaan kuvaus
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")
