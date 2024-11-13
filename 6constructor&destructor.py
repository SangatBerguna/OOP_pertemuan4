class MobilSport:
    # Constructor - dipanggil saat objek dibuat
    def __init__(self, merek, warna):
        print("=== Constructor dipanggil ===")
        self.merek = merek
        self.warna = warna
        print(f"Mobil sport {merek} warna {warna} sedang dirakit di pabrik...")
        print(f"Perakitan {merek} selesai!")
    
    # Destructor - dipanggil saat objek dihapus
    def __del__(self):
        print("\n=== Destructor dipanggil ===")
        print(f"Mobil {self.merek} sudah tidak digunakan lagi")
        print("Mobil telah dihancurkan")


# inti
print("1. Membuat mobil baru")
mobil1 = MobilSport("Porsche", "Merah")

print("\n2. Program sedang berjalan...")
print(f"Ada mobil {mobil1.merek} warna {mobil1.warna}")

print("\n3. Menghapus mobil")
del mobil1