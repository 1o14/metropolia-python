luvut = []  # Lista lukujen tallentamiseen

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":  # Lopetetaan, jos syöte on tyhjä
        break

    luvut.append(int(syote))  # Lisätään syöte listaan kokonaislukuna

if luvut:  # Jos listassa on lukuja
    print("Pienin luku on", min(luvut))
    print("Suurin luku on", max(luvut))
else:
    print("Et syöttänyt yhtään lukua.")
