print("DOBRO DOSAO U MOJ PYTHON PROJEKAT")
print("jednog dana dodje je neki beskucnik ispred kuce")
print("on pita da li moze da udje u tvoju kucu.Sta ces uraditi?")
print("1)pusti ga da udje ")
print("2)nemoj mu dozvoliti da udje")
a = input(">>>")
if a == "1":
    print("ti si ga pustio da udje")
    print("posle 5 minuta dodje policija i pita da li je u vasoj kuci beskucnik")
    print("sta ces da uradis?")
    print("1)kazes da beskucnik jeste u tvojoj kuci")
    print("2)lazes da nije u tvojoj kuci")
    b = input(">>>")
    if b == "1":
        print("ti si ga tuzio i beskucnjika su uphasili")
        print("zbog toga sto si reko istinu dala ti je policija 1000$")
        print("ti si otiso da kupis ps5 i vidis kako neki delklenti biju coveka")
        print("sta ces uraditi?")
        print("a)nista")
        print("b)pokusas da spasis tog coveka")
        p = input(">>>")
        if p == "a":
            print("ti nisi nista uradio i kupio ps5")
            print("posle ti deliklenti su videli da imas ps5")
            print("pa su te opljackali i ubili")
            quit()
        elif p == "b":
            print(
                "pokusao si da ga spasis tako sto si pre izlaska kuci poneo noz za svaki slucaj"
            )
            print(" dovojno dugo ste bili u sukobu da neko pozove policiju")
            print(
                "ti si bio veoma blizu smrti ali su uhapsili delikvente i dala ti je policija jos 1000000$ jer su delikventi deo mafie"
            )
        else:
            print("nauci da kucas slova")
            quit()
        print(
            "sutra dan neko kuca na tvoja vrata.Ti otvoris vrata i vidis da je vodja te mafije ispred tvoje kuce"
        )
        print(
            "on je bio zadivljen kako si uspeo da se oboris od njegovih najboljih borca"
        )
        print("on te pita da li hoces da se pridruzis njegovoj mafiji za 10 000$")
        print("sta ces uraditi?")
        print("1)da se pridruzis")
        print("2)da se ne pridruzis")
        y = input(">>>")
        if y == "1":
            print("uhapsila te policija jer je sve ovo bio plan da te uhapse")
            print(
                "oni su te navukli da radis sve za vece pare.Okupirana je bila policija i iskoristili su te da bi oni  imali vecu platu"
            )
            quit()
        elif y == "2":
            print("upuc an si")
            quit()
        else:
            print("pogledaj na tastaturi,videces brojeve 1 i 2 :)")
            quit()
    elif b == "2":
        print("policajci su usli u tvoju kucu i nasli beskucnika")
        print("i tebe i beskucnjika su uphasili")
        quit()
    else:
        print("ne znas da kucas, CAOOO")
        quit()
elif a == "2":
    print("on izvadi noz i pokusa da te ubije")
    print("pored tebe je pistolj. Sta ces uraditi")
    print("1)uzmes pistolj")
    print("2)pokusas da ga bijes")
    b = input(">>>")
    if b == "1":
        print("uzeo si pistolj ali ti trebalo predugo da ga repetiras i on te ubio")
        quit()
    if b == "2":
        print("oborio si ga i uzeo noz od njega")
        print("dosla je policija i dali ti 1000$ jer si pomogo policiji")
        print(
            "jer izgleda da je on bio kriminalac i policija je pokusala puno puta da ga uhvati"
        )
        print("ti posle ides da kupis ps5")
        print("dok cekas u liniji pocnu kriminalci da opljackaju tu prodavnicu")
        print("ti se sakrijes i ne znas sta da radis")
        print("1)da se krijes dok se ne zavrsi pljacka")
        print("ili")
        print("2)da im odvratis paznju")
        k = input(">>>")
        if k == "1":
            print("ti si se krio i cekao ali su te nasli i ubili")
            quit()
        elif k == "2":
            print("ti si im odvratio paznju tako sto si bacio nesto")
            print(
                "dok su oni reagovali covek koji je tamo radio izvladio je njegov pistolj i ranio kriminalce u nogu"
            )
            print("posle toga dosla policija i uhapsila kriminalce")
            print("ostatak dana ti je bio normalan")
        else:
            print("imas brojeve")
            quit()
else:
    print("ne znas da kucas slova pa neces ni da igras")
    quit()
