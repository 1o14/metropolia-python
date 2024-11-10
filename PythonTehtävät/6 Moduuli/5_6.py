def karsi_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu_lista = karsi_parittomat(alkuperainen_lista)

print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", karsittu_lista)
