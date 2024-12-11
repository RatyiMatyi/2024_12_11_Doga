"""1. Volt-e 6-os a dobások között?
2. Hányadikra sikerült először 18-nál nagyobbat dobni?
3. Hány darab 1-est dobtak?
4. Melyik volt a legnagyobb dobás a 10-nél kisebbek közül, és hányadik dobás volt?
5. Mennyi a 4-es dobások szorzata?"""

import random

random_numbers = [random.randint(1, 20) for _ in range(100)]

print(random_numbers)

print("1. feladat")
if 6 in random_numbers:
    print("Van 6-os a dobások között.")
else:
    print("Nincs 6-os a dobások között")

print("2. feladat")
tizen_nyolc_plusz = [i for i, num in enumerate(random_numbers) if num > 18]
elso = tizen_nyolc_plusz[0]
print(f"{elso} dobás kellet az első 18-nál nagyob szám kidobásához.")

print("3. feladat")
egyesek = random_numbers.count(1)
print(f"Ennyi 1-est dobtál: {egyesek}")

print("4. feladat")

tizminusz = [i for i in random_numbers if i < 10]
legnagyobb = max(tizminusz)
print(f"A legnagyobb 10-nél kisebb szám: {legnagyobb}")

print("5. feladat")

negy_szorzat = 1
for i in random_numbers:
    if i == 4:
        negy_szorzat *= 4

print(f"A négyesek szorzata: {negy_szorzat}")