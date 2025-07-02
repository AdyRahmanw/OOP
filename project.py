class user:
    def __init__(self,nama_lengkap,email,no_telepon,nip,role):
        self.nama = nama_lengkap
        self.email = email
        self.no_telepon = no_telepon
        self.nip = nip
        self.role = role
    
    def login(self):
        print(f"kosongan dulu")
class guru(user):
    def __init__(self,nama_lengkap,email,no_telepon,nip,role,mapel,total_pendaaptan,jumlah_sesi):
        super().__init__(nama_lengkap,email,no_telepon,nip,role)
        self.mapel = mapel
        self.total_pendapatan = total_pendaaptan
        self.jumlah_sesi = jumlah_sesi
    
    def hitung_pendapatan_akhir(self):
        ...
    
    def hitung_jumlah_sesi(self):
        ...
    def get_info_dari_data_rekap(self):
        ...
     
class kepsek(user):
    def __init__(self, nama_lengkap, email, no_telepon, nip, role,jabatan):
        super().__init__(nama_lengkap, email, no_telepon, nip, role)
        self.jabatan = jabatan
    
    def melihat_data_rekap(self):
        ...
        
class admin(user):
    def __init__(self, nama_lengkap, email, no_telepon, nip, role):
        super().__init__(nama_lengkap, email, no_telepon, nip, role)  
    
    def melihat_data_rekap(self):
        ...
    def menghapus_guru(self):
        ...
    def menambahkan_guru(self):
        ...
    def mengubah_data_rekap(self):      
        ...

        