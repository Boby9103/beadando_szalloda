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

# Példa használatra
# hotel = Szalloda("Hotel Budapest", "Budapest, Bajcsy-Zsilinszky út 1.")
# hotel.szoba_hozzaadas(101, 20000, "egyágyas")
# hotel.szoba_hozzaadas(102, 30000, "kétagyas")
# print(hotel.szobak_listazasa())
# hotel.szoba_eltavolitas(101)
# print(hotel.szobak_listazasa())

# Megjegyzés: a példányosítás és metódushívások kikommentezve vannak, csak demonstrációs célból szerepelnek itt.

class Foglalas:
    def __init__(self, szobaszam, datum, vendeg_neve):
        self.szobaszam = szobaszam
        self.datum = datum
        self.vendeg_neve = vendeg_neve

    def foglalas_info(self):
        return (f"Foglalás: {self.szobaszam} szobaszám, Dátum: {self.datum}, "
                f"Vendég: {self.vendeg_neve}")

# Példa használatra
# foglalas = Foglalas(102, "2024-05-05", "Kovács István")
# print(foglalas.foglalas_info())

    def szoba_foglalas(self, szobaszam, datum, vendeg_neve):
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

# hotel = Szalloda("Hotel Budapest", "Budapest, Bajcsy-Zsilinszky út 1.")
# hotel.szoba_hozzaadas(101, 20000, "egyágyas")
# hotel.szoba_hozzaadas(102, 30000, "kétagyas")
# print(hotel.szoba_foglalas(101, "2024-05-05", "Kovács István"))

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

    def szoba_foglalas(self, szobaszam, datum, vendeg_neve):
        szoba = next((sz for sz in self.szobak if sz.szobaszam == szobaszam), None)
        if not szoba:
            return "A megadott számú szoba nem létezik."
        if any(f.szobaszam == szobaszam and f.datum == datum for f in self.foglalasok):
            return "A szoba már foglalt ezen a napon."
        foglalas = Foglalas(szobaszam, datum, vendeg_neve)
        self.foglalasok.append(foglalas)
        return f"A foglalás sikeres. Ár: {szoba.ar} Ft/éj"

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

# Példa használatra
# hotel = Szalloda("Hotel Budapest", "Budapest, Bajcsy-Zsilinszky út 1.")
# hotel.szoba_hozzaadas(101, 20000, "egyágyas")
# hotel.szoba_foglalas(101, "2024-05-05", "Kovács István")
# print(hotel.foglalas_lemondas(101, "2024-05-05"))

# Megjegyzés: a példányosítás és metódushívások kikommentezve vannak, csak demonstrációs célból szerepelnek itt.


