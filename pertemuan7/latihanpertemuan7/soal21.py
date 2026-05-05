antrean_array = ["Pasien A (Stabil)", "Pasien B (Stabil)", "Pasien C (Stabil)"]

def sisipkan_pasien_darurat_array(nama_pasien, posisi):
    antrean_array.insert(posisi - 1, nama_pasien)

sisipkan_pasien_darurat_array("Pasien DARURAT X", 2)

print("Antrean Akhir (Array):", antrean_array)