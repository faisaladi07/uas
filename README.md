# Berikut hasil dari praktikum UAS pemograman - Python
## Dengan sturuktur sebagai berikut :
![gambar1](ssuas/prog.png)
* daftar_nilai.py berisi modul untuk tambah_data,ubah_data,hapus_data,dan cari_data
* view_nilai.py berisi modul untuk cetak_daftar_nilai,cetak_hasil_pencarian
* input_nilai.py berisi modul untuk input_data yang meminta pengguna memeasukan data
* main.py berisi program utama 
### Berikut penjelasanya 
- Berikut codingan untuk daftar_nilai.py
```python
from view.input_nilai import *

dataMahasiswa = {}


def tambah_data():
    global dataMahasiswa
    nama = input_nama()
    nim = input_nim()
    nilaiTugas = input_nilaiTugas()
    nilaiUts = input_nilaiUts()
    nilaiUas = input_nilaiUas()
    nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
    dataMahasiswa[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
    print("\nData Berhasil Ditambahkan!")
    return dataMahasiswa

def ubah_data():
    nama = input("Masukkan Nama: ")
    if nama in dataMahasiswa.keys():
        nim = input_nim()
        nilaiTugas = input_nilaiTugas()
        nilaiUts = input_nilaiUts()
        nilaiUas = input_nilaiUas()
        nilaiAkhir = (0.30 * nilaiTugas) + (0.35 * nilaiUts) + (0.35 * nilaiUas)
        dataMahasiswa[nama] = nim, nilaiTugas, nilaiUts, nilaiUas, nilaiAkhir
        print("\nData Berhasil Di Update!")
    else:
        print("Data tidak ditemukan!")


def hapus_data():
    nama = input("Masukkan Nama:  ")
    if nama in dataMahasiswa.keys():
        del dataMahasiswa[nama]
        print("Data",nama, "Telah dihapus!")
    else:
        print("Data Mahasiswa Tidak Ada".format(nama))
```

- Berikut codingan untuk cetak_nilai.py
```python
from model.daftar_nilai import *


def cetak_daftar_nilai():
    if dataMahasiswa.items():
        print("\n                      DAFTAR NILAI MAHASISWA                    ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        i = 0
        for x in dataMahasiswa.items():
            i += 1
            print("| {6:2} | {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print("==================================================================")
    else:
        print("\n                      DAFTAR NILAI MAHASISWA                    ")
        print("==================================================================")
        print("| No |     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir |")
        print("==================================================================")
        print("|                          TIDAK ADA DATA!                       |")
        print("==================================================================")


def cetak_hasil_pencarian():
    nama = input("Masukkan Nama        : ")
    if nama in dataMahasiswa.keys():
        print("\n                   DAFTAR NILAI MAHASISWA                   ")
        print("==============================================================")
        print("|     Nama     |    NIM    | Tugas |  UTS  |  UAS  |  Akhir  |")
        print("==============================================================")
        print("| {0:12s} | {1:9s} | {2:5} | {3:5} | {4:5} | {5:6}  |".format(nama, dataMahasiswa[nama][0], dataMahasiswa[nama][1], dataMahasiswa[nama][2], dataMahasiswa[nama][3], dataMahasiswa[nama][4]))
        print("==============================================================")
    else:
        print("Datanya {0} Tidak Ada ".format(nama))
```

- Berikut codingan  untuk input_nilai.py
```python
def input_nama():
    global nama
    nama = input("Masukkan Nama        : ")
    return nama


def input_nim():
    global nim
    nim = input("Masukkan NIM         : ")
    return nim


def input_nilaiTugas():
    global nilaiTugas
    nilaiTugas = int(input("Masukkan Nilai Tugas : "))
    return nilaiTugas


def input_nilaiUts():
    global nilaiUts
    nilaiUts = int(input("Masukkan Nilai UTS   : "))
    return nilaiUts


def input_nilaiUas():
    global nilaiUas
    nilaiUas = int(input("Masukkan Nilai UAS   : "))
    return nilaiUas
```

- Dan berikut adalah script untuk main.py
```python
from view.cetak_nilai import *


def menu():
    print('=====================================')
    print('Input Data Nilai Mahasiswa'.center(40))
    print('=====================================')
    print('|    1. Tambah Data                 |')
    print('|    2. Cari Data                   |')
    print('|    3. Tampilkan Data Mahasiswa    |')
    print('|    4. Ubah Data Mahasiswa         |')
    print('|    5. Hapus Data Mahasiswa        |')
    print('|    6. Selesai                     |')
    print('=====================================')


while True:
    menu()
    choose = input('Pilih Menu  : ')

    if choose == '1':
        tambah_data()
        input('Untuk pergi ke menu awal, tekan enter')

    elif choose == '2':
        cetak_hasil_pencarian()
        input('Untuk pergi ke menu awal, tekan enter')

    elif choose == '3':
        cetak_daftar_nilai()
        input('Untuk pergi ke menu awal, tekan enter')

    elif choose == '4':
        ubah_data()
        input('Untuk pergi ke menu awal, tekan enter')

    elif choose == '5':
        hapus_data()
        input('Untuk pergi ke menu awal, tekan enter')

    elif choose == '6':
        exit()

    else:
        print("Menu yang anda pilih tidak ada, Silahkan pilih menu yang tersedia")
```

![gambar2](ssuas/ss1.PNG)

* Diatas adalah hasil program ketika dirun, dan menampilkan menu utama

![gambar3](ssuas/ss2.PNG)
* Diatas adalah hasil ketika program dirun, dan menekan angka 1 pada keyboard, untuk menambah data

![gambar4](ssuas/ss3.PNG)
* Diatas adalah hasil program ketika dirun, dan menekan angka 2 pada keyboard, untuk mencari data dengan prompt masukkan nama yang ingin di cari

![gambar5](ssuas/ss4.PNG)
* Diatas adalah hasil ketika program dirun, dan menekan angka 1 pada keyboard, untuk melakukan penambahan data, disini kita tambahkan data riski


![gambar6](ssuas/ss5.PNG)
* Diatas adalah hasil ketika program dirun, dan menekan angka 3 pada keyboard, untuk melihat semua daftar data yang ada

![gambar7](ssuas/ss6.PNG)
* Diatas adalah hasil ketika program dirun, dan menekan angka 4 pada keyboard, untuk merubah data, disini kita ubah data nilai pada nama faisal adi titisno


![gambar8](ssuas/ss7.PNG)
* Dan untuk melihat apakah data telah terubah, maka kita menekan angka 3 pada keyboard, untuk melihat daftar data yang ada, disini sudah terlihat bahwa data faisal adi titisno sudah berubah nilai nya


![gambar9](ssuas/ss8.PNG)
* Dibawah adalah hasil ketika program dirun, dan menekan angka 5 pada keyboard, untuk perintah hapus data, dengan prompt masukkan nama data yang ingin di hapus, disini kita akan menghapus data dengan nama riski


![gambar10](ssuas/ss9.PNG)
* Dibawah adalah hasil ketika program dirun, dan maasukan angka 3 pada keyboard, untuk melihat daftar yang ada, karena adanya penghapusan data, apakah data dengan nama riski sudah terhapus atau belum


![gambar11](ssuas/ss10.PNG)
* Di atas adalah ketika program dijalankan, dan input angka 6 pada keyboard, untuk selesai atau keluar dari program
