#Realiza operaciones aritméticas
import math
import decimal

from algelin.Vectorial import *


class OperArit():
	
	def __init__(self):
		self.__NumerosHexa=['A','B','C','D','E','F']
		self.__NumerosHexaVal=[10,11,12,13,14,15]
		self.VectorInvertido=[]
		#self.__NumerosHexaVal=['10','11','12','13','14','15']


	def Factorial(self,iNumero):
		# Calcula el factorial de un número entero tecnica recursiva

		if iNumero==0:
			return 1
		else:
			return iNumero*self.Factorial(iNumero-1)


	def QDigitos(self, iNumero):
		#Calclula el tamaño de de un número natural
		
		if iNumero!=0:
			xDigitos=int(math.log10(iNumero))+1
		else:
			xDigitos=1

		return xDigitos


	def SeparaDigitoEntDec(self, iNumero):
		# Separa un número racional en: signo,  parte entera y la parte dicimal

		if iNumero !=0:
			xNumAbs=math.fabs(iNumero)
			sPEntera=str(math.trunc(xNumAbs))
			xTamNumE=len(sPEntera)
			sPDecimal=str(xNumAbs)[xTamNumE+1:]
			xTamNumD=len(sPDecimal)
			if iNumero<0:
				sSigno="-"
			else:
				sSigno="+"
			return [sSigno],[sPEntera, sPDecimal],[xTamNumE, xTamNumD]
		else:
			return 0


	def VectorNumBase(self,iNumero,iBase):
		#Valida si iNumero es un número ENTERO es compatible con la base iBase

		sNumero=str(iNumero)
		vNumero=[]
		xDigMax=iBase-1
		xTamNum=len(sNumero)
		xNumMaxDig=int(len(str(xDigMax)))
		i=0;
		sParentesis=""
		xContaDig=0
		bSiguiente=True

		while (i<xTamNum) and bSiguiente:
			if sNumero[i]=="(":
				i=i+1 # Avanza una posicion
				if (i+xNumMaxDig)<xTamNum:
					sTrozo=sNumero[i:i+xNumMaxDig]
					i=i+xNumMaxDig 
					if i<xTamNum:
						if sNumero[i]==")":
							try:
								xTrozo=int(sTrozo) 
								i=i+1
								if xTrozo<=xDigMax:
									vNumero.append(str(xTrozo))
								else:
									bSiguiente=False
							except ValueError:
								bSiguiente=False
						else:
							bSiguiente=False
					else:
						bSiguiente=False
				else:
					bSiguiente=False
			else:
				try:
					sTrozo=sNumero[i]
					i=i+1
					if sTrozo in self.__NumerosHexa:
						sTrozo=self.__NumerosHexaVal[self.__NumerosHexa.index(sTrozo)]
					xTrozo=int(sTrozo)
					if xTrozo<=xDigMax:
						vNumero.append(str(sTrozo))
					else:
						bSiguiente=False
				except ValueError:
					bSiguiente=False
		if bSiguiente:
			return vNumero
		else:
			return print("Número no compatible")


	def SeparaDigEntDecGeneral(self,iNumero,iBase):
		# Separa la parte entera y decimal de un número de cualquier base

		sNumero=str(iNumero)
		xTamNum=len(sNumero)
		xQpunto=sNumero.count(".")
		bSiguiente=True

		if sNumero[0]=="-":
			sSigno="-"
			sNumero=sNumero[1:]
		elif sNumero[0]=="+":
			sSigno="+"
			sNumero=sNumero[1:]
		else:
			sSigno="+"

		if xQpunto>1:
			bSiguiente=False
		elif xQpunto==0:
			vEntero=self.VectorNumBase(sNumero,iBase)
			vDecimal=None
		else:
			xIndex=sNumero.find(".")
			if xIndex==0:
				bSiguiente=False
			else:
				vEntero=self.VectorNumBase(sNumero[0:xIndex],iBase)
				vDecimal=self.VectorNumBase(sNumero[xIndex+1:],iBase)

		if bSiguiente:
			return (sSigno,vEntero,vDecimal)	
		else:
			return None

	def ConverABase10(self,iNumero,iBase):
		# Convierte un número de otra base a base 10

		if iNumero !=0:
			mDatos=self.SeparaDigitoEntDec(iNumero)
			sSigno=mDatos[0][0]		#Signo de iNumero
			vEntero=mDatos[1][0]	#Parte Entera de iNumero
			vDecimal=mDatos[1][1]	#Parte Decimal de iNumero
			vQDig=mDatos[2]			#Cantidad de dígitos de la parte Entera, parte Decimal
			xQDigEnt=int(vQDig[0])
			xQDigDec=int(vQDig[1])
			xEntero=0
			xDecimal=0

			for i in range(xQDigEnt):
				xEntero=xEntero+int(vEntero[i])*math.pow(iBase,xQDigEnt-i-1)
			for i in range(xQDigDec):
				xDecimal=xDecimal+int(vDecimal[i])/math.pow(iBase,i+1)
			if sSigno=="-":
				xSigno=-1
			else:
				xSigno=1
			return xSigno*(xEntero+xDecimal)

		else:
			return 0


	def DivisionSucesivaEntero(self,iDividendo,iDivisor):
		# División sucesiva, hasta que el coeficiente sea menor al divisor. Formando un vector invertido del resto
		
		xCoeficiente=iDividendo

		if xCoeficiente>=iDivisor:
			xCoeficiente=int(math.trunc(iDividendo/iDivisor))
			xResto=int(math.fmod(iDividendo,iDivisor))
			self.VectorInvertido.append(str(xResto))
			self.DivisionSucesivaEntero(xCoeficiente,iDivisor)
		else:
			self.VectorInvertido.append(str(xCoeficiente))

		return self.VectorInvertido

	
	def ReversionVectorInvertido(self,iVector):
		# Revierte orden a un vector invertido
		
		sVector=[]
		for i in range(len(iVector)):
			sVector.append(iVector[len(iVector)-1-i])
	
		return sVector


	def ConverDesdeBase10PE(self,iNumero,iBase):
		# Convierte un número entero de base 10 a otra base

		try:
			xNumero=int(iNumero)
			xBase=int(iBase)
			bSiguiente=True
			if xNumero<0:
				sSigno="-"
				xNumero=math.fabs(xNumero)
			elif xNumero>0:
				sSigno="+"
			else:
				sSigno=""
			self.VectorInvertido.clear()
			sVector=self.DivisionSucesivaEntero(xNumero,xBase)
			sVector=self.ReversionVectorInvertido(sVector)
		except ValueError:
			bSiguiente=False
		if bSiguiente:
			return (sSigno,sVector)
		else:
			return None


	def PrimerDigNumNatural(self, iNumero):
		# Extrae el primer dígito, de mayor orden de un número natural, en string

		try:
			sNumero=str(int(iNumero))
			xPrimerD=sNumero[0]
			xTrozo=sNumero[1:]
			return (xPrimerD,xTrozo)
		except ValueError:
			return None		


	def ConverDesdeBase10PD(self,iNumero,iBase):
		# Convierte sólo la parte decimal de un número de base 10 a otra base

		try:
			sNumero=str(iNumero)
			if iNumero!=0:
				if sNumero[0]=="0" and sNumero[1]==".":
					sNumero=sNumero[2:]
					bSiguiente=True
			else:
				bSiguiente=False

			xTamNum=len(sNumero)						
			xNumero=int(sNumero)
			xMaxIter=20
			sVector=[]
			xIter=0

			while (xNumero!=0 and xIter<=xMaxIter):
				xMulti=xNumero*iBase
				xPrimerD=int(math.trunc(xMulti/math.pow(10,xTamNum)))
				xNumero=int(xMulti-xPrimerD*math.pow(10,xTamNum))
				sVector.append(str(xPrimerD))
				xIter=xIter+1	
			
		except ValueError:
			bSiguiente=False

		print(bSiguiente)
		if bSiguiente:
			return sVector
		else:
			return None

	def ConverDesdeBase10PDG(self,iNumero,iBase):
		pass
		