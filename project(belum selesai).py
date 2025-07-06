class User:
    def __init__(self,nama_lengkap,nip,role):
        self.nama = nama_lengkap
        self.nip = nip
        self.role = role
    
    def login(self):
        ...
        
    def logout(self):
        ...
        
class Guru(User):
    def __init__(self,nama_lengkap,email,no_telepon,nip,role,mapel,total_pendapatan,jumlah_sesi):
        super().__init__(nama_lengkap,nip,role)
        self.mapel = mapel
        self.__total_pendapatan = total_pendapatan
        self.jumlah_sesi = jumlah_sesi 
        self.email = email
        self.no_telepon = no_telepon
    
    def hitung_pendapatan_akhir(self):
        ...
    
    def hitung_jumlah_sesi(self):
        ...
        
    def get_info_dari_data_rekap(self):
        ...
     
class Kepsek(User):
    
    def melihat_data_rekap(self):
        ...
        
class Admin(User):
    
    def melihat_data_rekap(self):
        ...
    def menghapus_guru(self):
        ...
    def menambahkan_guru(self):
        ...
    def mengubah_data_rekap(self):      
        ...

class Data_Rekap:
     def __init__(self, tanggal, jam_awal, jam_akhir, menit_tambahan, nama_siswa,jumlah_siswa, tempat, pencapaian):
        self.tanggal = tanggal 
        self.jam_awal = jam_awal  
        self.jam_akhir = jam_akhir  
        self.menit_tambahan = menit_tambahan  
        self.nama_siswa = nama_siswa  
        self.jumlah_siswa = jumlah_siswa 
        self.tempat = tempat  
        self.pencapaian = pencapaian  
        