class Calc: #Loome klassi kalkulaatorite loomiseks
    def __init__(self, num1, num2): #Klassi objekti loomisel peab sellele andma kaks numbri muutujat.
        self.num1 = num1 #Kalkulaatori objekti esimeseks numbriks määratakse esimene numbri muutuja.
        self.num2 = num2 #Teiseks numbriks määratakse teine numbri muutuja.

    def liitmine(self): #Defineerime liitmise meetodi.
        return self.num1 + self.num2 #Tagastame kahe antud numbri liitmise tulemuse.
    def lahutamine(self): #Defineerime lahutamise meetodi.
        return self.num1 - self.num2 #Tagastame kahe antud numbri lahutamise tulemuse.
    def korrutamine(self): #Defineerime korrutamise meetodi
        return self.num1 * self.num2 #Tagastame kahe antud numbri korrutamise tulemuse.
    def jagamine(self): #Defineerime jagamise meetodi.
        return self.num1 / self.num2 #Tagastame kahe antud numbri jagamise tulemuse.
    def jaak(self): #Defineerime jagamise jäägi leidmise meetodi.
        return self.num1 % self.num2 #Tagastame kahe antud numbri jagamise jäägi leidmise tulemuse.
    def aste(self): #Defineerime astendamise meetodi.
        return self.num1 ** self.num2 #Tagastame esimese arvu teise astendajaks panemise tulemuse.


a = int(input("Sisesta esimene number: ")) #Küsime kasutajalt esimese muutujana esimest numbrit.
b = int(input("Sisesta teine number: ")) #Küsime kasutajalt teise muutujana teist numbrit.
kalk = Calc(a, b) #Loome kalkulaatori kasutades kahte saadud muutujat objekti loomiseks vajalike väärtustena.
while True: #Senikaua kui selle all olevad read False tulemust ei tagasta kordame neid kui jõuame lõppu.
    def menu(): #Defineerime menu.
        x = '1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Astendamine ' #Menu prinditakse sõnedena erinevatel ridadel, mis vastavad kalkulaatori tegudele.
        print(x)
    menu()
    valik = int(input('Sisesta üks valikutest: '))
    if valik == 1:
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == 2:
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ", kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ",kalk.aste())
        break
    else:
        print("See valiku number pole valikutes antud")

