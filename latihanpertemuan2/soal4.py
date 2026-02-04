mahasiswa = {
    "A001": {"nama": "Budi", "prodi": "Informatika", "ipk": 3.45},
    "A002": {"nama": "Siti", "prodi": "Sistem Informasi", "ipk": 3.20},
    "A003": {"nama": "Andi", "prodi": "Informatika", "ipk": 3.75}
}


print("Mahasiswa berprestasi (IPK > 3.5):")
for nim, data in mahasiswa.items():
    if data["ipk"] > 3.5:
        print(data["nama"])


total_ipk = 0
for data in mahasiswa.values():
    total_ipk += data["ipk"]

rata_rata = total_ipk / len(mahasiswa)
print("\nRata-rata IPK seluruh mahasiswa:", rata_rata)


mahasiswa["A004"] = {"nama": "Fasbir", "prodi": "Teknik Informatika", "ipk": 3.60}

print("\nData setelah ditambah:")
print(mahasiswa["A004"])


