from data import tukang, status_tukang
from helper import clear_screen, enter, pilih_menu, tanya_teks
from tampilan import tampil_tukang
from prettytable import PrettyTable

def ambil_nomor(daftar):
    try:
        nomor = int(tanya_teks("Nomor"))
        if nomor < 1 or nomor > len(daftar):
            raise IndexError(nomor)
    except ValueError:
        print("Nomornya harus angka!")
        return None
    except IndexError:
        print("Nomor itu nggak ada!")
        return None
    return nomor - 1

def kelola_tukang():
    while True:
        clear_screen()
        print("---( KELOLA TUKANG )---")
        print()
        tampil_tukang()
        print()
        sub = pilih_menu("Pilih", [("Tambah tukang", 1), ("Ubah tukang", 2), ("Ubah status tukang", 3), ("Kembali", 0)])
        if sub == 0:
            break
        elif sub == 1:
            nama = tanya_teks("Nama tukang").strip()
            nama_ada = False
            for t in tukang:
                if t["nama"] == nama:
                    nama_ada = True
            if nama == "":
                print("Nama nggak boleh kosong!")
            elif nama_ada == True:
                print("Nama tukang sudah ada!")
            else:
                tukang.append({"nama": nama, "status": status_tukang[0]})
                print("Tukang", nama, "udah ditambah!")
            enter()
        elif sub == 2:
            if len(tukang) == 0:
                print("Belum ada tukang!")
                enter()
                continue
            idx = ambil_nomor(tukang)
            if idx is None:
                enter()
                continue
            nama = tanya_teks("Nama baru").strip()
            nama_ada = False
            for i in range(len(tukang)):
                if i != idx and tukang[i]["nama"] == nama:
                    nama_ada = True
            if nama == "":
                print("Nama nggak boleh kosong!")
            elif nama_ada == True:
                print("Nama tukang sudah ada!")
            else:
                tukang[idx]["nama"] = nama
                print("Data tukangnya udah diubah!")
            enter()
        elif sub == 3:
            if len(tukang) == 0:
                print("Belum ada tukang!")
                enter()
                continue
            idx = ambil_nomor(tukang)
            if idx is None:
                enter()
                continue
            status = pilih_menu("Status baru", list(status_tukang))
            tukang[idx]["status"] = status
            print("Status", tukang[idx]["nama"], "udah jadi", status)
            enter()

def cari_tukang_siap():
    return

def lihat_tukang():
    clear_screen()
    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama", "Status"]
    for i in range(len(tukang)):
        tabel.add_row([i + 1, tukang[i]["nama"], tukang[i]["status"]])
    if len(tabel.rows) == 0:
        print("Belum ada tukang.")
    else:
        print(tabel)
    enter()