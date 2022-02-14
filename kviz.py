print("Dobrodosli u nas kviz znanja!")

igranje = input("Da li zelite da igrate? ")

if igranje.lower() != "da":
    quit()


print("Hajde da se igramo! :)")

rezultat = 0

pitanje = input("Koji programski jezik ucite? ")
if pitanje.lower() == "python":
    print("Vas odgovor je tacan!")
    rezultat +=1
else:
    print("Vas odgovor je netacan :(")

pitanje = input("Koliko je 2*(2+2) ")
if pitanje == "8":
    print("Vas odgovor je tacan!")
    rezultat +=1
else:
    print("Vas odgovor je netacan :(")

pitanje = input("Koji je glavni grad Turske? ")
if pitanje.lower() == "ankara":
    print("Vas odgovor je tacan!")
    rezultat +=1
else:
    print("Vas odgovor je netacan :(")

pitanje = input("Koji je sluzbeni naziv SAD ")
if pitanje.lower() == "sjedinjene americke drzave":
    print("Vas odgovor je tacan!")
    rezultat +=1
else:
    print("Vas odgovor je netacan :(")

print("Imate" + str(rezultat))
print("Uradili ste" +str((rezultat/4)*100) +"%")

