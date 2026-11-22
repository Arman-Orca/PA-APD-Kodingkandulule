from helper import clear_screen, pilih_menu
from autentikasi import lihat_pengguna
from fiturtukang import kelola_tukang
from fiturpaket import kelola_paket
from fiturpesanan import buat_pesanan
def menu_admin():
    while True:
        clear_screen()
        print("---( MENU ADMIN )---")
        print()
        menu = pilih_menu("Pilih menunya bos",[
            ("Kelola tukang", 1),
            ("Kelola paket", 2),
            ("Kembali", 0)
        ] )
        if menu == 0:
            break
        elif menu == 1:
            kelola_tukang()
        elif menu == 2:
            kelola_paket()
def menu_pelanggan(user_login):
    while True:
        clear_screen()
        print("---( MENU PELANGGAN )---")
        print()
        menu = pilih_menu("Pilih menunya",[
            ("Buat pesanan", 1),
            ("Kembali", 0)
        ] )
        if menu == 0:
            break
        elif menu == 1:
            buat_pesanan(user_login)