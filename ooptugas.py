class Karakter:
    def __init__(self,Nama,Role):
        self.Nama = Nama
        self.Role = Role
    
    def Menembak(self):
        print(f"{self.Nama} menembak dor dor dor")
        
Reyna = Karakter("Reyna","Duelist")
Karakter.Menembak(Reyna)
    