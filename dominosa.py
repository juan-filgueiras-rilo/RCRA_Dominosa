#clase ficha
import math
class ficha:
	def __init__(self,x,y,val,direc):
		self.x=x
		self.y=y
		self.val=val#izqierda/arriba-derech/abajo
		self.direc=direc
	def hash(self):
		pass
	def toString(self):
		print (self.x ,self.y,self.val,self.direc)
	def incompatibles(self,fich):
		if self.val[0]==fich.val[0] and self.val[1]==fich.val[1]:
			return True
		if self.val[1]==fich.val[0] and self.val[0]==fich.val[1]:
			return True
		##################
		newx=0
		newy=0
		finewx=0
		finewy=0
		if self.direc=='HORIZONTAL':
			newx=self.x+1
			newy=self.y
		if self.direc=='VERTICAL':
			newx=self.x
			newy=self.y+1
		if fich.direc=='HORIZONTAL':
			finewx=self.x+1
			finewy=self.y
		if fich.direc=='VERTICAL':
			finewx=self.x
			finewy=self.y+1
		if (self.x==fich.x and self.y==fich.y) or (self.x==finewx and self.y==finewy) or (newx==fich.x and newy==fich.y) or (newx==finewx and newy==finewy):
			return True
		return False

		##################
		# if self.x==fich.x :
		# 	if self.y==fich.y:
		# 		return True
		# 	if self.y!=fich.y-1 and self.y!=fich.x+1:
		# 		return False
		# 	if self.direc=='VERTICAL' and fich.direc=='VERTICAL':
		# 		return True
		# 	if self.direc=='HORIZONTAL' and fich.direc=='HORIZONTAL':
		# 		return False
		# 	if self.direc=='HORIZONTAL' and fich.y==self.y+1:
		# 		return False
		# 	return True
		# if self.y==fich.y :
		# 	if self.x==fich.x:
		# 		return True
		# 	if self.x!=fich.x-1 and self.x!=fich.x+1:
		# 		return False
		# 	if self.direc=='VERTICAL' and fich.direc=='VERTICAL':
		# 		return False
		# 	if self.direc=='HORIZONTAL' and fich.direc=='HORIZONTAL':
		# 		return True
		# 	if self.direc=='VERTICAL' and fich.x==self.x+1:
		# 		return False
		# 	return True
		# return False
	def equals(self,fich):
		if self.x==fich.x and self.y==fich.y and self.direc==fich.direc:
			return True
		else:
			return False
#clase regla
class regla():
	def __init__(self,fich):
		self.creaFicha=fich
		self.lcancel=[]
	def addCancel(self,fich):
		self.lcancel.append(fich)
	def toString(self):
		print('regla<')
		self.creaFicha.toString()
		print('cancela')
		for fich in self.lcancel:
			fich.toString()
		print('>')
#clase tabla
class tabla:
	def __init__(self,fichero):
		self.lista=[]
		self.lfichas=[]
		self.lreglas=[]
		f=open(fichero,'r')
		linea=f.readline()
		self.maxx= int(linea.split()[0])
		self.maxy= int(self.maxx-1)
		i=0
		j=0
		print('larg',self.maxy)
		for i in range(0,self.maxy+1):
			linea=f.readline().split()
			print('fila',i,'linea',linea)
			for j in range(0,self.maxx+1):
				self.lista.append(int(linea[j]))
	def generatefichas(self):
		#genera toda las fichas
		i=0
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			print(i)
			if not self.maxx==(i%(self.maxx+1)) :
				self.lfichas.append(ficha(i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+1]),'HORIZONTAL'))				
			if not self.maxy==math.floor((i/(self.maxx+1))):
				self.lfichas.append(ficha(i%(self.maxx+1),
					math.floor(i/(self.maxx+1)),
					(self.lista[i],
						self.lista[i+self.maxx+1])
					,'VERTICAL'))
	def showFichas(self):
		print('fichas')
		for f in self.lfichas:
			f.toString()
		print('Lengt:',len(self.lfichas))	
		print('------------------')
	def show(self):
		i=0
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			if 0 == (i % (self.maxx+1) ):
				print('\n')
			print(self.lista[i],end='') 
		print('')
	def createReglas(self):
		for fi1 in self.lfichas:
			r1=regla(fi1)
			for fi2 in self.lfichas:
				if not fi1.equals(fi2):
					if fi1.incompatibles(fi2):
						r1.addCancel(fi2)
			self.lreglas.append(r1)
	def showReglas(self):
		print('Reglas')
		for reg in self.lreglas:
			reg.toString()
		print('--------------------------')
def main():
	#Leer fichero
	t=tabla('dom05.txt')
	t.show()
	t.generatefichas()
	t.showFichas()
	t.createReglas()
	t.showReglas()
	#lista de fichas
		#buscar fichas con cada valor y anadirlas
		#hash de la ficha (val1 val2 x y (h|v))
		#negar fichas superpuestas (que compatan (x,y) o al rededores)
	#exportar hash y reglas a formato clasp

if __name__ == "__main__":
    # execute only if run as a script
    main()