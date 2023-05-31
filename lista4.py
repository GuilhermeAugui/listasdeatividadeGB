# 1
import math
class figuraGeometricas():
    def __init__(self):
        self._nome= '?'
        self._tipo= '?'
class retangulo(figuraGeometricas):
    def __init__(self, base, altura):
        self._base= base
        self._altura= altura
    def getAltura(self):
        return self._altura
    def getBase(self):
        return self._base
    def calculaArea(self):
        area= self._base * self._altura
        return area 
    def calculaPerimetro(self):
        perimetro= self._base + self._base + self._altura + self._altura
        return perimetro
class triangulo(figuraGeometricas):
    def __init__(self, base, altura, lado):
        self._base = base
        self._altura= altura
        self._lado= lado
    def getAltura(self):
        return self._altura
    def getBase(self):
        return self._base
    def getLado(self):
        return self._lado
    def calculaArea(self):
        area= (self._base * self._altura)/2
        return area 
    def calculaPerimetro(self):
        perimetro= self._base +self._lado + self._lado   
        return perimetro
class circulo(figuraGeometricas):
    def __init__(self, raio):
        self._raio= raio     
    def getRaio(self):
        return self._raio
    def calculaArea(self):
        area= 3.14 * (self._raio)**2
        return area
    
    def calculaPerimetro(self):
        perimetro= (self._raio *2 *3.14)         
        return perimetro   
baseret= float(input('Informe o valor da base do retangulo: '))
alturaret= float(input('Informe o valor da Altura do retangulo: '))
basetri= float(input('Informe o valor da base do triangulo: '))
alturatri= float(input('Informe o valor da altura do triangulo: '))
ladotri= float(input('Informe o valor do lado do triangulo:'))
raio= float(input('Informe o valor do raio do circulo: '))
fg= figuraGeometricas()
ret= retangulo(baseret,alturaret)    
tri= triangulo(basetri,alturatri,ladotri)
cir= circulo(raio)   
print('O valor da area do retangulo é',ret.calculaArea())
print('O valor do perimetr do retangulo é',ret.calculaPerimetro())
print('O valor da area do triangulo é',tri.calculaArea())
print('O valor do perimetro do triangulo é',tri.calculaPerimetro())
print('O valor da area do circulo é',cir.calculaArea())
print('O valor do perimetro do circulo é', cir.calculaPerimetro())
import math
# 2
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca= marca
        self._modelo= modelo
        self._ano= ano
    def acelerar(self):
        print('O carro está sendo acelerado')
    def frear(self):
        print('O carro está freando')
class carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)   
        self._cor= cor
    def ligarRadio(self):
        print('Radio ligado')
    def abrirPorta(self):
        print('Abrindo a porta do carro')
class moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)                              
        self._cilindrada= cilindrada
    def empinar(slef):
        print('A moto esta sendo empinada')
    def buzinar(self):
        print('A buzina da moto esta sendo tocada')
class caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cargaMaxima):
        super().__init__(marca, modelo, ano)            
        self._cargaMaxima= cargaMaxima
    def carregar(self):
        print('O caminhao esta sendo carregado')
    def descaregar(self):
        print('O caminha está sendo descaregado')
C1marca=input('Informe a marca do carro? ')
C1modelo= input('Informe qual é o modelo do carro? ')
C1ano= input('Qual é o ano do carro?')
C1cor= input('Qual é a cor do carro')
c1= Veiculo(C1marca,C1modelo,C1ano)
c1=carro(C1marca,C1modelo,C1ano,C1cor)
c1.ligarRadio()
c1.abrirPorta()
M1marca=input('Informe a marca da moto? ')
M1modelo= input('Informe qual é o modelo da moto? ')
M1ano= input('Qual é o ano da moto?')
M1cilindrada= input('Quantas cilindradas tem o motor da moto?')
m1= Veiculo(M1marca,M1modelo,M1ano)
m1=moto(M1marca,M1modelo,M1ano,M1cilindrada)
m1.buzinar()
m1.empinar()
CA1marca=input('Informe a marca do caminhao? ')
CA1modelo= input('Informe qual é o modelo do caminhao? ')
CA1ano= input('Qual é o ano do caminhao?')
CA1cargaMaxima= input('Quantos quilos o caminhao pode levar? ')
ca1= Veiculo(CA1marca,CA1modelo,CA1ano)
ca1=caminhao(CA1marca,CA1modelo,CA1ano,CA1cargaMaxima)
ca1.carregar()
ca1.descaregar()
# 3
