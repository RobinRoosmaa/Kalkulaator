class Calc: #Loome klassi kalkulaatorite loomiseks
    def __init__(self, num1, num2): #Klassi objekti loomisel peab sellele andma kaks numbri muutujat.
        self.num1 = num1 #Kalkulaatori objekti esimeseks numbriks määratakse esimene numbri muutuja.
        self.num2 = num2 #Teiseks numbriks määratakse teine numbri muutuja.
    def liitmine(self): #Defineerime liitmise meetodi.
        return self.num1+self.num2 #Tagastame kahe antud numbri liitmise tulemuse.
    def lahutamine(self): #Defineerime lahutamise meetodi.
        return self.num1-self.num2 #Tagastame kahe antud numbri lahutamise tulemuse.
    def korrutamine(self): #Defineerime korrutamise meetodi
        return self.num1*self.num2 #Tagastame kahe antud numbri korrutamise tulemuse.
    def jagamine(self): #Defineerime jagamise meetodi.
        return self.num1/self.num2 #Tagastame kahe antud numbri jagamise tulemuse.
    def jaak(self): #Defineerime jagamise jäägi leidmise meetodi.
        return self.num1%self.num2 #Tagastame kahe antud numbri jagamise jäägi leidmise tulemuse.
    def aste(self): #Defineerime astendamise meetodi.
        return self.num1**self.num2 #Tagastame esimese arvu teise astendajaks määramise tulemuse.
    def prots(self): #Defineerime protsendi leidmise meetodi.
        return self.num1/self.num2 * 100 #Tagastame kui suure protsendi moodustab esimene arv teisest.
    def hypotenuus(self): #Defineerime täisnurkse kolmnurga hüpotenuusi leidmise Pythagorase teoreemiga.
        return (self.num1**2+self.num2**2)**0.5 #Tagastame Pythagorase teoreemi tulemuse kasutades esimest ja teist arvu täisnurkse kolmnurga külgede pikkusena.
def menu(): # Defineerime taaskasutava menüü, mis kuvab kasutajale kalkulaatori valikud..
    x = '1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Astendamine\n7. Protsendi leidmine (Esimese arvu protsent teisest)\n8. Pythagorase teoreem '  # Menu prinditakse sõnedena erinevatel ridadel, mis vastavad kalkulaatori tegudele.
    print(x)
a = float(input("Sisesta esimene number: ")) #Küsime kasutajalt esimest ja teist numbrit, mis võivad olla komata kui ka komaga arvud.
b = float(input("Sisesta teine number: "))
kalk = Calc(a, b) #Loome kalkulaatori kasutades kahte saadud muutujat objekti loomiseks vajalike väärtustena.
while True: #Senikaua kui selle all olevad read False tulemust või break käsku ei tagasta kordame neid kui jõuame lõppu.
    menu()
    valik = input('Sisesta üks valikutest: ') #Kasutajalt küsitakse menüüst soovitud valikut. Selle põhjal teostatakse saadud numbritega valitud meetod.
    if valik == "1":
        print("Vastus: ",kalk.liitmine())
        break
    elif valik == "2":
        print("Vastus: ",kalk.lahutamine())
        break
    elif valik == "3":
        print("Vastus: ",kalk.korrutamine())
        break
    elif valik == "4":
        print("Vastus: ",kalk.jagamine())
        break
    elif valik == "5":
        print("Vastus: ", kalk.jaak())
        break
    elif valik == "6":
        print("Vastus: ",kalk.aste())
        break
    elif valik == "7":
        print("Vastus: ", kalk.prots(), "%")
        break
    elif valik == "8":
        print("Vastus: ", kalk.hypotenuus())
        break
    else: #Juhul kui valiku number on valesti sisestatud (ükskõik mis tähtede või numbrite kombinatsioon peale 1-8) teatatakse seda kasutajale ja while tsükkel jõustub.
        print("See valiku number pole valikutes antud")