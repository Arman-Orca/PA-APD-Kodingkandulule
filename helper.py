import os
import inquirer

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def enter():
    input("Tekan Enter...")

def tanya_teks(pesan, rahasia=False):
    if rahasia:
        pertanyaan = inquirer.Password("t", message=pesan)
    else:
        pertanyaan = inquirer.Text("t", message=pesan)
    hasil = inquirer.prompt([pertanyaan])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["t"]

def pilih_menu(pesan, pilihan):
    hasil = inquirer.prompt([inquirer.List("p", message=pesan, choices=pilihan)])
    if hasil is None:
        raise KeyboardInterrupt
    return hasil["p"]

def minta_angka(pesan, minimum, maksimum):
    while True:
            teks = input(pesan).strip()
            try:
                if not (teks.isascii() and teks.isdecimal()):
                    raise ValueError("Harus berupa angka bulat bos!")
                nilai = int(teks)
                if nilai < minimum or nilai > maksimum:
                    raise ValueError("Angkanya harus antara " + str(minimum) + " sampai " + str(maksimum) + " bos!")
            except ValueError as e:
                print(e)
            else:
                return nilai

def minta_teks(pesan, boleh_kosong=False):
    while True:
        teks = tanya_teks(pesan).strip()
        if teks or boleh_kosong:
            return teks
        print("Tidak boleh kosong!")