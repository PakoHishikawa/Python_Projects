from algelin.Matricial import Matricial
# Classe que realiza operações da Matemática Linear


class Opelinear():
    
    def __init__(self):
        self.Matriz=[]
        
    
    def EquaLinG1(self,AMatriz, BLinear):
        # Função linear AX = B. Retorna o valor dp vectpr X
        # X = Binversa x B
        
        MX=Matricial()
        self.Matriz=MX.MatrizInversa(AMatriz)
        return MX.Multiplicar2Matriz(self.Matriz,BLinear)
        
        