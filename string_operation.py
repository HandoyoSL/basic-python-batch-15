nama: str = "Iqbals"
belakang: str = "Adudu"

# Mendapatkan karakter ke x
print(f"huruf ke 0 adalah: {nama[0]}")

# Mendapatkan karakter dari posisi x ke y
#kalau ini dari 0, tapi untuk akhir angka yang diminta itu harus dilebihkan satu pada angka yang diminta
print(f"Karakter dari indeks ke 2 sampai indeks ke 4 adalah: {nama[2:5]}")

# Panjang dari string
#kalau len ngitung dari satu
print(f"panjang string: {len(nama)}")

# Merge variabel
print(nama, belakang)
print(f"{nama} {belakang}")
print(f"{nama + belakang}")