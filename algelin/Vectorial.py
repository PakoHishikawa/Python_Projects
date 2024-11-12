#Clase que realiza operaciones matemáticas vectoriales
#import numpy as np

class Vectorial():

	def __init__(self):
		# Inicializaciones

		self.vVector=[]
		self.vMes=[31,28,31,30,31,30,31,31,30,31,30,31]


	def VerTam2Vector(self,iVector1,iVector2):
		# Verifica si los tamaños de dos vectores son iguales

		xTam1=len(iVector1)
		xTam2=len(iVector2)

		if (xTam1==xTam2):
			ValidaTam=True
		else:
			ValidaTam=False

		return ValidaTam


	def OrdenMenMayVector(self,iVector):
		#Ordena un vector de números de menor a mayor

		self.vVector.clear

		for i in range(len(iVector)):
			for j in range(i+1,len(iVector)):
				if iVector[j]<iVector[i]:
					xAux=iVector[i]
					iVector[i]=iVector[j]
					iVector[j]=xAux

		self.vVector=iVector
		return self.vVector


	def OrdenMenMay2Vector(self,iVector):
		#Ordena un vector de números de menor a mayor, conforme à index, também se guarda

		xTam = len(iVector)
		vVector = []
		vIndex  = []
		for i in range(xTam):
			vIndex.append(i+1)
			vVector.append(iVector[i])
		for i in range(xTam):
			for j in range(i+1,xTam):
				if vVector[j]<vVector[i]:
					xAuxInd = vIndex[i]
					xAuxVal=vVector[i]
					vIndex[i] = vIndex[j]
					vVector[i] = vVector[j]
					vIndex[j] = xAuxInd
					vVector[j] = xAuxVal

		# self.vVector=iVector
		return vIndex


	def OrdenMayMenVector(self,iVector):
		#Ordena un vector de números de mayor a menor

		self.vVector.clear

		for i in range(len(iVector)):
			for j in range(i+1,len(iVector)):
				if iVector[j]>iVector[i]:
					xAux=iVector[i]
					iVector[i]=iVector[j]
					iVector[j]=xAux

		self.vVector=iVector
		return self.vVector

	def OrdenMayMen2Vector(self,iVector):
		#Ordena um vetor de números de maior a menor, conforme à index, também se guarda

		xTam = len(iVector)
		vVector = []
		vIndex  = []
		for i in range(xTam):
			vIndex.append(i+1)
			vVector.append(iVector[i])
		for i in range(xTam):
			for j in range(i+1,xTam):
				if vVector[j]>vVector[i]:
					xAuxInd = vIndex[i]
					xAuxVal=vVector[i]
					vIndex[i] = vIndex[j]
					vVector[i] = vVector[j]
					vIndex[j] = xAuxInd
					vVector[j] = xAuxVal

		# self.vVector=iVector
		return vIndex


	def Sumar2Vector(self,iVector1,iVector2):
		#Suma dos vectores de números  !!!!!!!!!!! AJUSTAR

		self.vVector.clear()

		if (self.VerTam2Vector(iVector1,iVector2)):
			for i in range(len(iVector1)):
				self.vVector.append(iVector1[i]+iVector2[i])
		else:
			print("No se puede sumar 2 vectores con tamaños diferentes")
			
		return self.vVector
	
	def Restar2Vector(self,iVector1,iVector2):
		# Resta dos vectores de números V1 - v2 !!!! Ajustar

		self.vVector.clear()
		for i in range(len(iVector2)):
			iVector2[i]= -1*iVector2[i]
		self.vVector=self.Sumar2Vector(iVector1,iVector2)
		return self.vVector


	def Multiplicar2Vector(self,iVector1,iVector2):
		#Multiplica dos vectores de números  !!!!!!!!!!! AJUSTAR

		xMult=0
		if (self.VerTam2Vector(iVector1,iVector2)):

			for i in range(len(iVector1)):
				xMult=iVector1[i]*iVector2[i]+xMult
		else:
			print("No se puede multiplicar 2 vectores con tamaños diferentes")
		return xMult


	def ImprimirVector(self):	

		print("[ ", end="")
		for i in range(len(self.vVector)):
				print( self.vVector[i], end=" ")

		print("]")


	def VectorTodoCero(self,iVector):
    
		xZero=0
		for i in iVector:
			if i==0:
				xZero+=1
		if xZero==len(iVector):
			return True
		else:
			return False


	def DiviVectorConstante(self,iConstante,iVector):
		
		if iConstante==0:
			return None
		else:
			for i in range(len(iVector)):
				iVector[i]=iVector[i]/iConstante
			return iVector

	def MultVectorConstante(self,iConstante,iVector):
		
		for i in range(len(iVector)):
			iVector[i]=iVector[i]/iConstante
		return iVector

	def CantidadDiasMes(self,iMes,iAnho):
		
		xDiasMes=self.vMes[iMes-1]
		if iAnho % 4==0 & iMes==2:
			xDiasMes = 29
		return xDiasMes

	def Igualdad2Vectores(self,iVector1,iVector2):

		for i in range(len(iVector1)):
			print(iVector1[i],iVector2[i])
			if iVector1[i] != iVector2[i]:
				eOutput = False
				break
			else:
				eOutput = True
		print("Comparación ",eOutput)
		return eOutput

	def Igualdad2VectoresString(self,iVector1,iVector2):
    
		qTam = len(iVector1)
		sVector1=[]
		sVector2=[]
		for i in range(qTam):
			sVector1.append(iVector1[i])
			sVector2.append(iVector2[i])
		if sVector1==sVector2:
			return True
		else:
			return False