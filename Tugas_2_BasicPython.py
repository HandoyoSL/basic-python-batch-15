
print(f"Selamat Datang!")
print(f"1. Daftar Kontak")
print(f"2. Tambah Kontak")
print(f"3. Keluar")
menu = int(input("Pilih Menu: "))

kontak = []
if menu == 1:
    for i in kontak:
        kontak.append(f"Nama: Fawwaz")
        kontak.append(f"No Telepon: 08123456789")
        kontak.append(f"Nama: John")
        kontak.append(f"No Telepon: 08987654321")
        print(kontak)

elif menu == 2:
    nama = str(input("Nama: "))
    telepon = int(input("No Telepon: "))
    print(f"Kontak Berhasil Ditambah")

elif menu == 3:
    print(f"program selesai sampai jumpa")
    
else:
    print(f"Menu tidak tersedia")