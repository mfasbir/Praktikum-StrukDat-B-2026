kelas_A = {"Struktur Data", "Basis Data", "AI", "Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI", "Cloud Computing"}

irisan = kelas_A.intersection(kelas_B)
print("Diambil kedua kelas:", irisan)

hanya_A = kelas_A.difference(kelas_B)
print("Hanya di kelas A:", hanya_A)

gabungan = kelas_A.union(kelas_B)
print("Seluruh mata kuliah unik:", gabungan)