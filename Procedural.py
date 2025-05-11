hpHero = 100
seranganHero = 20
hpGoblin = 50
seranganGoblin = 10
hitungLoop = 0

print("Hero mempunyai", hpHero ,"Darah dan kekuatan serangan",seranganHero)
print("Goblin mempunyai", hpGoblin ,"Darah dan kekuatan serangan",seranganGoblin)
print("tekan enter untuk memulai")

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
    
print("selesai")
    
    
    
