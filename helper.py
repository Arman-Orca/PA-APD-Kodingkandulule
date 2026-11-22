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