from data import tukang, status_tukang
from helper import clear_screen, enter, minta_angka, pilih_menu, tanya_teks
from tampilan import tampil_tukang
def cari_tukang_siap():
    for t in tukang:
        if t["status"] == "Siap otw":
            return t
    return {}
def kelola_tukang():
    while True:
        clear_screen()
        print("---( KELOLA TUKANG )---")
        print()
        tampil_tukang(tukang, False)
        print()
        sub = pilih_menu("Pilih bos", [("Tambah tukang", 1), ("Ubah status tukang", 2), ("Hapus tukang", 3), ("Kembali", 0)])
        if sub == 0:
            break
        elif sub == 1:
            nama = tanya_teks("Nama tukang").strip()
            nama_ada = False  
            for t in tukang:
                if t["nama"] == nama:
                    nama_ada = True
            if nama == "":
                print("Mana namanya bos?")
            elif nama_ada == True:
                print("Nama tukang sudah ada bos!")
            else:
                tukang.append({"nama": nama, "status": status_tukang[0]})
                print("Tukang", nama, "udah ditambah!")
            enter()
 