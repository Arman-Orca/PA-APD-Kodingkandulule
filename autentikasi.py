from data import users
from helper import clear_screen, enter, tanya_teks
def validasi_akun(username, password):
    if username == "":
        raise ValueError("Namamu masih kosong bos!")
    for u in users:
        if u["username"] == username:
            raise ValueError("Ganti nama lain, udah ada yang make")
    if len(password) < 3:
        raise ValueError("Password minimal 3 karakter!")
def cari_user(username, password):
    for u in users:
        if u["username"] == username and u["password"] == password:
            return u
    return {}
def register():
    clear_screen()
    print("---( BUAT AKUN BARU )---")
    print()
    username_baru = tanya_teks("Username")
    password_baru = tanya_teks("Password", True)
    try:
        validasi_akun(username_baru, password_baru)
    except ValueError as e:
        print(e)
    else:
        users.append({"username": username_baru, "password": password_baru, "role": "pelanggan"})
        print("Register berhasil bos, silakan login.")
    finally:
        enter()
def login():
    clear_screen()
    print("---( LOGIN )---")
    print()
    username = tanya_teks("Username")
    password = tanya_teks("Password", True)
    user_login = cari_user(username, password)
    if len(user_login) == 0:
        print("Username atau password salah!")
        enter()
    return user_login
def lihat_pengguna():
    clear_screen()
    print("---( DAFTAR PENGGUNA )---")
    for i in range(len(users)):
        print(i + 1, ".", users[i]["username"], "(", users[i]["role"], ")")
    enter()