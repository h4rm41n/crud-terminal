import pandas as pd
import requests
import func

data_pegawai = []
data_pegawai.append({
   "nama":"Budi",
   "nip":"123",
   "kelamin":"Laki"
})

while True:
   print("*********************")
   print("*Menu program       *")
   print("*===================*")
   print("*1. List pegawai    *")
   print("*2. Tambah pegawai  *")
   print("*3. Delete pegawai  *")
   print("*4. Requests data JSON  *")
   print("*0. Close program   *")
   print("*********************")

   menu = raw_input("Pilih menu : ")
   if menu=="1":
      func.bersihkan_layar()
      func.list_pegawai(data_pegawai)
   elif menu=="2":
      func.bersihkan_layar()
      data_pegawai.append(func.tambah_pegawai(data_pegawai))
   elif menu=="3":
      func.bersihkan_layar()
      func.hapus_pegawai(data_pegawai)
   elif menu=="0":
      func.bersihkan_layar()
      break
   elif menu=="4":
      url = "https://jsonplaceholder.typicode.com/posts"
      data = requests.get(url).json()
      userId = []
      id = []
      title = []
      body = []
      
      for x in range(len(data)):
         userId.append(data[x]['userId'])
         id.append(data[x]['id'])
         title.append(data[x]['title'])
         body.append(data[x]['body'])

      raw_data = {
         "userId":userId,
         "id":id,
         "title":title,
         "body":body,
      }
      
      df = pd.DataFrame(raw_data, columns = ['userId', 'id', 'title', 'body'])
      df.to_csv('example.csv')

print("Program ditutup, thanks!")