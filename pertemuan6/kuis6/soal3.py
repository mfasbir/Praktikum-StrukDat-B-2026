riwayat_transaksi = set()

def proses_transaksi(katalog, nama_buku, jumlah_beli):
    for buku in katalog:
        if buku['nama'].lower() == nama_buku.lower():
            if buku['stok'] >= jumlah_beli:
                buku['stok'] -= jumlah_beli
                total_harga = buku['harga'] * jumlah_beli
                riwayat_transaksi.add(buku['nama'])
                print(f"Transaksi Berhasil! Total Bayar: Rp{total_harga}")
                return
            else:
                print("Peringatan: Stok tidak mencukupi.")
                return
    print("Error: Buku tidak ditemukan di katalog.")

#Contoh 3 transaksi
katalog = [{'nama': 'Python', 'harga': 50000, 'stok': 10}]

for _ in range(3):
    nama = input("\nNama buku yang ingin dibeli: ")
    jumlah = int(input("Jumlah beli: "))
    proses_transaksi(katalog, nama, jumlah)

print("\nIsi Riwayat Transaksi (Unique):")
print(riwayat_transaksi)