import random

#Luodaan kolmenumeroinen koodi
kolmenumeroinen_koodi = ""
for _ in range(3):
    kolmenumeroinen_koodi += str(random.randint(0, 9))

#Luodaan nelinumeroinen koodi
nelinumeroinen_koodi = ""
for _ in range(4):
    nelinumeroinen_koodi += str(random.randint(1,6))

print("Kolmenumeroinen koodi:", kolmenumeroinen_koodi)
print("Nelinumeroinen_koodi:", nelinumeroinen_koodi)