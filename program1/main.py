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