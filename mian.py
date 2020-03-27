class matriz:

    matriz:float = []
    inversa:float = []

    def __init__(self,  matriz):
        self.matriz = matriz
        tam = len(matriz)
        self.inversa = [[0]*tam]*tam
        for i in range(tam):
            self.inversa[i][i] = 1
    def calcLinha(self, i, j):
        print(f'passou com linha 1: {self.matriz[i]} e linha 2: {self.matriz[j]} usando de mult: {self.matriz[j][i]}/{self.matriz[i][i]}')

        for x in range(len(self.matriz)):
            self.matriz[j][x] -= self.matriz[i][x]*self.matriz[j][i]
            self.inversa[j][x] -= self.inversa[i][x]*self.matriz[j][i]

    def calcInversa(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if i != j:
                    if self.matriz[i][i] != 1:
                        print('tornou pivo 1')
                        for k in range(len(self.matriz)):
                            self.matriz[i][k]/=(float)(self.matriz[i][i])
                        print(self.matriz[i])
                    if self.matriz[i][i] == 0:
                        print('trocou linha')
                        if i == len(self.matriz)-1:
                            aux = self.matriz[i-1]
                            self.matriz[i-1] = self.matriz[i]
                            self.matriz[i] = aux
                        else:
                            aux = self.matriz[i+1]
                            self.matriz[i+1] = self.matriz[i]
                            self.matriz[i] = aux
                    self.calcLinha(i, j)

    def validar(self) -> bool:

        negador = [0]*len(self.matriz)

        for i in self.matriz:
            if i == negador:
                print('linha nula')
                return False
        
        for i in range(len(self.matriz)):
            somador = 0
            for j in range(len(self.matriz)):
                if self.matriz[j][i] == 0:
                    somador +=1
            if somador == len(self.matriz):
                return False

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if(i != j):
                    somador = 0
                    for k in range(len(self.matriz)):
                        if self.matriz[i][k] % self.matriz[j][k] == 0:
                            somador+=1
                    if somador == len(self.matriz):
                        return False
        return True


m = [[3,1,2],[4,2,8],[7,-1,5]]


M = matriz(m)
print(M.inversa)
if M.validar():
    M.calcInversa()

for i in range(len(M.matriz)):
    print(f'{M.matriz[i]} | {M.inversa[i]}')