import random

broj = random.randint(1, 10)

player_name = input("Zdravo, vase ime je? ")
pokusaji = 0
print("okay! " + player_name + "Pogadjajte broj od 1 do 10:")

while pokusaji < 5:
    pokusaj2 = int(input("unesite neki broj: "))
    pokusaji += 1
    if pokusaj2 < broj:
        print("Pokusaj vam je mali, pokusajte ponovo!")
    if pokusaj2 > broj:
        print("Pokusaj vam je visok, pokusajte ponovo!")
    if pokusaj2 == broj:
        break
if pokusaj2 == broj:
    print("Pogodili ste broj " + str(pokusaj2) + " pokusaja!")
else:
    print("Niste pogodili broj, vas broj je bio " + str(broj))
