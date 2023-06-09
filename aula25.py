#           POO - Herança / P3
class NPC: #Classe base, pai ou classe super
    def __init__(self, nome, time, força, munição): 
        self.nome=nome
        self.time=time
        self.força=força
        self.munição=munição
        self.vivo=True
        self.energia=100
    def info(self):
        print(f"Nome...: {self.nome}")
        print("Time...: " + str(self.time))
        print("Força..: " + str(self.força))
        print("Munição: " + str(self.munição))
        print("Vivo...: " + ("sim" if self.vivo else "não"))
        print("Energia: " + str(self.energia))
        print(30 * "*")
        
class Soldado(NPC):
    def __init__(self, nome, time):
        self.força=200
        self.munição=200
        super().__init__(nome, time, self.força, self.munição)
        
class Guarda(NPC):
    def __init__(self, nome, time):
        self.força=100
        self.munição=20
        super().__init__(nome, time, self.força, self.munição)
        
class Elite(NPC):
    def __init__(self, nome, time):
        self.força=400
        self.munição=500
        super().__init__(nome, time, self.força, self.munição)
    def inf(self):
        super().info()
            
s1=Guarda("Olho", 1)
s2=Soldado("Bala", 1)
s3=Elite("Ninja", 1)
s4=Guarda("Super", 2)
s5=Soldado("Tiro", 2)
s6=Elite("Samurai", 2)

s1.vivo=False
s6.vivo=False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()