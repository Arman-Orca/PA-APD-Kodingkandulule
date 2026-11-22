from data import tukang, status_tukang
from helper import clear_screen, enter, tanya_teks, pilih_menu
from tampilan import tampil_tukang

def ambil_nomor(daftar):
    try:
        nomor = int(tanya_teks("Masukkan nomor"))
        if nomor < 1 or nomor > len(daftar):
            raise IndexError(nomor)
    except ValueError:
        print("Nomor harus berupa angka!")
        return None
    except IndexError:
        print("Nomor tidak ditemukan!")
        return None
    return nomor - 1

def ubah_tukang():
    clear_screen()
    print("---( UBAH TUKANG )---")
    print()
    tampil_tukang()
    if len(tukang) == 0:
        enter()
        return
    print()
    idx = ambil_nomor(tukang)
    if idx is None:
        enter()
        return
    nama_baru = tanya_teks("Nama baru").strip()
    try:
        if nama_baru == "":
            raise ValueError("Nama tukang tidak boleh kosong!")
    except ValueError as e:
        print(e)
    else:
        tukang[idx]["nama"] = nama_baru
        print("Data tukang berhasil diubah.")
    finally:
        enter()

def ubah_status_tukang():
    clear_screen()
    print("---( UBAH STATUS TUKANG )---")
    print()
    tampil_tukang()
    if len(tukang) == 0:
        enter()
        return
    print()
    idx = ambil_nomor(tukang)
    if idx is None:
        enter()
        return
    status_baru = pilih_menu("Status baru", list(status_tukang))
    tukang[idx]["status"] = status_baru
    print("Status tukang berhasil diubah.")
    enter()