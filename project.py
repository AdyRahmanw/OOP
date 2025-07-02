class user: #Setiap nama class diawali huruf Kapital.
    def __init__(self,nama_lengkap,email,no_telepon,nip,role):
        self.nama = nama_lengkap
        #email dan notelepon apakah harus semua user punya atau tidak? Pertimbangkan lagi apakah turunan dari user(admin dan kepsek) perlu email dan notelepon?
        self.email = email 
        self.no_telepon = no_telepon 
        self.nip = nip
        self.role = role
    
    def login(self):
        print(f"kosongan dulu")

    #Tambahkan method logout juga jika ada method login

class guru(user): #Setiap nama class diawali huruf Kapital.
    def __init__(self,nama_lengkap,email,no_telepon,nip,role,mapel,total_pendaaptan,jumlah_sesi):
        super().__init__(nama_lengkap,email,no_telepon,nip,role)
        self.mapel = mapel
        self.total_pendapatan = total_pendaaptan #Gunakan enkapsulapsi
        self.jumlah_sesi = jumlah_sesi
    
    def hitung_pendapatan_akhir(self):
        ...
    
    def hitung_jumlah_sesi(self):
        ...
    def get_info_dari_data_rekap(self):
        ...
     
class kepsek(user): #Setiap nama class diawali huruf Kapital.
    def __init__(self, nama_lengkap, email, no_telepon, nip, role,jabatan):
        super().__init__(nama_lengkap, email, no_telepon, nip, role)
        self.jabatan = jabatan
    
    def melihat_data_rekap(self): #Polymorpisme aja dari method lihat data rekap dari class guru
        ...
        
class admin(user): #Setiap nama class diawali huruf Kapital.
    def __init__(self, nama_lengkap, email, no_telepon, nip, role): #Kalau tidak ada atribut tambahan tidak perlu di-override methodnya.
        super().__init__(nama_lengkap, email, no_telepon, nip, role) 
    
    def melihat_data_rekap(self): #Polymorpisme aja dari method lihat data rekap dari class guru
        ...
    def menghapus_guru(self):
        ...
    def menambahkan_guru(self):
        ...
    def mengubah_data_rekap(self):      
        ...
#Pertimbangkan ada class untuk honorarium, berfungsi untuk menyimpan semua data dan behavior dari rekap sesi guru.
#Coba upload juga class diagramnya Adi
        
