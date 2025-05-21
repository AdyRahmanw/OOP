class Karakter:
    def __init__(self,Nama,Role):
        self.Nama = Nama
        self.Role = Role
    
    def Menembak(self):
        print(f"{self.Nama} menembak dor dor dor")
    
    def Menyapa(self):
        print(f"{self.Nama} mengucapkan halo")
        
        
Reyna = Karakter("Reyna","Duelist")

Reyna.Menembak()
Reyna.Menyapa()
