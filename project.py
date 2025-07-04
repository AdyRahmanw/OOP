#Tambahkan anotasi disetiap parameter dan output method
#Mulai isi tiap fungsinya
""" 
Contoh: 
def hitung_angka(int: a, int: a) -> int:
    return a * a
def print_nilai(string: nama) -> None;
    print(f"hai {nama}")

"""

class User:
    def __init__(self,nama_lengkap,nip,role):
        self.nama = nama_lengkap
        self.nip = nip
        self.role = role
    
    def login(self):
        print(f"kosongan dulu")
        
    def logout(self):
        ...

#Terapkan enkapsulapsi pada atribut yang diperlukan
class Guru(User):
    def __init__(self,nama_lengkap,email,no_telepon,nip,role,mapel,total_pendaaptan,jumlah_sesi):
        super().__init__(nama_lengkap,nip,role)
        self.mapel = mapel
        self.total_pendapatan = total_pendaaptan
        self.jumlah_sesi = jumlah_sesi
        self.email = email
        self.no_telepon = no_telepon
    
    def hitung_pendapatan_akhir(self):
        ...
    
    def hitung_jumlah_sesi(self):
        ...
    def get_info_dari_data_rekap(self):
        ...
     
class Kepsek(Guru):
    def __init__(self, nama_lengkap, email, no_telepon, nip, role,jabatan):
        super().__init__(nama_lengkap, email, no_telepon, nip, role)
        self.jabatan = jabatan #Pertimbangkan kembali atribut jabatan perlu atau tidak.
    
    def melihat_data_rekap(self):
        ...
        
class Admin(User):
    def __init__(self, nama_lengkap,nip, role):
        super().__init__(nama_lengkap,nip, role)  
        #Jika sama persis atributnya, method tidak perlu di override.
    def melihat_data_rekap(self):
        ...
    def menghapus_guru(self):
        ...
    def menambahkan_guru(self):
        ...
    def mengubah_data_rekap(self):      
        ...

        
