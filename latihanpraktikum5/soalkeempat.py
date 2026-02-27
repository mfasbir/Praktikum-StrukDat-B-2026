transaksi = [
    {"produk": "Buku", "harga": 10000, "jumlah": 3},
    {"produk": "Pena", "harga": 5000, "jumlah": 10},
    {"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]

# a. Ubah jumlah buku menjadi 8
transaksi[0]["jumlah"] = 8

# b. Tambahkan 2 produk baru
transaksi.append({"produk": "Penggaris", "harga": 3000, "jumlah": 5})
transaksi.append({"produk": "Kertas A4", "harga": 50000, "jumlah": 1})


# c. Hitung Total Pendapatan menggunakan perulangan
for item in transaksi:
    total_per_item = item["harga"] * item["jumlah"]
    print(f"Produk: {item['produk']} | Total: {total_per_item}")