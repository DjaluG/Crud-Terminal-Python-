# Program Management Kontak

def tampilkan_kontak(daftar_kontak):
    for kontak  in daftar_kontak:
        print("===================================")
        print(f"Nama    : {kontak['nama']}")
        print(f"Email   : {kontak['email'] }")
        print(f"Telepon : {kontak['telepon']}")
        print("===================================")

def tambah_kontak():
    nama = input("Nama  : ")
    email = input("Email  : ")
    telepon = input("Telepon  : ")
    kontak = {
        "nama":nama,
        "email":email,
        "telepon":telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input('No telepon yang akan di hapus: ')
    index = -1
    for i in range (0, len(daftar_kontak)):
        kontak= daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("data kontak tidak di temukan")
    else:
        del daftar_kontak[index]
        print("data kontak berhasil dihapus")

def cari_kontak(daftar_kontak):
    nama_yang_dicari = input("Nama yang di cari : ")

    for kontak in daftar_kontak:
        nama = kontak["nama"].lower()
        if nama.find(nama_yang_dicari.lower()) != -1:
            print("===================================")
            print(f"Nama    : {kontak['nama']}")
            print(f"Email   : {kontak['email'] }")
            print(f"Telepon : {kontak['telepon']}")
            print("===================================")