from H2.Kodutöö import Kodutöö


class Õpilane :
    def __init__(self, õpilaseNimi, kursuseNimetus ):
        self.nimi = õpilaseNimi
        self.kursus = kursuseNimetus
        self.tehtudKodutööd = [] #Tühi list
        self.tegemataKodutööd = [] #Tühi list

    def lisaKodutöö(self, antudülesanne1): #antudÜlesanne1 parameetri nimetus võib olla mistahes
        self.tegemataKodutööd.append(antudülesanne1)

    def tagastaTegemataKodutööd(self):
        for koduneÜlesanne in self.tegemataKodutööd:
            print(koduneÜlesanne.nimetus)

    def lisatehtudKodutööd(self, tehtudKodutöö):
            tehtudKodutöö.kasTehtud = True
            self.tegemataKodutööd.remove(tehtudKodutöö)
            self.tehtudKodutööd.append(tehtudKodutöö)

    def tagastaTehtudKodutöö(self):
        for tehtudKodutöö in self.tehtudKodutööd:
            print(tehtudKodutöö.pealkiri)




kooliÕpilane = Õpilane("Tark Tudeng", "AB-123")
kodutöö1 = Kodutöö("TEST")
kodutöö2 = Kodutöö ("Arvutamine")

kooliÕpilane.lisaKodutöö(kodutöö1)
kooliÕpilane.lisaKodutöö(kodutöö2)
kooliÕpilane.tagastaTegemataKodutööd() # = Õpilane("Tark Tudeng", "AB-123").tagastaTegemataKodutööd()