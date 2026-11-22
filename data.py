users = [
    {"username": "admin", "password": "akuadminkaumember", "role": "admin"},
    {"username": "yanto", "password": "000", "role": "pelanggan"},
]
paket = [
    {"nama": "Paket Furnitur", "harga": 1000, "fitur": 10, "sedia": True},
    {"nama": "Paket Seruangan", "harga": 1900, "fitur": 8, "sedia": True},
    {"nama": "Paket Indoor", "harga": 3100, "fitur": 5, "sedia": True},
    {"nama": "Paket Outdoor", "harga": 3500, "fitur": 0, "sedia": False},
    {"nama": "Paket Renovasi Rumah", "harga": 5000, "fitur": 1, "sedia": True},
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