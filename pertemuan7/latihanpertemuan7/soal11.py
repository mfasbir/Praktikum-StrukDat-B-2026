history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.insert(0, keyword)

tambah_pencarian_array("github.com")

print("Riwayat (Array):", history_array)