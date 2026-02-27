sesi_pagi = {"Andi", "Budi", "Cici"}
sesi_siang = {"Budi", "Deni", "Eka"}

# a. Mahasiswa yang hadir di kedua sesi
keduanya = sesi_pagi.intersection(sesi_siang)
print("Hadir di kedua sesi:", keduanya)

# b. Total daftar nama unik
unik = sesi_pagi.union(sesi_siang)
print("Total mahasiswa unik:", len(unik))

# c. Gabungkan kedua set menjadi satu set baru
sesi_hari_ini = sesi_pagi.union(sesi_siang)