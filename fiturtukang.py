from helper import clear_screen, enter
from data import tukang

def lihat_tukang():
    clear_screen()
    print("---( TUKANG YANG SIAP )---")
    ada = False
    for t in tukang:
        if t["status"] == "Siap kerja":
            print("-", t["nama"])
            ada = True
    if ada == False:
        print("Tukang Sibuk")
    enter()
