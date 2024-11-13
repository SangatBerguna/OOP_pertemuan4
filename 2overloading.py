class Mobil:
    def __init__(self):
        self.nama = ""
        
    # Method dengan parameter yang fleksibel
    def hitung_kecepatan(self, kecepatan, waktu=None, bahan_bakar=None):
        if waktu is None and bahan_bakar is None:
            return f"Kecepatan mobil adalah {kecepatan} km/jam"
        
        elif bahan_bakar is None:
            jarak = kecepatan * waktu
            return f"Dengan kecepatan {kecepatan} km/jam selama {waktu} jam, mobil menempuh jarak {jarak} km"
        
        else:
            jarak = kecepatan * waktu
            konsumsi = jarak * bahan_bakar
            return f"Mobil menempuh jarak {jarak} km dan menghabiskan {konsumsi} liter bensin"

# Membuat objek dari class Mobil
mobil_saya = Mobil()

# Mencoba memanggil method dengan parameter berbeda
print("\nTest 1 (satu parameter):")
print(mobil_saya.hitung_kecepatan(60))

print("\nTest 2 (dua parameter):")
print(mobil_saya.hitung_kecepatan(60, 2))

print("\nTest 3 (tiga parameter):")
print(mobil_saya.hitung_kecepatan(60, 2, 0.1))