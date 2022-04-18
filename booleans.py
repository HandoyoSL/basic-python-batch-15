#menghasilkan true
a = 34 > 33
print(a)
#menghasilkan false
c = 34 < 33
print(c)

# Jika dalam python angka 0 bernilai salah
b = 0
print(f"angka NOL: {bool(b)}")
#jika dalam python angka 1 bernilai benar
r = 1
print(f"angka SATU : {bool(r)}")
# Jika dalam python list kosong bernilai salah
b = []
print(f"angka List Kosong : {bool(b)}")

#jika int type data nya
bilangan_pertama = int(input("Masukkan bilangan pertama: "))
bilangan_kedua = int(input("Masukkan bilangan kedua: "))

if bilangan_pertama > bilangan_kedua:
    print(f"Bilangan {bilangan_pertama} lebih besar dari {bilangan_kedua}")
elif bilangan_pertama < bilangan_kedua:
    print(f"bilangan {bilangan_pertama} lebih kecil dari {bilangan_kedua}")

#jika string type data nya
bilangan_pertama = input("Masukkan bilangan pertama: ")
bilangan_kedua = input("Masukkan bilangan kedua: ")

if bilangan_pertama > bilangan_kedua:
    print(f"Bilangan {bilangan_pertama} lebih besar dari {bilangan_kedua}")
elif bilangan_pertama < bilangan_kedua:
    print(f"bilangan {bilangan_pertama} lebih kecil dari {bilangan_kedua}")