nilai1 = int(input("Masukan nilai ujian teori siswa: "))
nilai2 = int(input("Masukan nilai ujian praktek siswa: ")) 

nilai3 = nilai1 + nilai2
while nilai3 >= 140:
    print(f"Selamat, anda lulus!")

while nilai3 <= 138:
    print(f"Anda harus mengulang ujian teori dan praktek.")

while nilai1 < 70:
        print(f"Anda harus mengulang ujian teori.")

while nilai2 < 70:
        print(f"Anda harus mengulang ujian praktek.")




    
    
    
    
    

    