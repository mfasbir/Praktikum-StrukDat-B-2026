kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]

for nama, nilai in kumpulan_nilai:
    if nilai >= 75:
        print(f"Selamat {nama}, Anda Lulus!")
    else:
        print(f"maaf {nama}, Anda harus remmidi")