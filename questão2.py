class Equipe:
    def __init__(self,nome, numeroDevitorias):
        self._nome= nome
        self._numeroDeVitorias= numeroDevitorias
class Competidor:
    def __init__(self , nome, vitoriasPessoais):
        self._nome= nome
        self._vitoriasPessoais= vitoriasPessoais
    def round(self,jogadaTime1, jogadaTime2):
       while jogadaTime1== jogadaTime2:
        jogadaTime1= input('Informe novamente um numero: ')
        jogadaTime2= input('Informe novamente um numero: ')
        if jogadaTime1==0 and jogadaTime2== 2:
            print('Vitoria time 1')
        elif jogadaTime1==0 and jogadaTime2== 1:
            print('vitoria time 2')
        elif jogadaTime1==1 and jogadaTime2== 2:                    
            print('vitoria time 2')
        elif jogadaTime1==1 and jogadaTime2== 0:
            print('Vitoria time 1')
        elif jogadaTime1==2 and jogadaTime2== 0:
            print('Vitoria time 2')
        elif jogadaTime1==2 and jogadaTime2== 1:        
            print('Vitoria time 1')    
        elif jogadaTime1==2 and jogadaTime2== 0:        
            print('Vitoria time 2')
        elif jogadaTime1==1 and jogadaTime2== 0:        
            print('Vitoria time 1')
        elif jogadaTime1==2 and jogadaTime2== 1:        
            print('Vitoria time 1')
        elif jogadaTime1==0 and jogadaTime2== 1:        
            print('Vitoria time 2')          
        elif jogadaTime1==0 and jogadaTime2== 2:        
            print('Vitoria time 1')
        elif jogadaTime1==1 and jogadaTime2== 2:        
            print('Vitoria time 2') 
                       