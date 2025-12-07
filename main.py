# Fungsi Tambah Data

def tambah():
    print("\n=== Tambah Data Karyawan ===")

    nama = input("Nama: ").strip()
    jabatan = input("Jabatan: ").strip()
    gaji = input("Gaji: ").strip()
    status = input("Status (aktif / non-aktif): ").strip()

    if len(data) == 0:
        id_baru = 1
    else:
        id_baru = data[-1]["id"] + 1

    karyawan = {
        "id": id_baru,
        "nama": nama,
        "jabatan": jabatan,
        "gaji": gaji,
        "status": status
    }

    data.append(karyawan)
    print("Data berhasil ditambahkan.\n")

# Fungsi Tampilkan Data

def tampil():
    print("\n=== Daftar Karyawan ===")
    if len(data) == 0:
        print("Belum ada data.\n")
    else:
        for d in data:
            print("[" + str(d["id"]) + "] " +
                  d["nama"] + " | " +
                  d["jabatan"] + " | " +
                  d["gaji"] + " | " +
                  d["status"])
        print()
# Fungsi Edit Data

def edit():
    tampil()

    if len(data) == 0:
        return

    id_cari = input("Masukkan ID yang mau diedit: ").strip()
    id_cari = int(id_cari)

    ketemu = False
    for d in data:
        if d["id"] == id_cari:
            ketemu = True

            print("Kosongkan jika tidak ingin mengubah.")

            nama = input("Nama baru: ").strip()
            jabatan = input("Jabatan baru: ").strip()
            gaji = input("Gaji baru: ").strip()
            status = input("Status baru: ").strip()

            if nama != "":
                d["nama"] = nama
            if jabatan != "":
                d["jabatan"] = jabatan
            if gaji != "":
                d["gaji"] = gaji
            if status != "":
                d["status"] = status

            print("Data berhasil diupdate.\n")
            break

    if ketemu == False:
        print("ID tidak ditemukan.\n")

# Menu yang Utama

while True:
    print("==== Sistem Pendataan Karyawan ====")
    print("1. Tampilkan data")
    print("2. Tambah data")
    print("3. Edit data")
    print("4. Hapus data")
    print("5. Cari / Filter data")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ").strip()

    if menu == "1":
        tampil()
    elif menu == "2":
        tambah()
    elif menu == "3":
        edit()
    elif menu == "4":
        hapus()
    elif menu == "5":
        cari()
    elif menu == "6":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.\n")
