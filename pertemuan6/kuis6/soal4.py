level_diskon = (
    (500000, 15),
    (300000, 10),
    (100000, 5),
    (0, 0)
)

def hitung_diskon(total_belanja, level_diskon, index=0):
    ambang_batas, persen = level_diskon[index]
    
    if total_belanja >= ambang_batas:
        nominal_diskon = total_belanja * (persen / 100)
        total_bayar = total_belanja - nominal_diskon
        return (persen, nominal_diskon, total_bayar)
    else:
        return hitung_diskon(total_belanja, level_diskon, index + 1)


nama_user = input("Masukkan nama Anda: ")
total = float(input("Masukkan total belanja: "))

if total < 100000:
    print("Tidak ada diskon.")
else:
    p, n, t = hitung_diskon(total, level_diskon)
    print(f"\nRingkasan untuk {nama_user}:")
    print(f"Total Belanja  : Rp{total}")
    print(f"Persen Diskon  : {p}%")
    print(f"Nominal Diskon : Rp{n}")
    print(f"Total Bayar    : Rp{t}")