class Mobil:

    # atribut dan metode kelas induk
    name = "Mustang"
    harga = "9 Milliar"
    def sport(self):
        print("Aku Mobil dengan torsi terbaik")
    

# kelas anak
class Mobilbalap(Mobil):

    #method atau subclass anak
    def Cetaknama(self):
        print("Namaku : ", self.name)
    def cetakharga(self):
        print("Hargaku :", self.harga)

# instasiansi
labrador = Mobilbalap()

# inisialisasi

labrador.sport()
labrador.cetakharga()
# pemanggilan subclass method 
labrador.Cetaknama()