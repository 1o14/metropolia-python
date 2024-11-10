# Kysytään käyttäjän sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna sukupuolesi (mies/nainen): ").lower()
hemoglobiini = int(input("Anna hemoglobiiniarvosi (g/l): "))

# Tarkistetaan sukupuoli ja arvioidaan hemoglobiiniarvo
if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif hemoglobiini <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")
else:
    print("Virheellinen sukupuoli.")
