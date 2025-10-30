#Novo arquivo para aprender fila em Phyton

#Classe No
class No:
    def __init__(self, dado: int):
        self.dado = dado 
        self.prox = None

#Clase Fila
class Fila:
    def __init__(self):
        self.noPrimeiro = None
        self.noUltimo = None
        self.tamanho = 0
    
    def inserir (self, dado: int):
        novo = No(dado)
        if  self.noPrimeiro==None:
            self.noPrimeiro=novo
            self.noUltimo=novo 
        else:  
            self.noUltimo.prox=novo
            self.noUltimo=novo
        self.tamanho+=1
        print(novo.dado)
    
    def remover (self):
        if self.noPrimeiro==None:
            return None
        
        dadoRemovido=self.noPrimeiro.dado
        self.noPrimeiro= self.noPrimeiro.prox
        self.tamanho-=1
        if self.noPrimeiro==None:
            self.noUltimo=None
        print(dadoRemovido)
        return dadoRemovido
        
    
    def retornar (self):
        if self.noPrimeiro==None: 
            return None
        dadoPrimeiro=self.noPrimeiro.dado 
        return dadoPrimeiro
   
    def imprimaTudo (self):
        if self.tamanho==0:
            print("Lista vazia!")
            return None
        atual=self.noPrimeiro
        while atual:
            print(atual.dado)
            atual=atual.prox

def main():
    fila=Fila()
    while True:
        explicacao= "1.inserir 2.remover 3.imprimir x.sair: \n"
        coloque = input(explicacao)
        if coloque== "x" :
            print("Sair") 
            return
        if coloque=='1':
            print("Insira um Número:")
            novoNumero=input("Número inserido:")
            fila.inserir(novoNumero)
        if coloque=="2":
            print("Numero removido:")
            fila.remover()
        if coloque=="3":
            print("Imprimir todos:")
            fila.imprimaTudo()

if __name__=="__main__":
    main()