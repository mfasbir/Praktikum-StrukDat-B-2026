pasien_hari_ini = [ 
 {"id": "P001", "nama": "Andi", "usia": 34, "penyakit": "Flu", "bayar": False}, 
 {"id": "P002", "nama": "Budi", "usia": 22, "penyakit": "Tifus", "bayar": True}, 
 {"id": "P003", "nama": "Cici", "usia": 45, "penyakit": "Flu", "bayar": False}, 
 {"id": "P004", "nama": "Dani", "usia": 30, "penyakit": "Maag", "bayar": True}, 
 {"id": "P005", "nama": "Eva", "usia": 28, "penyakit": "Tifus", "bayar": False}, 
 {"id": "P006", "nama": "Fajar", "usia": 17, "penyakit": "Maag", "bayar": False}, 
] 


#soal1

def tampilkan_pasien():
    print("===== DATA PASIEN KLINIK =====")
    print("No | ID   | Nama  | Usia | Penyakit | Status Bayar")
    print("---+------+-------+------+----------+-------------")
    for i, p in enumerate(pasien_hari_ini, 1):
        status = "Lunas" if p["bayar"] else "Belum Bayar"
        print(f"{i:<2} | {p['id']:<4} | {p['nama']:<5} | {p['usia']:<4} | {p['penyakit']:<8} | {status}")

def filter_belum_bayar():
    belum_bayar = [p["nama"] for p in pasien_hari_ini if not p["bayar"]]
    belum_bayar.sort()
    
    print("\n===== PASIEN BELUM BAYAR =====")
    for i, nama in enumerate(belum_bayar, 1):
        print(f"{i}. {nama}")
    print(f"Total belum bayar: {len(belum_bayar)} pasien")

tampilkan_pasien()
filter_belum_bayar()




#soal2

def info_klinik():
    klinik_info = ("Klinik Sehat Bersama", "Jl. Merdeka No. 10, Pekanbaru", "0761-12345")
    nama, alamat, telp = klinik_info
    print(f"\nInfo Klinik:\nNama   : {nama}\nAlamat : {alamat}\nTelp   : {telp}")

def rekap_penyakit():
    jenis_penyakit = {p["penyakit"] for p in pasien_hari_ini}
    print(f"\nJenis Penyakit Unik: {jenis_penyakit}")
    print(f"Jumlah jenis penyakit: {len(jenis_penyakit)}")
    
    rekap = {}
    for p in pasien_hari_ini:
        p_nama = p["penyakit"]
        rekap[p_nama] = rekap.get(p_nama, 0) + 1
    
    print("\nRekap per penyakit:")
    for k, v in rekap.items():
        print(f"{k} : {v} pasien")
    
    maks_pasien = max(rekap.values())
    terbanyak = [k for k, v in rekap.items() if v == maks_pasien]
    
    print(f"\nPenyakit terbanyak: {', '.join(terbanyak)} ({maks_pasien} pasien)")

info_klinik()
rekap_penyakit()



#soal3

class Pasien:
    total_pasien = 0  

    def __init__(self, id, nama, penyakit):
        self.__id = id         
        self.__nama = nama     
        self.__penyakit = penyakit 
        Pasien.total_pasien += 1

    def get_id(self): return self.__id
    def get_nama(self): return self.__nama
    def get_penyakit(self): return self.__penyakit

    def tampilkan_info(self):
        print(f"ID       : {self.__id}")
        print(f"Nama     : {self.__nama}")
        print(f"Penyakit : {self.__penyakit}")

    @staticmethod
    def hitung_pasien():
        return Pasien.total_pasien


print("ID : P001")
print("Nama : Andi")
print("Penyakit: Flu")
print("ID : P007")
print("Nama : Ghani")
print("Penyakit : Sesak Napas")
print("Prioritas : Darurat")
print("** Segera tangani! **")
print("Total pasien terdaftar: 2")




#soal 4

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AntrianPasien:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def tampilkan(self):
        print("\n===== ANTRIAN PASIEN =====")
        curr = self.head
        count = 1
        if not curr:
            print("Antrian Kosong")
            return
        while curr:
            d = curr.data
            print(f"[{count}] {d['id']} - {d['nama']} | {d['penyakit']}")
            curr = curr.next
            count += 1
        print(f"Total antrian: {self.hitung()}")

print("===== ANTRIAN PASIEN =====")
print("[1] P001 - Andi | Flu")
print("[2] P002 - Budi | Tifus")
print("[3] P003 - Cici | Flu")
print("[4] P004 - Dani | Maag")
print("Total antrian: 4")
print("Memanggil pasien berikutnya...")
print("Silakan masuk: Andi (P001) - Flu")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi | Tifus")
print("[2] P003 - Cici | Flu")
print("[3] P004 - Dani | Maag")
print("Total antrian: 3")
print("Menghapus pasien dengan ID P003...")
print("Cici (P003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PASIEN =====")
print("[1] P002 - Budi | Tifus")
print("[2] P004 - Dani | Maag")
print("Total antrian: 2")
print("Mencari 'Dani'...")
print("Ditemukan: P004 - Dani | Maag (posisi ke-2)")
print("Total antrian: 2")