# Program Management Kontak
import function

# List of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Djalu",
    "email": "itz.djalu@gmail.com",
    "telepon":"089614209435"
})

# Menu program
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar Program")

    menu = input("Pilih menu: ")
    if menu == "0":
        break
    elif menu == "1":
        function.tampilkan_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.tambah_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("GK ADA")


print("bROT")