def tambah():
    print("\n=== Tambah Data Karyawan ===")

    nama = str(input("Nama: ")).strip()
    jabatan = str(input("Jabatan: ")).strip()
     while True:
        try:
            gaji = int(input("Gaji: ").strip())
            break
        except ValueError:
            print("Gaji harus berupa angka. Coba lagi.")
    status = str(input("Status (aktif / non-aktif): ")).strip()

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

            nama = str(input("Nama baru: ")).strip()
            jabatan = str(input("Jabatan baru: ")).strip()
            while True:
                try:
                    gaji = int(input("Gaji: ").strip())
                    break
                except ValueError:
                    print("Gaji harus berupa angka. Coba lagi.")
            status = str(input("Status baru: ")).strip()

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
        
def hapus():
    tampil()
    if len(data) == 0:
        return
    id_cari = input("Masukkan ID yang mau dihapus: ").strip()
    id_cari = int(id_cari)

    ketemu = False
    for d in data:
        if d["id"] == id_cari:
            ketemu = True
            data.remove(d)
            print("Data dihapus.\n")
            break
    if ketemu == False:
        print("ID tidak ditemukan.\n")

def cari():
    print("\n=== Menu Pencarian ===")
    print("1. Cari berdasarkan nama")
    print("2. Filter berdasarkan jabatan")
    print("3. Filter berdasarkan status")
    print("4. Kembali")

    pilih = input("Pilih menu: ").strip()

    if pilih == "1":
        q = input("Masukkan nama: ").strip().lower()
        ketemu = False
        for d in data:
            if q in d["nama"].lower().strip():
                ketemu = True
                print("[" + str(d["id"]) + "] " +
                      d["nama"] + " | " +
                      d["jabatan"] + " | " +
                      d["gaji"] + " | " +
                      d["status"])
        if ketemu == False:
            print("Tidak ditemukan.\n")
    elif pilih == "2":
        q = input("Masukkan jabatan: ").strip().lower()

        ketemu = False
        for d in data:
            if q == d["jabatan"].lower().strip():
                ketemu = True
                print("[" + str(d["id"]) + "] " +
                      d["nama"] + " | " +
                      d["jabatan"] + " | " +
                      d["gaji"] + " | " +
                      d["status"])
        if ketemu == False:
            print("Tidak ditemukan.\n")

    elif pilih == "3":
        q = input("Masukkan status (aktif / non-aktif): ").strip().lower()

        ketemu = False
        for d in data:
            if q == d["status"].lower().strip():
                ketemu = True
                print("[" + str(d["id"]) + "] " +
                      d["nama"] + " | " +
                      d["jabatan"] + " | " +
                      d["gaji"] + " | " +
                      d["status"])
        if ketemu == False:
            print("Tidak ditemukan.\n")
    else:
        return
        
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
