from helper import clear_screen, pilih_menu
from autentikasi import lihat_pengguna, users
from fiturtukang import lihat_tukang
from tampilan import tampil_tukang

def menu_admin():
    while True:
        clear_screen()
        print("---( Yang Atmin Atmin Aja )---")
        print()
        menu = pilih_menu("Pilih menunya bos", [
            ("Kelola Tukang", 1),
            ("Kelola Paket", 2),
            ("Lihat Ringkasan", 3),
            ("Tandai Selesai", 4),
            ("Status Pembayaran", 5),
            ("Logout", 0),
        ])
        if menu == 0:
            break
        elif menu == 1:
            kelola_tukang()
        elif menu == 2:
            kelola_paket()
        elif menu == 3:
            lihat_ringkasan()
        elif menu == 4:
            tandai_selesai()
        else:
            status_pembayaran()

def menu_pelanggan():
    while True:
        clear_screen()
        print("---( MENU PELANGGAN )---")
        menu = pilih_menu("Pilih menu", [
            ("Lihat Tukang", 1),
            ("Pesan Tukang", 2),
            ("Lihat Status", 3),
            ("Jumlah Saldo", 4),
            ("Top Up Saldo", 5),
            ("Pembayaran", 6),
            ("Hapus Data Pesanan", 7),
            ("Logout", 0),
        ])
        if menu == 0:
            break
        elif menu == 1:
            lihat_tukang ()
        elif menu == 2:
            pesan_tukang()
        elif menu == 3:
            lihat_status()
        elif menu == 4:
            jumlah_saldo()
        elif menu == 5:
            topup_saldo()
        elif menu == 6:
            pembayaran()
        else:
            hapus_data_pesanan()

menu_pelanggan()