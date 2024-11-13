class MobilSport:
    def __init__(self):
        # Variable private
        self.__merek = "Ferrari"
        self.__kecepatan = 320
        self.__warna = "Merah"
    
    # Setter - Method untuk mengubah nilai
    def set_merek(self, merek_baru):
        print(f"Mengubah merek dari {self.__merek} menjadi {merek_baru}")
        self.__merek = merek_baru
    
    def set_kecepatan(self, kecepatan_baru):
        if kecepatan_baru > 0:
            print(f"Mengubah kecepatan dari {self.__kecepatan} menjadi {kecepatan_baru}")
            self.__kecepatan = kecepatan_baru
        else:
            print("Error: Kecepatan tidak boleh kurang dari 0!")
    
    def set_warna(self, warna_baru):
        print(f"Mengubah warna dari {self.__warna} menjadi {warna_baru}")
        self.__warna = warna_baru
    
    # Method untuk melihat hasil perubahan
    def tampilkan_info(self):
        print(f"\nInfo Mobil Terkini:")
        print(f"Merek: {self.__merek}")
        print(f"Kecepatan: {self.__kecepatan} km/jam")
        print(f"Warna: {self.__warna}")

# Program utama
print("=== Program Setter ===")
mobil1 = MobilSport()

print("\nInfo awal:")
mobil1.tampilkan_info()

print("\nMencoba mengubah data mobil:")
mobil1.set_merek("Lamborghini")
mobil1.set_kecepatan(350)
mobil1.set_warna("Hitam")

print("\nSetelah perubahan:")
mobil1.tampilkan_info()

print("\nMencoba input yang salah:")
mobil1.set_kecepatan(-100)  # Akan menampilkan pesan error