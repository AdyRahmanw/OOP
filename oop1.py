class Karakter:
    def __init__(self,hp, damage,nama):
        self.hp = hp
        self.damage = damage
        self.nama = nama
    
    def serangan(self):
        self.hp = self.hp - self.damage
        
    def cerita(self):
        print(f"{self.nama} mempunyai {self.hp}Darah dan kekuatan serangan {self.damage}")
        print("tekan enter untuk memulai")
    
    def loop(self):
        while hpHero > 0 and hpGoblin > 0:
            input("tekan")
            hpGoblin = hpGoblin - seranganHero 
            print(f"hp sisa goblin = {hpGoblin}")
    
        if hpGoblin <= 0:
            print("goblin kalah")
            break
    
        hpHero = hpHero - seranganGoblin
        print(f"hp sisa hero = {hpHero}")
    
        if hpHero <= 0:
            print("hero kalah")
            break
    
        
hero = Karakter(100, 20)
goblin = Karakter(50,10)

print(hero.hp)
print(hero)