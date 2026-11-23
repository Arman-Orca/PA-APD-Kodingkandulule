from helper import clear_screen, pilih_menu
from autentikasi import lihat_pengguna
from fiturtukang import kelola_tukang, lihat_tukang
from fiturpaket import kelola_paket
from fiturpesanan import buat_pesanan
from fitursaldo import topup_saldo, jumlah_saldo

def menu_admin():
    while True:
        clear_screen()
        print("---( Yang Atmin Atmin Aja )---")
        print()
        menu = pilih_menu("Pilih menunya bos", [
            ("Kelola Tukang", 1),
            ("Kelola Paket", 2),
            ("Total Pendapatan", 3),
            ("lihat_pengguna", 4),
            ("Tandai Selesai", 5),
            ("Status Pembayaran", 6),
            ("Logout", 0),
        ])
        if menu == 0:
            break
        elif menu == 1:
            kelola_tukang()
        elif menu == 2:
            kelola_paket()
        elif menu == 3:
            print("belum dibikin")
        elif menu == 4:
            lihat_pengguna()
        elif menu == 5:
            print("belum dibikin")
        elif menu == 6:
            print("belum dibikin")
            
def menu_pelanggan(user_login):
    while True:
        clear_screen()
        print("---( MENU PELANGGAN )---")
        menu = pilih_menu("Pilih menu", [
            ("Lihat Tukang", 1),
            ("Lihat Status", 2),
            ("Buat Pesanan", 3),
            ("Jumlah Saldo", 4),
            ("Top Up Saldo", 5),
            ("Pembayaran", 6),
            ("Hapus Lokasi Pesanan", 7),
            ("Logout", 0),
        ])
        if menu == 0:
            break
        elif menu == 1:
            lihat_tukang()
        elif menu == 2:
            print("belum dibikin")
        elif menu == 3:
            buat_pesanan()
        elif menu == 4:
            jumlah_saldo(user_login)
        elif menu == 5:
            topup_saldo(user_login)
        elif menu == 6:
            print("belum dibikin")
        elif menu == 7:
            print("belum dibikin")