from data import MAKS_TOPUP
from helper import clear_screen, enter, minta_angka

def jumlah_saldo(user_login):
    clear_screen()
    print("---( JUMLAH SALDO )---")
    print()
    try:
        saldo = user_login["saldo"]
    except KeyError:
        print("Data akun tidak ditemukan!")
    else:
        print("Saldo Anda: Rp", saldo)
    finally:
        enter()

def topup_saldo(user_login):
    clear_screen()
    print("---( TOP UP SALDO )---")
    print()
    print("Saldo kamu sekarang : Rp", user_login["saldo"])
    print("Nominal maksimal top up saldo : Rp", MAKS_TOPUP)
    print()
    nominal = minta_angka("Nominal top up (0 = batal) : ", 0, MAKS_TOPUP)
    if nominal == 0:
        print("Top up dibatalkan.")
    else:
        user_login["saldo"] += nominal
        print("Top up berhasil!")
        print("Saldo sekarang : Rp", user_login["saldo"])
    enter()