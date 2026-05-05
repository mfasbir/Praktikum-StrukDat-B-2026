class Node:
    def __init__(self, nama, keluhan):
        self.nama    = nama
        self.keluhan = keluhan
        self.next    = None

class AntrianRumahSakit:
    def __init__(self):
        self.head  = None
        self.tail  = None
        self._size = 0
        self._nomor_antrian = 0

    def enqueue(self, nama, keluhan):
        pasien_baru = Node(nama, keluhan)
        self._nomor_antrian += 1

        if self.tail is None:
            self.head = pasien_baru
            self.tail = pasien_baru
        else:
            self.tail.next = pasien_baru
            self.tail      = pasien_baru

        self._size += 1
        print(f"[DAFTAR] {nama.capitalize()} terdaftar dengan keluhan: "
              f"{keluhan} (No. Antrian: {self._nomor_antrian})")

    def dequeue(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong! Tidak ada pasien yang bisa dipanggil.")
            return None

        pasien_dipanggil = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self._size -= 1
        print(f"[PANGGIL] Dokter memanggil: {pasien_dipanggil.nama.upper()} "
              f"(keluhan: {pasien_dipanggil.keluhan})")
        return pasien_dipanggil

    def peek(self):
        if self.is_empty():
            print("[ERROR] Antrian kosong!")
            return None

        print(f"[PEEK] Pasien berikutnya: {self.head.nama.upper()} "
              f"— {self.head.keluhan}")
        return self.head

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def clear(self):
        self.head  = None
        self.tail  = None
        self._size = 0
        print("[CLEAR] Sesi poliklinik selesai. Antrian dikosongkan.")

    def tampilkan_antrian(self):
        if self.is_empty():
            print("[ANTRIAN] Antrian sedang kosong.")
            return

        print("[ANTRIAN SAAT INI]")
        current = self.head
        nomor   = 1
        while current is not None:
            print(f"  {nomor}. {current.nama.upper():<10} → {current.keluhan}")
            current = current.next
            nomor  += 1


def main():
    print("=" * 36)
    print("  SISTEM ANTRIAN POLI UMUM")
    print("  RS Sehat Bersama")
    print("=" * 36)
    print()

    antrian = AntrianRumahSakit()

    if antrian.is_empty():
        print("[CEK] Apakah antrian kosong? → YA, antrian masih kosong.")
    else:
        print("[CEK] Apakah antrian kosong? → TIDAK, ada pasien menunggu.")
    print()

    antrian.enqueue("Budi",  "demam tinggi")
    antrian.enqueue("Ani",   "batuk pilek")
    antrian.enqueue("Citra", "sakit kepala")
    print()

    print(f"[INFO] Jumlah pasien menunggu: {antrian.size()} orang")

    antrian.peek()
    print()

    antrian.dequeue()

    antrian.enqueue("Dodi", "nyeri perut")
    print()

    antrian.tampilkan_antrian()
    print()

    antrian.dequeue()

    print(f"[INFO] Jumlah pasien masih menunggu: {antrian.size()} orang")
    print()

    antrian.clear()

    if antrian.is_empty():
        print("[CEK] Apakah antrian kosong? → YA, antrian sudah kosong.")
    else:
        print("[CEK] Apakah antrian kosong? → TIDAK, ada pasien menunggu.")

    print()
    print("=" * 36)
    print("  Simulasi Selesai!")
    print("=" * 36)


main()