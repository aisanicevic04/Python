def ubistvo(osumnjiceni):
    print(osumnjiceni)


print("Dobrodosli u igru ubistva!")

print("Vi ste detektiv i radite na ubistvu jednog velikog bogatsa.")
print("Osumnjiceni su:batler,sef,bastovan i sin")
print("Budite pametni")

print("Batler kaze:Pospremao sam dnevnu sobu dok se ubistvo dogodilo.")
print("Batler kaze:Ja bih rekao da je bastovan cudno se ponasa")

detektiv = input(
    "Cuvsi batlera,mozes da kazes ko je kriv ili mozes da cujes sledeceg osumnjicenog?"
)
osumnjiceni = ("batler", "sef", "bastovan", "sin")

if (
    detektiv == "batler"
    or detektiv == "sef"
    or detektiv == "bastovan"
    or detektiv == "sin"
):
    print("Zao mi je,ali vas osumnjiceni nije ubica")
    quit()
elif detektiv == "sledeci":
    print("U redu onda,sledeceg koga cete preispitati jeste kuhinjski sef")

    print("Sef kaze:Ja sam bio sve vreme u kuhinji,pripremao sam bogatasu rucak.")
    print("Sef kaze:Odjednom cuo sam vrisak napolju.")

detektiv = input(
    "Cuvsi sefa,mozes da biras koje ubica ili da ides na sledeceg osumnjicenog:"
)

if detektiv == osumnjiceni:
    print("Zao mi je,ali vas osumnjiceni nije ubica")
    quit()
elif detektiv == "sledeci":
    print("U redu onda,sledeceg koga cete preispitati jeste bogatasev sin")

    print("Sin kaze:Ja sam se kupao u bazenu a moj otac je setao bastom.")
    print("Sin kaze:Odjednom cuo sam jak vrisak.")
    print("Sin kaze:Kada sam pogledao mogao sam videti bastovana.")
    print("Sin kaze:Drzao je makaze i stajao je pored tela.")
    print("Sin kaze:Mislim da ga je on ubio.")

detektiv = input(
    "Sada si siguran da je bastovan ubio bogatasa,ali se jos dvoumis da li da ga saslusas ili da kazes da je on ubica?"
)

if detektiv == "ne":
    print(
        "Odlucio si da bez saslusanja odes kod sudije i kazes mu da si pronasao krivca."
    )
    print("Sudija ti je poverovao i uhapsio je bastovana.")
    print(
        "Nakon nekog vremena saznajes da bastovan uopste nije kriv i da si optuzio nevinog coveka"
    )
    quit()
elif detektiv == "da":
    print("Odlucio si da svejedno saslusas bastovana i da cujes njegov deo price.")

    print("Bastovan kaze:Uopste ga nisam ubio!")
    print("Bastovan kaze:Samo sam tu prolazio i video sam njega kako lezi po travi")
    print("Bastovan kaze:Onda me je njegov sin optuzio da sam ga ja ubio")
    print("Bastovan kaze:Ali ja znam pravu istinu.")
    print("Bastovan kaze:Mogu da ti pokazem nakon tvog posla.")
    print("Bastovan kaze:Nadjimo se kod bogataseve vile.")

detektiv = input(
    "Bastovanova prica ti izgleda veoma izmisljeno i razmisljas da ga odmah stavis u zatvor,ali isto si radoznao zbog njegove ponude,ko zna sta moze da ti pokaze:"
)

if detektiv == "da":
    print("Odlucio si da ga stavis u zatvor,to je bila jedina bezbedna opcija.")
    print("Dok su ga vodili u zatvor on ti sapnu")
    print("Napravio si kardinalnu gresku.")
    quit()
elif detektiv == "ne":
    print("Radoznalost te je obuzela i morao si videti sta ce ti pokazati.")

    print("NAKON POSLA")

    print("Bastovan kaze:Stigao si,mislio sam da si zaboravio na mene.")
    print("Bastovan kaze:Dodji pokazacu ti nesto")

    print("Pratio si bastovana do njegove supe gde drzi svoj alat.")
    print("Usao si veoma tiho i tamo sto si video bilo je zastrasujue.")
    print(
        "Tamo je bio bogatas,ziv i zdrav,kako je uperio pistolj prema tebi i bastovan te hvata sa ledja"
    )

    print("Bogatas kaze:Konacno,dobicu osvetu koju sam oduvek zeleo.")

    print("Zbunjen,pitas ga ste desava a on ti rece")

    print("Bogatas kaze:Secas li se onog slucaja pre par godina?")
    print("Bogatas kaze:Ono kada je jedna zena ubila svog muza?")
    print(
        "Bogatas kaze:E pa ta zena je bila moja cerka a ti si je zatvorio dozivotno u zatvoru!"
    )
    print("Bogatas kaze:Od toga trenutka svaki dan se budim sa zeljom da te ubijem")
    print(
        "Bogatas kaze:Pa sam lazirao svoje ubistvo tako da bi te navukao da dodjes ovde"
    )
    print("Bogatas kaze:Sada cu imati osvetu koju sam veoma dugo cekao!")

detektiv = input(
    "Sada su ti ostale samo dve opcije:a)Da ostanes miran i da se suocis sa sudbinom ili b)Da pokusas da pobegnes:"
)

if detektiv == "b":
    print("Pokusao si da pobegnes bastovanu")
    print("Ali te bogatas upuca pre nego sto si ista uradio.")
    quit()
elif detektiv == "a":
    print("Pomirio si se sa svojom sudbinom")
    print("Ali bas kad je trebao da te upuca")
    print("U supu ulete bogatasev sin sa policijom")
    print(
        "On ti rece da je sazno o planu njegovog oca i da je zvao policiju cim je video da si ti stigao."
    )
    print("I tako misterija je bila resena i bastovan i bogatas su bili uhapseni!")
    quit()

ubistvo()
