# Matemática estatística das loterias

# import math
# import os
import random
# from datetime import datetime
from algelin.Vectorial import *

class LoteriaX():

	def __init__(self):

		self.vRandom = []
		self.cRandom = Vectorial()


	def getGerarNumEntRandom(self, iLimInf,iLimSup, iSalto):
		# Genera un número entero random en un intervalo [iLimInf,iLimSup]
		return random.randrange(iLimInf, iLimSup, iSalto)
		

	def getVectorERandom(self, iLimInf, iLimSup, iQuaNum):
		# Genera un vector de números enteros de cantidad iQuaNum,no repetidos, entre un rango iLimInf y iLimSup
		# Genera um arquivo txt para guardar temporáriamente vetores mTemRandom

		iSalto=1
		self.vRandom.clear()
		for i in range(iQuaNum):
			xNumRandom = random.randrange(iLimInf-1,iLimSup,iSalto)+1
			xIndex=0
			while xIndex<i:
				if self.vRandom[xIndex]==xNumRandom:
					xNumRandom=random.randrange(iLimInf,iLimSup,iSalto)
					xIndex=0
				else:
					xIndex=xIndex+1
			self.vRandom.append(xNumRandom)

		self.vRandom = self.cRandom.OrdenMenMayVector(self.vRandom)

		return self.vRandom

	def getVectorRandomTXT(self, iLimInf, iLimSup, iQuaNum):
		# Genera un vector de números enteros de cantidad iQuaNum,no repetidos, entre un rango iLimInf y iLimSup
		# Genera um arquivo txt para guardar temporáriamente vetores mTemRandom

		sNomeArquivo = "ColunaRandom.txt"
		vArquivo = open(sNomeArquivo, "w")

		iSalto=1
		self.vRandom.clear()
		# iFator = iQuaNum
		iFator = 100
		iVezes = iQuaNum * iFator
		for i in range(iFator):
			for j in range(iQuaNum):
				xNumRandom = random.randrange(iLimInf-1,iLimSup,iSalto)+1
				xIndex=0
				while xIndex<j:
					if self.vRandom[xIndex]==xNumRandom:
						xNumRandom=random.randrange(iLimInf,iLimSup,iSalto)
						xIndex=0
					else:
						xIndex=xIndex+1
				self.vRandom.append(xNumRandom)
				sTexto = str(xNumRandom)+"\n"
				vArquivo.write(sTexto)
    
		vArquivo = open(sNomeArquivo,"r")
		vConArquivo = vArquivo.readlines()
		vArquivo.close()
		vValores = []

		for i in range(iLimSup):
			vValores.append(0)
		for i in range(iVezes):
			
			iValor = int(vConArquivo[i])- 1 	#Se resta 1 pelo índice zero, que é o primeiro valor
			vValores[iValor] = vValores[iValor] + 1
		self.vRandom.clear()
		vValSelect = Vectorial().OrdenMayMen2Vector(vValores)
		for i in range(iQuaNum):
			self.vRandom.append(vValSelect[i])
		self.vRandom = self.cRandom.OrdenMenMayVector(self.vRandom)

		return self.vRandom	


	def getVectorTrevol(self):
		self.vRandom.clear()
		qTrevol = 6
		vTrevol = []
		xTrevol1 = self.getGerarNumEntRandom(1,qTrevol,1)
		vTrevol.append(xTrevol1)
		xTrevol2 = self.getGerarNumEntRandom(1,qTrevol,1)
#		print(xTrevol1,xTrevol2)
		while xTrevol1==xTrevol2:
			xTrevol2 = self.getVectorERandom(1,qTrevol,1)
		vTrevol.append(xTrevol2)
		self.vRandom = self.cRandom.OrdenMenMayVector(vTrevol)
		return self.vRandom
    
	def getMilhonaria(self):
		print("MILHONARIA")
		print("Trevos")
		self.getVectorTrevol()
		print(self.vRandom)
		self.getVectorERandom(1,50,6)
		return self.vRandom


	def getMegasena(self):
		print("MEGASENA")
#		self.getVectorERandom(1,60,6)
		self.getVectorRandomTXT(1,60,6)
		return self.vRandom

	def getQuina(self):
		print("QUINA")
#		self.getVectorERandom(1,80,5)
		self.getVectorRandomTXT(1,80,5)
		return self.vRandom

	def getLotofacil(self):
		print("LOTOFACIL")
#		self.getVectorERandom(1,25,15)
		self.getVectorRandomTXT(1,25,15)
		return self.vRandom

	def getLotomania(self):
		print("LOTOMANIA")
		self.getVectorERandom(1,100,20)
		return self.vRandom

	def getDiadasorte(self):
    
		print("DIADASORTE")
		print("Mês Sorte")
		print(self.getVectorERandom(1,12,1))
		self.getVectorERandom(1,31,7)
		return self.vRandom

	def getDuplasena(self):
		
		print("DUPLA SENA")
		print("Primeira Serie")
		vLista1 = self.getVectorERandom(1,50,6)
		print(vLista1)
		vLista2 = self.getVectorERandom(1,50,6)
		print("Segunda Serie")
		return (vLista2)

