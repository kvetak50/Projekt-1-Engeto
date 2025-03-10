ukoly = []

def hlavni_menu():
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")
        
        volba = input("Vyberte možnost (1-4): ")
        print()
        
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Ukončování programu...")
            break
        else:
            print("Neplatná volba, zkuste to znovu.\n")

def pridat_ukol():
    ukol = input("Zadejte název úkolu: ")
    popis = input("Zadejte popis úkolu: ")
    ukoly.append((ukol, popis))
    print("Úkol a popis byl přidán!\n")

def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.\n")
    else:
        print("Seznam úkolů:")
        for x, (ukol, popis) in enumerate(ukoly, start=1):
            print((f"{x}. {ukol.capitalize()} - {popis}"))
        print()

def odstranit_ukol():
    zobrazit_ukoly()
    while True:
        if ukoly:
            try:
                cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
                if 1 <= cislo <= len(ukoly):
                    odstraneny = ukoly.pop(cislo - 1)
                    print(f"Úkol 'Úkol {odstraneny[0]}' byl odstraněn.\n")
                    return
                else:
                    print("Neplatné číslo úkolu.\n")
            except ValueError:
                print("Neplatný vstup. Zadejte prosím číslo.\n")

hlavni_menu()