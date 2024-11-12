#Clase que realiza operaciones matemáticas matriciales
from algelin.Vectorial import Vectorial
#import numpy as np

class Matricial():
    def __init__(self):
		# Inicializaciones
        self.Matriz=[]
        #self.Vector=Vectorial()


    def ImprimirMatriz(self,iMatriz):

        for row in iMatriz:
            print()
            for element in row:
                print(element, end=" ")


    def Sumar2Matriz(self, iMatrizA, iMatrizB):
        self.Matriz.clear()

        for i in range(len(iMatrizA)):
            fila=[]
            filaA=[]
            filaB=[]
            filaA=iMatrizA[i]
            filaB=iMatrizB[i]
            
            for j in range(len(iMatrizA)):
                fila.append(filaA[j]+filaB[j])
            self.Matriz.append(fila)
        return self.Matriz
    

    def Multiplicar2Matriz(self, iMatrizA, iMatrizB):
        
        self.Matriz.clear()
        xFilas=len(iMatrizA)
        xFilasB=len(iMatrizB)
        xColumnasB=len(iMatrizB[0])

        for i in range(xFilas):
            fila=[]
            filaA=[]
            filaA=iMatrizA[i]

            for j in range(xColumnasB):
                elemento=0
                for k in range(xFilasB):
                    elemento=elemento+filaA[k]*iMatrizB[k][j]
                fila.append(elemento)
            self.Matriz.append(fila)
        return self.Matriz
    

    def MatrizTranspuesta(self, iMatriz):

        self.Matriz.clear()
        xFilas=len(iMatriz)
        xColumnas=len(iMatriz[0])

        for i in range(xColumnas):
            Filas=[]
            for j in range(xFilas):
                Filas.append(iMatriz[j][i])
            self.Matriz.append(Filas)
        return self.Matriz
    

    def MatrizUnitaria(self, iOrden):
        # Matriz unitaria con los elementos de la traza (diagonal) igual a 1 

        self.Matriz.clear()

        for i in range(iOrden):
            Fila=[]
            for j in range(iOrden):
                if i==j:
                    Fila.append(1)
                else:
                    Fila.append(0)
            self.Matriz.append(Fila)
        return self.Matriz
    

    def MatrizSimetrica(self, iMatriz):
        # Verifica si una matriz cuadrada es simétrica

        bVerificar=True

        for i in range(len(iMatriz)):
            for j in range(len(iMatriz)):
                if iMatriz[i][j]!=iMatriz[j][i]:
                    bVerificar=False
                    break
        return bVerificar


    def MatrizInversa(self, iMatriz):
        # Matriz es la matriz inversa como resultado, al inicio es una matriz unitaria
        # iMatriz es la matriz a invertir
        # HACER AJUSTES FINOS: COLOCAR EXCEPTION Y REDONDEO A DECIMALES

        self.Matriz.clear()
        xOrden=len(iMatriz)
        self.Matriz=self.MatrizUnitaria(xOrden)
        bNoSolucion=False
        Vector=Vectorial()
        
        for i in range(xOrden):

            if Vector.VectorTodoCero(iMatriz[i]):
                print("estamos en problemas")
                iMatriz.clear()
                self.Matriz.clear()
                bNoSolucion=True
                break                     
            if iMatriz[i][i]!=0:
                bOperar=True
            else:
                k=i+1
                print("Fila ",i,iMatriz[i])
                while k<xOrden:
                    if iMatriz[k][i]!=0:

                        vFilaU=iMatriz[i]
                        vFilaI=self.Matriz[i]
                        iMatriz[i]=iMatriz[k]
                        self.Matriz[i]=self.Matriz[k]
                        iMatriz[k]=vFilaU
                        self.Matriz[k]=vFilaI
                        bOperar=True 
                        break
                    k=k+1
                    if k==xOrden:
                        bNoSolucion=True
                        bOperar=False
            if bNoSolucion:
                self.Matriz.clear()
                break
                
            if bOperar:                
                xPivotCentral=iMatriz[i][i]
                Vector.DiviVectorConstante(xPivotCentral,iMatriz[i])
                Vector.DiviVectorConstante(xPivotCentral,self.Matriz[i])
                
                for kk in range(xOrden):                    
                    if i==kk:
                        continue
                    xZero=0
                    xPivot=iMatriz[kk][i]
                    if iMatriz[kk][i]!=0:
                        
                        for ee in range(xOrden):
                            iMatriz[kk][ee]=iMatriz[kk][ee]-xPivot*iMatriz[i][ee]
                            self.Matriz[kk][ee]=self.Matriz[kk][ee]-xPivot*self.Matriz[i][ee]

                    else:
                        xZero=xZero+1
                if (xZero==xOrden-1):
                    self.Matriz.clear()
                    iMatriz.clear()
                    break
                        
        return (self.Matriz)

    
    