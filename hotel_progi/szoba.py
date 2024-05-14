from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szoba_szam, ar):
        self.szoba_szam = szoba_szam
        self.ar = ar

    @abstractmethod
    def ar_szamitas(self):
        pass

class EgyagyasSzoba(Szoba):
    def ar_szamitas(self):
        return self.ar

class KetagyasSzoba(Szoba):
    def ar_szamitas(self):
        return self.ar * 1.5

class Szalloda:
    def __init__(self, nev, szobak):
        self.nev = nev
        self.szobak = szobak
        self.foglalasok = []

    def foglalas(self, szoba_szam, datum):
        for szoba in self.szobak:
            if szoba.szoba_szam == szoba_szam:
                foglalt = any(f.datum == datum for f in self.foglalasok)
                if not foglalt:
                    self.foglalasok.append(Foglalas(szoba, datum))
                    return f"A szobát sikeresen lefoglaltad {szoba.ar_szamitas()} Ft-ért."
                else:
                    return "A szoba már foglalt ezen a napon."
        return "Nincs ilyen szobaszám."

    def lemondas(self, szoba_szam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szoba_szam == szoba_szam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return "A foglalás sikeresen törölve."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        if self.foglalasok:
            for foglalas in self.foglalasok:
                print(f"Szoba: {foglalas.szoba.szoba_szam}, Dátum: {foglalas.datum}")
        else:
            print("Nincs foglalás.")

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

# Szobák létrehozása
szoba1 = EgyagyasSzoba("101", 100)
szoba2 = KetagyasSzoba("102", 120)
szoba3 = EgyagyasSzoba("103", 150)

# Szálloda létrehozása
szalloda = Szalloda("Példa Szálloda", [szoba1, szoba2, szoba3])

# Foglalások hozzáadása
szalloda.foglalas("101", datetime(2024, 10, 10))
szalloda.foglalas("102", datetime(2024, 9, 12))
szalloda.foglalas("103", datetime(2024, 8, 14))
szalloda.foglalas("101", datetime(2024, 7, 16))
szalloda.foglalas("102", datetime(2024, 7, 18))

# Felhasználói interfész és adatbekérés
while True:
    print("\nVálassz műveletet:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Kilépés")
    valasztas = input("Választott művelet: ")

    if valasztas == "1":
        szoba_szam = input("Add meg a foglalandó szoba számát:   \n Egyfős szobák száma:  \n szoba 101 = 100ft/éj, szoba 103 = 150ft/éj \n Kétfős szobák száma: \n szoba 102 = 120ft/éj \n")
        while szoba_szam not in ["101", "102", "103"]:
            print("Nincs ilyen szobaszám.")
            szoba_szam = input("Add meg a foglalandó szoba számát: ")
        while True:
            try:
                datum = datetime.strptime(input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d")
                while True:
                    if datum < datetime.now():
                        print("A foglalás dátuma nem lehet a múltban.")
                    else:
                        break
                    datum = datetime.strptime(input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d")
                print(f"{szalloda.foglalas(szoba_szam, datum)}")
                break                
            except ValueError:
                print("Hibás dátum formátum.")
            


            
    elif valasztas == "2":
        szoba_szam = input("Add meg a lemondandó foglalás szoba számát: ")
        datum = datetime.strptime(input("Add meg a lemondandó foglalás dátumát (YYYY-MM-DD formátumban): "), "%Y-%m-%d")
        print(szalloda.lemondas(szoba_szam, datum))
    elif valasztas == "3":
        szalloda.foglalasok_listazasa()
    elif valasztas == "4":
        break
    else:
        print("Érvénytelen választás.")
