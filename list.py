#untuk data yang bisa dihapus
from tkinter import N


minuman = []
minuman.append("susu")
minuman.append("jus")
minuman.append("teh")
minuman.pop(1)

for minum in minuman:
    print(minum)

#manual dalam menyebutkan index
buah = []
print("\n")
buah.append("mangga")
buah.append("anggur")
buah.append("semangka")

print(buah[0])
print(buah[1])
print(buah[2])

print("\n")

#untuk otomatis dipanggil
foods = []
# Menambahkan data baru di ujung
foods.append("Seblak")
foods.append("Rendang")
foods.append("Ayam Bakar")

# Mendapatkan panjang dari list
print(len(foods))


for food in foods:
    print(food)


