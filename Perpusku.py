import json
from json import encoder
import os
from datetime import datetime as dt
fileku = 'datapengguna.json'
filebuku = 'daftarbuku.json'
filepinjam = 'daftarpinjam.json'
data_pengguna = []
data_buku = []
data_pinjam = []
pengguna = []
def clear() :
    os.system('cls')
def menu_login() :
    while True :
        print('-'*30)
        print('{0:^30s}'.format('PERPUSKU'))
        print('-'*30)
        print('{0:^30s}'.format('-'*20))
        print('{0:^30s}'.format('|     1. LOGIN     |'))
        print('{0:^30s}'.format('-'*20))
        print('{0:^30s}'.format('-'*20))
        print('{0:^30s}'.format('|     2. DAFTAR    |'))
        print('{0:^30s}'.format('-'*20))
        print('\n')
        pilih = int(input('pilih menu :'))
        if (pilih == 1) :
            login()
        elif(pilih == 2) :
            daftar()
        else :
            print('Maaf menu tidak tersedia')
            clear()
                
def daftar() :
    clear()
    print('{0:^30}'.format('DAFTAR'))
    print('='*30)
    with open (fileku, 'r') as file :
        data_pengguna = json.load(file)
        for x in file :
            data_pengguna.append(x)
    while True :
        data = dict()
        data ['username'] = input('Username :')
        data ['password'] = input('Password :')
        data ['password2'] = input('Re-type Password :')
        if (data['password']==data['password2']) :
            data_pengguna.append(data)
            break
        else :
            print('password tidak sama')

    with open (fileku, 'w') as file :
        json.dump(data_pengguna, file, indent=2)
    print('Akun berhasil dibuat')
def login() :
    clear()
    print('{0:^30s}'.format('LOGIN'))
    print('='*30)
    try :
        while True :
            with open (fileku, 'r') as file :
                data_pengguna = json.load(file)
                nama = input('Username :')
                pas = input('Password :')
                pengguna.append(nama)
                for x in range(len(data_pengguna)) :
                    if (nama == data_pengguna[x]['username'] and pas == data_pengguna[x]['password']) :
                        menu_utama()
                        break
                print('Username atau Passowrd salah')
    except IOError as e :
        print(e)
def menu_utama():
    clear()
    while True :
        print('='*30)
        print('{0:^30s}'.format('PERPUSKU'))
        print('-'*30)
        print('{0:^30s}'.format('SELAMAT DATANG'))
        print('{0:^30s}'.format(pengguna[0]))
        print('='*30)
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|       1. Daftar buku       |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|    2. Tambah daftar buku   |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|  3. Daftar buku dipinjam   |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|       4. Pinjami buku      |'))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('-'*30))
        print('{0:^30s}'.format('|          5. KELUAR         |'))
        print('{0:^30s}'.format('-'*30))
        print('\n')
        item = int(input('Pilih menu :'))
        if (item == 1) :
            daftar_buku()
        elif (item == 2) :
            tambah_buku()
        elif (item == 3) :
            daftar_pinjam()
        elif (item == 4) :
            pinjami() 
        elif (item==5) :
            exit()
        else :
            print('Menu tidak tersedia')

