# ======================================
# Praktikum Struktur Data
# Materi: Python Dictionaries
# ======================================

# DICTIONARY adalah struktur data untuk menyimpan data
# dalam bentuk pasangan KEY : VALUE
# Dictionary bersifat TERURUT (Python >= 3.7),
# DAPAT DIUBAH (mutable), dan KEY TIDAK BOLEH DUPLIKAT

# ------------------------------------------------------
# 1. Membuat dan Mengakses Dictionary
# Fungsi:
# - Membuat dictionary dengan beberapa pasangan key-value
# - Mengakses value menggunakan key
# ------------------------------------------------------
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print("Model mobil:", thisdict["model"])


# ------------------------------------------------------
# 2. Mengubah dan Menambah Item Dictionary
# Fungsi:
# - Mengubah value berdasarkan key
# - Menambahkan pasangan key-value baru
# ------------------------------------------------------
thisdict["year"] = 2020        # Mengubah value
thisdict["color"] = "red"      # Menambah item baru
print("Setelah diubah & ditambah:", thisdict)


# ------------------------------------------------------
# 3. Menghapus Item Dictionary
# Fungsi:
# - Menghapus item berdasarkan key
# - Menggunakan pop() dan del
# ------------------------------------------------------
thisdict.pop("model")
del thisdict["brand"]
print("Setelah dihapus:", thisdict)


# ------------------------------------------------------
# 4. Loop Dictionary
# Fungsi:
# - Menampilkan seluruh isi dictionary
# - Menggunakan items() untuk mengambil key dan value
# ------------------------------------------------------
print("Isi dictionary:")
for key, value in thisdict.items():
    print(key, ":", value)


# ------------------------------------------------------
# 5. Nested Dictionary
# Fungsi:
# - Menyimpan dictionary di dalam dictionary
# - Digunakan untuk data yang lebih kompleks
# ------------------------------------------------------
myfamily = {
    "child1": {
        "name": "Fasbir",
        "year": 2004
    },
    "child2": {
        "name": "Sabran",
        "year": 2007
    }
}

print("Data keluarga:")
for child, info in myfamily.items():
    print(child, "->", info)
