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
    def ligarRadio():
        print('Radio ligado')
    def abrirPorta():
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
                   