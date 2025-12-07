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
