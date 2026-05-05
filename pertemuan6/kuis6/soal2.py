katalog = [
    {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
    {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
    {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8}
]

def cari_buku(katalog, keyword):
    hasil_cari = []
    for buku in katalog:
        if keyword.lower() in buku['nama'].lower():
            hasil_cari.append(buku)
    return hasil_cari


key = input("Masukkan kata kunci pencarian: ")
hasil = cari_buku(katalog, key)

if not hasil:
    print("Buku tidak ditemukan.")
else:
    print("\nHasil Pencarian:")
    for b in hasil:
        print(f"- {b['nama']} (Harga: {b['harga']}, Stok: {b['stok']})")