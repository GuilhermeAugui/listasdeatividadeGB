import random
class Equipe:
    def __init__(self,nome, numeroDevitorias):
        self._nome= nome
        self._numeroDeVitorias= numeroDevitorias
class Competidor:
    def __init__(self , nome, vitoriasPessoais):
        self._nome= nome
        self._vitoriasPessoais= vitoriasPessoais
    def round(self):
        jogadaTime1= random.randint(0,2)
        jogadorTime2= random.randint(0,2)
        while jogadaTime1 == jogadaTime2:
            jogadaTime1= random.randint(0,2)
            jogadaTime2= random.randint(0,2)
        if jogadaTime1==0 and jogadaTime2== 2:
            print('Vitoria time 1')
            jogadorTime1=jogadorTime1 + 1
            return jogadorTime1
        elif jogadaTime1==0 and jogadaTime2== 1:
            print('vitoria time 2')
            jogadorTime2= jogadorTime2 + 1
            return jogadorTime2
        elif jogadaTime1==1 and jogadaTime2== 2:                    
            print('vitoria time 2')
            jogadorTime2= jogadorTime2 + 1
            return jogadorTime2
        elif jogadaTime1==1 and jogadaTime2== 0:
            print('Vitoria time 1')
            jogadorTime1= jogadorTime1 + 1
            return jogadorTime1
        elif jogadaTime1==2 and jogadaTime2== 0:
            print('Vitoria time 2')
            jogadorTime2= jogadorTime2 + 1
            return jogadorTime2
        elif jogadaTime1==2 and jogadaTime2== 1:        
            print('Vitoria time 1') 
            jogadorTime1= jogadorTime1 + 1
            return jogadorTime1   
        elif jogadaTime1==2 and jogadaTime2== 0:        
            print('Vitoria time 2')
            jogadorTime2= jogadorTime2 + 1
            return jogadorTime2
        elif jogadaTime1==1 and jogadaTime2== 0:        
            print('Vitoria time 1')
            jogadorTime1= jogadorTime1 + 1
            return jogadorTime1
        elif jogadaTime1==2 and jogadaTime2== 1:        
            print('Vitoria time 1')
            jogadorTime1= jogadorTime1 + 1
            return jogadorTime1
        elif jogadaTime1==0 and jogadaTime2== 1:        
            print('Vitoria time 2')        
            jogadorTime2= jogadorTime2 + 1
            return jogadorTime2  
        elif jogadaTime1==0 and jogadaTime2== 2:        
            print('Vitoria time 1')
            jogadorTime1= jogadorTime1 + 1
            return jogadorTime1
        elif jogadaTime1==1 and jogadaTime2== 2:        
            print('Vitoria time 2') 
            jogadorTime2= jogadorTime2 + 1
            return jogadorTime2
joagdorTime1= 0
joagdorTime2= 0
vitoriastime1=0
vitoriastime2= 0
jogadaTime1=0 
jogadaTime2= 0
time1=['Ana','Pedro','Carolina']
time2=['Maria','João','José']

while vitoriastime1!= 10 or vitoriastime2 !=10:
    for i in time1:
        time1= Competidor(i,joagdorTime1)
        time1.round()
        time1= Equipe('Time1',vitoriastime1 )
    for i in time2:
        time2= Competidor(i,joagdorTime2)
        time2= Equipe('Time2',vitoriastime2)
            