# Membuat class Mahasiswa
class Mahasiswa:
    def __init__(self, nama, nim, prodi, semester, ipk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.semester = semester
        self.ipk = ipk

    # Method 1: menampilkan data mahasiswa
    def tampilkan_data(self):
        print("Nama      :", self.nama)
        print("NIM       :", self.nim)
        print("Prodi     :", self.prodi)
        print("Semester  :", self.semester)
        print("IPK       :", self.ipk)
        print("--------------------------")

    # Method 2: mengubah IPK
    def ubah_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print("IPK berhasil diubah menjadi", self.ipk)


# Membuat 3 object
mhs1 = Mahasiswa("Fasbir", "250711001", "Teknik Informatika", 2, 3.50)
mhs2 = Mahasiswa("Sabran", "250711002", "Teknik Kimia", 2, 3.20)
mhs3 = Mahasiswa("Jamil", "250711003", "Teknik Teknik Sipil", 2, 3.80)

# Menampilkan data awal
print("Data Awal Mahasiswa:")
mhs1.tampilkan_data()
mhs2.tampilkan_data()
mhs3.tampilkan_data()

# Mengubah salah satu atribut (IPK) dari object mhs2
mhs2.ubah_ipk(3.60)

# Menampilkan data setelah diubah
print("Data Setelah Perubahan:")
mhs2.tampilkan_data()
