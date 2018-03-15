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
#clase tabla
class tabla:
	def __init__(self,fichero):
		self.lista=[]
		self.lfichas=[]
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
		for i in range(0,(self.maxx)*(self.maxy)):
			print(i)
			if not self.maxx==(i%(self.maxx+1)) :
				#print('H',i%(self.maxx+1))
				self.lfichas.append(ficha(i%(self.maxx+1),math.floor(i/(self.maxy+1)),(self.lista[i],self.lista[i+1]),'HORIZONTAL'))				
			if not self.maxy==math.floor((i/(self.maxy+1))):
				#pass
				self.lfichas.append(ficha(i%(self.maxx+1),math.floor(i/(self.maxy+1)),(self.lista[i],self.lista[i+self.maxx+1]),'VERTICAL'))
	def showFichas(self):
		print('fichas')
		for f in self.lfichas:
			f.toString()
		print('------------------')
	def show(self):
		i=0
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			if 0 == (i % (self.maxx+1) ):
				print('\n')
			print(self.lista[i],end='') 
		print('')

def main():
	#Leer fichero
	t=tabla('dom05.txt')
	t.show()
	t.generatefichas()
	t.showFichas()
	#lista de fichas
		#buscar fichas con cada valor y anadirlas
		#hash de la ficha (val1 val2 x y (h|v))
		#negar fichas superpuestas (que compatan (x,y) o al rededores)
	#exportar hash y reglas a formato clasp

if __name__ == "__main__":
    # execute only if run as a script
    main()