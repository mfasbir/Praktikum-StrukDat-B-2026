
nilai_tugas = [70, 85, 90, 65, 80]

# a. Ganti nilai 65 menjadi 75 menggunakan index
nilai_tugas[3] = 75

# b. Tambahkan nilai 95 dan urutkan descending
nilai_tugas.append(95)
nilai_tugas.sort(reverse=True)

# c. Tampilkan jumlah total seluruh nilai
total = sum(nilai_tugas)
print("Total nilai:", total)

# d. Cek keberadaan nilai 100
if 100 in nilai_tugas:
    print("Ada nilai sempurna")
else:
    print("tidak ada")
