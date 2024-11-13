class Mobil:

    # atribute dan metod induk
    name =""
    def start(self):
        print("Mobil mogok")
class MobilSport(Mobil):
    def start(self):
        print("Mobil sport sudah bisa melaju dengan cepat")

# membuat instasiansi
porsche = MobilSport()

# memanggil inisialiasasi

porsche.start()