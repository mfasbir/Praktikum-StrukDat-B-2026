# main.py
from tabulate import tabulate
from kurs import kurs
from konverter import konversi

def format_rupiah(jumlah):
    return f"Rp {jumlah:,.0f}".replace(",", ".")

def tampilkan_tabel():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])
    
    print("=== KONVERTER MATA UANG ===")
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="grid"))

def main():
    tampilkan_tabel()

    daftar_mata_uang = ["IDR"] + list(kurs.keys())

    dari = input(f"\nDari ({'/'.join(daftar_mata_uang)}): ").upper()
    ke = input(f"Ke   ({'/'.join(daftar_mata_uang)}): ").upper()

    try:
        jumlah = float(input("Jumlah: "))
        hasil = konversi(jumlah, dari, ke)

        if ke == "IDR":
            print(f"\n{jumlah} {dari} = {format_rupiah(hasil)}")
        elif dari == "IDR":
            print(f"\n{format_rupiah(jumlah)} = {hasil:.2f} {ke}")
        else:
            print(f"\n{jumlah} {dari} = {hasil:.2f} {ke}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()