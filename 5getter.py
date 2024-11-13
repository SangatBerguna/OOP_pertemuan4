class MobilSport:
    def __init__(self):
        # Variable dengan __ adalah private
        self.__merek = "Ferrari"
        self.__kecepatan = 320
        self.__warna = "Merah"
    
    # Getter - Method untuk mengambil nilai
    def get_merek(self):
        return self.__merek
    
    def get_kecepatan(self):
        return self.__kecepatan
    
    def get_warna(self):
        return self.__warna
    
    def get_info_lengkap(self):
        return f"Mobil {self.__merek} berwarna {self.__warna} dengan kecepatan {self.__kecepatan} km/jam"

# Program utama
print("=== Program Getter ===")
mobil1 = MobilSport()

# Menggunakan getter untuk mengambil nilai
print("\nMengambil info satu per satu:")
print(f"Merek mobil: {mobil1.get_merek()}")
print(f"Kecepatan mobil: {mobil1.get_kecepatan()} km/jam")
print(f"Warna mobil: {mobil1.get_warna()}")

print("\nMengambil info lengkap:")
print(mobil1.get_info_lengkap())