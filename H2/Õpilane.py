from H2.Kodutöö import Kodutöö


class Õpilane :
    def __init__(self, õpilaseNimi, kursuseNimetus ):
        self.nimi = õpilaseNimi
        self.kursus = kursuseNimetus
        self.tehtudKodutööd = []
        self.tegemataKodutööd = []

    def lisaKodutöö(self, ülesanne1):
        self.tegemataKodutööd.append(ülesanne1)

    def tagastaTegemataKodutööd(self):
        for koduneÜlesanne in self.tegemataKodutööd:
            print(koduneÜlesanne.nimetus)

    def lisatehtudKodutööd(self, tehtudKodutöö):
            self.tegemataKodutööd.remove(tehtudKodutöö)
            self.tehtudKodutööd.append(tehtudKodutöö)
            tehtudKodutöö.kastehtud = True









kooliÕpilane = Õpilane("Tark Tudeng", "AB-123")
kodutöö1 = Kodutöö("TEST", True, True)
kodutöö2 = Kodutöö ("Arvutamine", True, True)

kooliÕpilane.lisaKodutöö(kodutöö1)
kooliÕpilane.lisaKodutöö(kodutöö2)
kooliÕpilane.tagastaTegemataKodutööd()