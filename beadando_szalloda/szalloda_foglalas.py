from abc import ABC

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, ar):
        super().__init__(None, ar)  # Szobaszámot később adjuk meg
        self.tipus = "Egyágyas"

    def info(self):
        return f"Egyágyas szoba, Ár: {self.ar} Ft/éj"

class KetagyasSzoba(Szoba):
    def __init__(self, ar):
        super().__init__(None, ar)  # Szobaszámot később adjuk meg
        self.tipus = "Kétagyas"

    def info(self):
        return f"Kétagyas szoba, Ár: {self.ar} Ft/éj"

class Szalloda:
    def __init__(self, nev, cim):
        self.nev = nev
        self.cim = cim
        self.szobak = []  # Szobák listája
        self.foglalasok = []  # Foglalások listája

    def szoba_hozzaadas(self, szobaszam, ar, tipus):
        if tipus == "egyágyas":
            szoba = EgyagyasSzoba(ar)
        elif tipus == "kétagyas":
            szoba = KetagyasSzoba(ar)
        else:
            return "Ismeretlen szoba típus"
        szoba.szobaszam = szobaszam  # Szobaszám hozzárendelése
        self.szobak.append(szoba)
        return f"Szoba hozzáadva: {szobaszam}"

    def szoba_eltavolitas(self, szobaszam):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.szobak.remove(szoba)
                return f"Szoba eltávolítva: {szobaszam}"
        return "Szoba nem található"

    def szobak_listazasa(self):
        if not self.szobak:
            return "Nincsenek szobák"
        return "\n".join(szoba.info() for szoba in self.szobak)

    def szoba_foglalas(self, tipus, datum, vendeg_neve):
        # Keresünk egy elérhető szobát a megadott típus alapján
        for szoba in self.szobak:
            if szoba.tipus == tipus and all(f.szobaszam != szoba.szobaszam or f.datum != datum for f in self.foglalasok):
                foglalas = Foglalas(szoba.szobaszam, datum, vendeg_neve)
                self.foglalasok.append(foglalas)
                return f"A foglalás sikeres. Szobaszám: {szoba.szobaszam}, Ár: {szoba.ar} Ft/éj"
        return "Nincs elérhető szoba a kért típusban."

    def foglalas_lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return f"Foglalás lemondva: Szoba {szobaszam}, Dátum {datum}"
        return "A foglalás nem található"

    def foglalasok_listazasa(self):
        if not self.foglalasok:
            return "Nincsenek aktív foglalások."
        return "\n".join(f"Foglalás: Szoba {f.szobaszam}, Dátum: {f.datum}, Vendég: {f.vendeg_neve}" for f in self.foglalasok)

class Foglalas:
    def __init__(self, szobaszam, datum, vendeg_neve):
        self.szobaszam = szobaszam
        self.datum = datum
        self.vendeg_neve = vendeg_neve

    def foglalas_info(self):
        return (f"Foglalás: {self.szobaszam} szobaszám, Dátum: {self.datum}, "
                f"Vendég: {self.vendeg_neve}")

    def szoba_foglalas(self, tipus, datum, vendeg_neve):
        # Ellenőrizzük, hogy a szoba létezik-e és elérhető-e a megadott napon
        szoba = next((sz for sz in self.szobak if sz.szobaszam == szobaszam), None)
        if not szoba:
            return "A megadott számú szoba nem létezik."
        if any(f.szobaszam == szobaszam and f.datum == datum for f in self.foglalasok):
            return "A szoba már foglalt ezen a napon."

        # Szoba foglalása
        foglalas = Foglalas(szobaszam, datum, vendeg_neve)
        self.foglalasok.append(foglalas)
        return f"A foglalás sikeres. Ár: {szoba.ar} Ft/éj"


def felhasznaloi_interfesz(hotel):
    while True:
        print("\n*** Szálloda Kezelő Rendszer ***")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy opciót (1-4): ")

        if valasztas == "1":
            tipus = input("Add meg a szoba típusát (egyágyas/kétagyas): ")
            datum = input("Add meg a foglalás dátumát (éééé-hh-nn): ")
            vendeg_neve = input("Add meg a vendég nevét: ")
            print(hotel.szoba_foglalas(tipus, datum, vendeg_neve))
        elif valasztas == "2":
            # A lemondás kezelése változatlan
            elif valasztas == "3":
            print("Aktív foglalások listája:")
            print(hotel.foglalasok_listazasa())
        elif valasztas == "4":
            print("Kilépés a programból.")
            break
        else:
            print("Érvénytelen választás, kérlek próbáld újra.")

hotel = Szalloda("Hotel Budapest", "Budapest, Bajcsy-Zsilinszky út 1.")
felhasznaloi_interfesz(hotel)
