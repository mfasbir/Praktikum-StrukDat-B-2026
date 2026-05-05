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