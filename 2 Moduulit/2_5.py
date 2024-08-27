leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

leiviska_nauloina = 20
naula_luoteina = 32
luoti_grammoina = 13.3

#Laskee massan grammoina
massa_grammoina = (
    leiviskat * leiviska_nauloina * naula_luoteina * luoti_grammoina +
    naulat * naula_luoteina * luoti_grammoina +
    luodit * luoti_grammoina
)

#Muuntaa massan kilogrammoiksi ja grammoiksi
kilogrammat = massa_grammoina // 1000
grammat = massa_grammoina % 1000

print("Massa nykymittojen mukaan: {} kilogrammaa ja {:.2f} grammaa.".format(kilogrammat, grammat))