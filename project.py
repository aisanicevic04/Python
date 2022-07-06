def lozinka():
    while True:
        password = input("Unesite sifru: ")
        if len(password) < 8:
            print("Lozinka mora imati najmanje 8 karaktera")
        elif not password.isdigit():
            print("Lozinka mora sadrzati broj!")
        elif not password.isupper():
            print("Lozinka mora imati veliko slovo unutar")
        else:
            print("Vasa sifra je prihvacena")
            break


lozinka()
