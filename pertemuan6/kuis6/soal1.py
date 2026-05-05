def tambah_buku(nama, harga, stok):
    if harga <= 0 or stok < 0:
        print("Error: Harga harus > 0 dan stok tidak boleh negatif.")
        return None
    
    return {
        "nama": nama,
        "harga": harga,
        "stok": stok
    }

katalog_buku = []

for i in range(3):
    print(f"\nInput Buku ke-{i+1}")
    nama = input("Masukkan nama buku: ")
    harga = float(input("Masukkan harga buku: "))
    stok = int(input("Masukkan stok buku: "))
    
    hasil = tambah_buku(nama, harga, stok)
    if hasil:
        katalog_buku.append(hasil)

print("\nDaftar Buku yang Berhasil Ditambahkan:")
print(katalog_buku)