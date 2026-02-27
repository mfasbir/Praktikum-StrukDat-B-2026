# konverter.py
# Berisi fungsi konversi mata uang

from kurs import kurs

def idr_ke_mata_uang(jumlah_idr, kode_tujuan):
    if kode_tujuan in kurs:
        return jumlah_idr / kurs[kode_tujuan]
    else:
        raise ValueError("Kode mata uang tidak valid!")

def mata_uang_ke_idr(jumlah_valas, kode_asal):
    if kode_asal in kurs:
        return jumlah_valas * kurs[kode_asal]
    else:
        raise ValueError("Kode mata uang tidak valid!")

def konversi(jumlah, dari, ke):
    if dari == ke:
        return jumlah

    # Jika dari IDR ke mata uang lain
    if dari == "IDR":
        return idr_ke_mata_uang(jumlah, ke)

    # Jika ke IDR
    if ke == "IDR":
        return mata_uang_ke_idr(jumlah, dari)

    # Jika valas ke valas (contoh USD ke EUR)
    jumlah_idr = mata_uang_ke_idr(jumlah, dari)
    return idr_ke_mata_uang(jumlah_idr, ke)