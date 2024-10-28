matriks1 = []
matriks2 = []

print("Masukkan Elemen Untuk Matriks Pertama :")
for i in range(2):
    baris = []
    for j in range(2):
        nilai = int(input(f"Masukkan Elemen Baris : {i+1},Kolom {j+1} : "))
        baris.append(nilai)
    matriks1.append(baris)

print("\nMasukkan Elemen Untuk Baris Kedua:")
for i in range(2):
    baris=[]
    for j in range (2):
        nilai = int(input(f"Masukkan elemen Baris {i+1}, Kolom {j+1} : "))
        baris.append(nilai)
    matriks2.append(baris)

hasil = []
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(matriks1[i][j] + matriks2[i][j])
    hasil.append(baris)

print("\nHasil Penjumlahan Matriks : ")
for baris in hasil:
    print(baris)





















