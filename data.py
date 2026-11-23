users = [
    {"username": "admin", "password": "akuadmin", "role": "admin", "saldo": 0},
    {"username": "yanto", "password": "000", "role": "pelanggan", "saldo": 0},
]
paket = [   
    {"nama": "Paket Furnitur", "harga": 1000, "fitur": "perbaiki segala macam furnitur", "membutuhkan": "1 tukang", "sedia": True},
    {"nama": "Paket Seruangan", "harga": 1900, "fitur": "perbaiki seluruh ruangan", "membutuhkan": "2 tukang", "sedia": True},
    {"nama": "Paket Indoor", "harga": 3100, "fitur": "perbaiki segala ruangan didalam rumah", "membutuhkan": "3 tukang", "sedia": True},
    {"nama": "Paket Outdoor", "harga": 3500, "fitur": "perbaiki segala macam yang berada di outdoor", "membutuhkan": "2 tukang", "sedia": False},
    {"nama": "Paket Renovasi Rumah", "harga": 5000, "fitur": "perbaiki diluar dan didalam rumah", "membutuhkan": "5 tukang", "sedia": True},
]
tukang = [
    {"nama": "Yono", "status": "Sibuk"},
    {"nama": "Tungkris", "status": "Siap kerja"},
    {"nama": "Sutomo", "status": "Siap kerja"},
    {"nama": "Joko", "status": "Sibuk"},
    {"nama": "Slamet", "status": "Siap kerja"},
    {"nama": "Budi", "status": "Sibuk"},
    {"nama": "Sutrisno", "status": "Siap kerja"},
]
orders = []
nomor_order = 1
status_tukang = ("Siap kerja", "Sibuk")
MAKS_HARGA = 100000
MAKS_TOPUP = 1000000