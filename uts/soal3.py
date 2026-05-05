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

class PasienPrioritas(Pasien):
    def __init__(self, id, nama, penyakit, prioritas):
        super().__init__(id, nama, penyakit)
        self.prioritas = prioritas

    def tampilkan_info(self): 
        super().tampilkan_info()
        print(f"Prioritas: {self.prioritas}")
        if self.prioritas == "Darurat":
            print("** Segera tangani! **")


p1 = Pasien("P001", "Andi", "Flu")
p1.tampilkan_info()
print()
p2 = PasienPrioritas("P007", "Ghani", "Sesak Napas", "Darurat")
p2.tampilkan_info()
print(f"\nTotal pasien terdaftar: {Pasien.hitung_pasien()}")