import os

def bersihkan_layar():
   os.system("clear")

def list_pegawai(data):
   if len(data)==0:
      print("Data pegawai kosong!")
   else:
      for pegawai in data:
         print("******========================")
         print("NIP       = "+pegawai['nip'])
         print("Nama      = "+pegawai['nama'])
         print("Kelamin   = "+pegawai['kelamin'])
         print("========================******")

def tambah_pegawai(data):
   nip = input("Masukkan nip = ")
   
   if cari_pegawai(nip, data):
      print("maaf nip "+nip+" sudah terdaftar!")
   else:
      nama = input("Masukkan nama = ")
      kelamin = input("Masukkan kelamin L/P = ")

      pegawai = {
         "nama":nama,
         "nip":nip,
         "kelamin":kelamin
      }

      return pegawai

def hapus_pegawai(data):
   nip = input("Masukkan NIP yang akan dihapus = ")

   index = -1
   for idx in range(len(data)):
      if nip==data[idx]['nip']:
         index=idx
         break

   if index==-1:
      print("data "+nip+" tidak ditemukan")
   else:
      del data[index]
      print("data pegawai dengan nip "+nip+" telah dihapus")

def cari_pegawai(nip_key=None, data=None):
   
   for pegawai in data:
      if pegawai['nip'].find(nip_key) != -1:
         return True