def daftar_buku() :
    clear()
    print('{0:^76s}'.format('DAFTAR BUKU'))
    print('='*76)
    print('{0:3s}{1:16s}{2:16s}{3:16s}{4:6s}    {5:12s}'.format(('NO'),('Judul Buku'),('Penulis'),('Penerbit'),('Kode buku'),('Jmlh Halaman')))
    print('-'*76)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
        for a in range(len(data_buku)) :
            print('{0:1d}  {1:16s}{2:16s}{3:16s}{4:6s}  {5:8d}'.format((a+1),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku'],data_buku[a]['tebal']))
    print('\n')
    print('MENU :  1. Tambah daftar    2. Hapus daftar    3. Kembali    4. Urutkan')
    menudaftar = int(input('Pilih menu :'))
    if menudaftar == 1 :
        tambah_buku()
    if menudaftar == 2 :
        hapus_buku()
    if menudaftar == 3 :
        menu_utama()
    if menudaftar == 4 :
        print('Urut berdasar :')
        print('1. Jumlah halaman terbesar')
        print('2. Jumlah halaman terkecil')
        print('3. Abjad awal')
        print('4. Abjad akhir')
        urut = int(input('Pilih menu :'))
        if  urut == 1 :
            urut_halnyak()
        if urut == 2 :
            urut_halkit()
        if urut == 3 :
            urut_abwal()
        if urut == 4 :
            urut_abkhir()

def tambah_buku() :
    clear()
    print('{0:^60s}'.format('TAMBAH BUKU'))
    print('='*60)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
    buku = dict()
    buku ['judul buku'] = input('Masukkan judul buku :') 
    buku ['penulis'] = input('Masukkan nama penulis :')
    buku ['penerbit'] = input('Masukkan nama penerbit :')
    buku ['kode buku'] = input('Masukkan kode buku (4 digit) :')
    buku ['tebal'] = int(input('Masukkan jumlah halaman buku :'))
    data_buku.append(buku)
    with open (filebuku, 'w') as file :
        json.dump(data_buku, file, indent=2)
    print('Buku berhasil ditambahkan')
    input('Tekan ENTER untuk kembali')
    menu_utama()
def hapus_buku() :
    clear()
    print('{0:^60s}'.format('HAPUS BUKU'))
    print('='*60)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
        for a in range(len(data_buku)) :
            print('{0:1d} {1:16s}{2:16s}{3:16s}{4:4s}'.format((a+1),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku']))
    print('\n')
    hapus = int(input('Masukkan nomor daftar yang ingin dihapus :'))
    hapus -= 1
    del data_buku[hapus]
    with open (filebuku, 'w') as file :
        json.dump(data_buku, file, indent=2)
    print ('Daftar berhasil dihapus')
    input('Tekan ENTER untuk kembali')
    menu_utama()
def daftar_pinjam() :
    clear()
    print('{0:^100s}'.format('DAFTAR BUKU DIPINJAM'))
    print('='*100)
    print('{0:4s}{1:17s}{2:12s}{3:21s}{4:17s}{5:18s}{6:12s}'.format(('NO'),('Nama Peminjam'),('Tanggal'),('Judul buku'),('Penulis'),('Penerbit'),('Kode buku')))
    print('-'*100)
    with open (filepinjam, 'r') as file :
        data_pinjam = json.load(file)
        for a in range(len(data_pinjam)) :
            print('{0:1d}   {1:17s}{2:12s}{3:21s}{4:17s}{5:18s}{6:12s}'.format((a+1), data_pinjam[a]['nama peminjam'], data_pinjam[a]['tanggal'], data_pinjam[a]['judul buku'], data_pinjam[a]['penulis'], data_pinjam[a]['penerbit'], data_pinjam[a]['kode buku']))
    print('\n')
    print('MENU :  1. Tambah daftar    2. Hapus daftar    3. Kembali')
    pilih = int(input('Pilih menu :'))
    if pilih == 1 :
        pinjami()
    if pilih == 2 :
        hapus_pinjam()
    if pilih == 3 :
        menu_utama()
def pinjami() :
    clear()
    print('{0:^60s}'.format('PINJAMI BUKU'))
    print('='*60)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
        for a in range(len(data_buku)) :
            print('{0:1d}  {1:16s}{2:16s}{3:16s}{4:4s}'.format((a+1),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku']))
    print('\n')
    with open (filepinjam, 'r') as file :
        data_pinjam = json.load(file)
    pinjam = dict()
    pinjam ['nama peminjam'] = input('Masukkan nama peminjam :')
    pinjam ['tanggal'] = dt.now().strftime('%Y-%m-%d')
    pinjam ['judul buku'] = input('Masukkan judul buku :')
    pinjam ['penulis'] = input('Masukkan nama penulis buku :')
    pinjam ['penerbit'] = input('Masukkan nama penerbit buku :')
    pinjam ['kode buku'] = input('Masukkan kode buku (4 digit) :')
    data_pinjam.append(pinjam)
    with open (filepinjam, 'w') as file :
        json.dump(data_pinjam, file, indent=2)
    print('Data peminjaman berhasil disimpan')
    input('Tekan ENTER untuk kembali')
    menu_utama()
def hapus_pinjam() :
    clear()
    print('{0:^100s}'.format('HAPUS BUKU YANG DIPINJAM'))
    print('='*100)
    with open (filepinjam, 'r') as file :
        data_pinjam = json.load(file)
        for a in range(len(data_pinjam)) :
            print('{0:1d}   {1:17s}{2:12s}{3:21s}{4:17s}{5:18s}{6:12s}'.format((a+1), data_pinjam[a]['nama peminjam'], data_pinjam[a]['tanggal'], data_pinjam[a]['judul buku'], data_pinjam[a]['penulis'], data_pinjam[a]['penerbit'], data_pinjam[a]['kode buku']))
    print('\n')
    hapus = int(input('Masukkan nomer daftar yang akan dihapus :'))
    hapus -= 1
    del data_pinjam[hapus]
    with open (filepinjam, 'w') as file :
        json.dump(data_pinjam, file, indent=2)
    print('Daftar berhasil dihapus')
    input('Tekan ENTER untuk kembali')
    menu_utama()

def urut_halnyak() :
    clear()
    print('{0:^76s}'.format('DAFTAR BUKU'))
    print('='*76)
    print('{0:3s}{1:16s}{2:16s}{3:16s}{4:6s}    {5:12s}'.format(('NO'),('Judul Buku'),('Penulis'),('Penerbit'),('Kode buku'),('Jmlh Halaman')))
    print('-'*76)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
    angka = 0
    for a in range(len(data_buku)-1,-1,-1):
        angka += 1
        for j in range(a) :
            if data_buku[j]["tebal"] > data_buku[j+1]["tebal"]:
                temp = data_buku[j]
                data_buku[j] = data_buku[j+1]
                data_buku[j+1] = temp
        print('{0:1d}  {1:16s}{2:16s}{3:16s}{4:6s}  {5:8d}'.format((angka),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku'],data_buku[a]['tebal']))
    print('\n')
    print('MENU :  1. Tambah daftar    2. Hapus daftar    3. Kembali    4. Urutkan')
    menudaftar = int(input('Pilih menu :'))
    if menudaftar == 1 :
        tambah_buku()
    if menudaftar == 2 :
        hapus_buku()
    if menudaftar == 3 :
        menu_utama()
    if menudaftar == 4 :
        print('Urut berdasar :')
        print('1. Jumlah halaman terbesar')
        print('2. Jumlah halaman terkecil')
        print('3. Abjad awal')
        print('4. Abjad akhir')
        urut = int(input('Pilih menu :'))
        if  urut == 1 :
            urut_halnyak()
        if urut == 2 :
            urut_halkit()
        if urut == 3 :
            urut_abwal()
        if urut == 4 :
            urut_abkhir()

def urut_halkit() :
    clear()
    print('{0:^76s}'.format('DAFTAR BUKU'))
    print('='*76)
    print('{0:3s}{1:16s}{2:16s}{3:16s}{4:6s}    {5:12s}'.format(('NO'),('Judul Buku'),('Penulis'),('Penerbit'),('Kode buku'),('Jmlh Halaman')))
    print('-'*76)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
    angka = 0
    for a in range(len(data_buku)-1,-1,-1):
        angka += 1
        for j in range(a) :
            if data_buku[j]["tebal"] < data_buku[j+1]["tebal"]:
                temp = data_buku[j]
                data_buku[j] = data_buku[j+1]
                data_buku[j+1] = temp
        print('{0:1d}  {1:16s}{2:16s}{3:16s}{4:6s}  {5:8d}'.format((angka),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku'],data_buku[a]['tebal']))
    print('\n')
    print('MENU :  1. Tambah daftar    2. Hapus daftar    3. Kembali    4. Urutkan')
    menudaftar = int(input('Pilih menu :'))
    if menudaftar == 1 :
        tambah_buku()
    if menudaftar == 2 :
        hapus_buku()
    if menudaftar == 3 :
        menu_utama()
    if menudaftar == 4 :
        print('Urut berdasar :')
        print('1. Jumlah halaman terbesar')
        print('2. Jumlah halaman terkecil')
        print('3. Abjad awal')
        print('4. Abjad akhir')
        urut = int(input('Pilih menu :'))
        if  urut == 1 :
            urut_halnyak()
        if urut == 2 :
            urut_halkit()
        if urut == 3 :
            urut_abwal()
        if urut == 4 :
            urut_abkhir()

def urut_abwal() :
    clear()
    print('{0:^76s}'.format('DAFTAR BUKU'))
    print('='*76)
    print('{0:3s}{1:16s}{2:16s}{3:16s}{4:6s}    {5:12s}'.format(('NO'),('Judul Buku'),('Penulis'),('Penerbit'),('Kode buku'),('Jmlh Halaman')))
    print('-'*76)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
    angka = 0
    for a in range(len(data_buku)-1,-1,-1):
        angka += 1
        for j in range(a) :
            if data_buku[j]["judul buku"] < data_buku[j+1]["judul buku"]:
                temp = data_buku[j]
                data_buku[j] = data_buku[j+1]
                data_buku[j+1] = temp
        print('{0:1d}  {1:16s}{2:16s}{3:16s}{4:6s}  {5:8d}'.format((angka),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku'],data_buku[a]['tebal']))
    print('\n')
    print('MENU :  1. Tambah daftar    2. Hapus daftar    3. Kembali    4. Urutkan')
    menudaftar = int(input('Pilih menu :'))
    if menudaftar == 1 :
        tambah_buku()
    if menudaftar == 2 :
        hapus_buku()
    if menudaftar == 3 :
        menu_utama()
    if menudaftar == 4 :
        print('Urut berdasar :')
        print('1. Jumlah halaman terbesar')
        print('2. Jumlah halaman terkecil')
        print('3. Abjad awal')
        print('4. Abjad akhir')
        urut = int(input('Pilih menu :'))
        if  urut == 1 :
            urut_halnyak()
        if urut == 2 :
            urut_halkit()
        if urut == 3 :
            urut_abwal()
        if urut == 4 :
            urut_abkhir()

def urut_abkhir() :
    clear()
    print('{0:^76s}'.format('DAFTAR BUKU'))
    print('='*76)
    print('{0:3s}{1:16s}{2:16s}{3:16s}{4:6s}    {5:12s}'.format(('NO'),('Judul Buku'),('Penulis'),('Penerbit'),('Kode buku'),('Jmlh Halaman')))
    print('-'*76)
    with open (filebuku, 'r') as file :
        data_buku = json.load(file)
    angka = 0
    for a in range(len(data_buku)-1,-1,-1):
        angka += 1
        for j in range(a) :
            if data_buku[j]["judul buku"] > data_buku[j+1]["judul buku"]:
                temp = data_buku[j]
                data_buku[j] = data_buku[j+1]
                data_buku[j+1] = temp
        print('{0:1d}  {1:16s}{2:16s}{3:16s}{4:6s}  {5:8d}'.format((angka),data_buku[a]['judul buku'],data_buku[a]['penulis'],data_buku[a]['penerbit'],data_buku[a]['kode buku'],data_buku[a]['tebal']))
    print('\n')
    print('MENU :  1. Tambah daftar    2. Hapus daftar    3. Kembali    4. Urutkan')
    menudaftar = int(input('Pilih menu :'))
    if menudaftar == 1 :
        tambah_buku()
    if menudaftar == 2 :
        hapus_buku()
    if menudaftar == 3 :
        menu_utama()
    if menudaftar == 4 :
        print('Urut berdasar :')
        print('1. Jumlah halaman terbesar')
        print('2. Jumlah halaman terkecil')
        print('3. Abjad awal')
        print('4. Abjad akhir')
        urut = int(input('Pilih menu :'))
        if  urut == 1 :
            urut_halnyak()
        if urut == 2 :
            urut_halkit()
        if urut == 3 :
            urut_abwal()
        if urut == 4 :
            urut_abkhir()
menu_login()
