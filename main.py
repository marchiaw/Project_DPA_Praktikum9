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
