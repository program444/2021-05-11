class Toit:
    def __init__(self, nimi, hind, päevaEri):
        # Toidu omadused:
        self.nimetus = nimi
        self.hind = hind
        self.eripakkumine = päevaEri

uusToit = Toit("Salat", 3, True )
print(uusToit.nimetus, uusToit.eripakkumine)
