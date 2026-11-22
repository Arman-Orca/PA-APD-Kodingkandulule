from data import paket, MAKS_HARGA
from helper import clear_screen, enter, tanya_teks, pilih_menu
from tampilan import tampil_paket
from fiturtukang import ambil_nomor

def input_angka(pesan, maksimal=None):
    while True:
        try:
            nilai = int(tanya_teks(pesan))
            if nilai < 0:
                raise ValueError("negatif")
            if maksimal is not None and nilai > maksimal:
                raise ValueError("terlalu besar")
        except ValueError:
            print("Input harus berupa angka bulat positif!")
            if maksimal is not None:
                print("(maksimal", maksimal, ")")
        else:
            return nilai

def ubah_paket():
    clear_screen()
    print("---( UBAH PAKET )---")
    print()
    tampil_paket(paket, False)
    if len(paket) == 0:
        enter()
        return
    print()
    idx = ambil_nomor(paket)
    if idx is None:
        enter()
        return
    nama_baru = tanya_teks("Nama baru").strip()
    if nama_baru == "":
        print("Nama paket tidak boleh kosong!")
        enter()
        return
    harga_baru = input_angka("Harga baru (Rp)", MAKS_HARGA)
    fitur_baru = input_angka("Jumlah fitur baru")
    paket[idx]["nama"] = nama_baru
    paket[idx]["harga"] = harga_baru
    paket[idx]["fitur"] = fitur_baru
    print("Paket berhasil diubah.")
    enter()

def ubah_status_paket():
    clear_screen()
    print("---( UBAH STATUS PAKET )---")
    print()
    tampil_paket(paket, False)
    if len(paket) == 0:
        enter()
        return
    print()
    idx = ambil_nomor(paket)
    if idx is None:
        enter()
        return
    pilihan = pilih_menu("Status baru", ["Tersedia", "Habis"])
    paket[idx]["sedia"] = pilihan == "Tersedia"
    print("Status paket berhasil diubah.")
    enter()