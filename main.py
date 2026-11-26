from helper import clear_screen, pilih_menu
from autentikasi import register, login
from menu import menu_admin, menu_pelanggan

def main():
    try:
        while True:
            clear_screen()
            print("---( Jasa Renovasi Rumah )---")
            print()
            pilih = pilih_menu("Pilih menu", [("Login", 1), ("Buat Akun Baru", 2), ("Keluar", 0)])
            if pilih == 0:
                print()
                print("Tengkyu bos!")
                break
            elif pilih == 1:
                user_login = login()
                if len(user_login) > 0:
                    if user_login["role"] == "admin":
                        menu_admin()
                    else:
                        menu_pelanggan(user_login)
            else:
                register()
    except (KeyboardInterrupt, EOFError):
            print()
            print("Program dihentikan. Tengkyu bos!")

main()