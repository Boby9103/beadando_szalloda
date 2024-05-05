from abc import ABC

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.tipus = "Egyágyas"

    def info(self):
        return f"Egyágyas szoba, Szobaszám: {self.szobaszam}, Ár: {self.ar} Ft/éj"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar):
        super().__init__(szobaszam, ar)
        self.tipus = "Kétagyas"

    def info(self):
        return f"Kétagyas szoba, Szobaszám: {self.szobaszam}, Ár: {self.ar} Ft/éj"

egyagyas_szoba = EgyagyasSzoba(101, 20000)
ketagyas_szoba = KetagyasSzoba(102, 30000)

print(egyagyas_szoba.info())
print(ketagyas_szoba.info())
