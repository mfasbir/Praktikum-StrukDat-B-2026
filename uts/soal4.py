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

    def panggil_berikutnya(self):
        if not self.head:
            print("Antrian kosong.")
            return
        p = self.head.data
        print(f"\nMemanggil pasien berikutnya...\nSilakan masuk: {p['nama']} ({p['id']}) - {p['penyakit']}")
        self.head = self.head.next

    def cari(self, nama):
        curr = self.head
        pos = 1
        while curr:
            if curr.data['nama'] == nama:
                d = curr.data
                print(f"\nMencari '{nama}'...\nDitemukan: {d['id']} - {d['nama']} | {d['penyakit']} (posisi ke-{pos})")
                return
            curr = curr.next
            pos += 1
        print(f"\nPasien {nama} tidak ditemukan.")
