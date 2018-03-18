import math
#clase salida
contreglas=0
class salida():
	def __init__(self,ficherosalida):
		self.fsalida=open(ficherosalida,'w')
		self.strstored=''
	def publica (self,cosas):
		print(cosas)
	def storetail(self,cosas):
		self.strstored=self.strstored+cosas
	def storehead(self,cosas):
		self.strstored=cosas+self.strstored
	def privado(self):
		self.fsalida.write(self.strstored)

#clase ficha
class ficha:
	def __init__(self,idf,x,y,val,direc):
		self.idfich=idf
		self.x=x
		self.y=y
		self.val=val#izqierda/arriba-derech/abajo
		self.direc=direc
	def hash(self):
		if self.direc=='HORIZONTAL':
			s='0'
		else:
			s='1'
		return str(self.x)+str(self.y)+str(self.val[0])+str(self.val[1])+s
		pass
	def toString(self):
		print (self.x ,self.y,self.val,self.direc)
	def valEquals(self,ficha2):
		if self.val[0]==ficha2.val[0] and self.val[1]==ficha2.val[1]:
			return True
		if self.val[1]==ficha2.val[0] and self.val[0]==ficha2.val[1]:
			return True
		return False
	def incompatibles(self,fich):
		if self.val[0]==fich.val[0] and self.val[1]==fich.val[1]:
			return True
		if self.val[1]==fich.val[0] and self.val[0]==fich.val[1]:
			return True
		##################
		x2=0
		y2=0
		x4=0
		y4=0
		if self.direc=='HORIZONTAL':
			x2=self.x+1
			y2=self.y
		if self.direc=='VERTICAL':
			x2=self.x
			y2=self.y+1
		if fich.direc=='HORIZONTAL':
			x4=fich.x+1
			y4=fich.y
		if fich.direc=='VERTICAL':
			x4=fich.x
			y4=fich.y+1
		if (self.x==fich.x and self.y==fich.y):
			print('Afichas:',self.idfich,' ',fich.idfich)
			return True
		if (self.x==x4 and self.y==y4):
			print('Bfichas:',self.idfich,' ',fich.idfich)
			return True
		if (x2==x4 and y2==y4):
			print('Cfichas:',self.idfich,' ',fich.idfich)
			return True
		if (x2==fich.x and y2==fich.y):
			print('Dfichas:',self.idfich,' ',fich.idfich)
			return True

		return False
			
		


		##################
		# if self.x==fich.x :
		# 	if self.y==fich.y:
		# 		return True
		# 	if self.y!=fich.y-1 and self.y!=fich.x+1:
		# 		return False
		# 	if self.direc=='VERTICAL' and fich.direc=='VERTICAL':
		# 		#cosas
		# 		return True
		# 	if self.direc=='HORIZONTAL' and fich.direc=='HORIZONTAL':
		# 		return False
		# 	if self.direc=='HORIZONTAL' and fich.y==self.y+1:
		# 		return False
		# 	if fich.direc=='HORIZONTAL' and self.y==fich.y+1:
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
		# 	if fich.direc=='VERTICAL' and self.x==fich.x+1:
		# 		return False	
		# 	return True
		##################

		return False
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
	def existeficha(self):
		for ficha in self.lcancel:
			if self.creaFicha.val[0]==ficha.val[0] and self.creaFicha.val[1]==ficha.val[1]:
				return True
			if self.creaFicha.val[1]==ficha.val[0] and self.creaFicha.val[0]==ficha.val[1]:
				return True
		return False
	def addCancel(self,fich):
		self.lcancel.append(fich)
	def toString(self):
		global contreglas
		
		s=str(self.creaFicha.idfich)
		for ficha in self.lcancel:
			if self.creaFicha.valEquals(ficha):
				s=s+' '+str(ficha.idfich)+' '
		contreglas+=1
		s=s+' 0\n'
		for i in range(0,len(self.lcancel)):
			#for j in range(i+1,len(self.lcancel)):
				s=s+' -'+str(self.creaFicha.idfich)+' -'+str(self.lcancel[i].idfich)+' 0\n'
				contreglas+=1
		return s
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
		#print('larg',self.maxy)
		for i in range(0,self.maxy+1):
			linea=f.readline().split()
			#print('fila',i,'linea',linea)
			for j in range(0,self.maxx+1):
				self.lista.append(int(linea[j]))
	def generatefichas(self):
		#genera toda las fichas
		idf=1
		i=0
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			#print(i)
			if not self.maxx==(i%(self.maxx+1)) :
				self.lfichas.append(ficha(idf,i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+1]),'HORIZONTAL'))				
				idf+=1
			if not self.maxy==math.floor((i/(self.maxx+1))):
				self.lfichas.append(ficha(idf,i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+self.maxx+1]),'VERTICAL'))
				idf+=1
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
	def toClasp(self,salida):
		global contreglas
		#primera linea
		#declracion de variables (aka fichas)
		sf='c'
		for fich in self.lfichas:
			sf=sf+' '+'['+str(fich.idfich)+']-'+fich.hash() 
		salida.storetail (sf+' 0\n')

		sfid=''
		for fich in self.lfichas:
			sfid=sfid+' '+str(fich.idfich) 
		salida.storetail(sfid+' 0\n')
		contreglas+=1
		sr=''
		for rgl in self.lreglas:
			sr=sr+'\n'+rgl.toString()+''
		salida.storetail (sr)
		#declaracion de reglas
		sh=('p cnf '+str(len(self.lfichas))+' '+str(contreglas)+'\n')
		salida.storehead(sh)
def main():
	#Leer fichero
	t=tabla('dom07.txt')
	s=salida('salida.txt')
	#t.show()
	t.generatefichas()
	#t.showFichas()
	t.createReglas()
	#t.showReglas()
	t.toClasp(s)
	s.privado()
		#lista de fichas
		#buscar fichas con cada valor y anadirlas
		#hash de la ficha (val1 val2 x y (h|v))
		#negar fichas superpuestas (que compatan (x,y) o al rededores)
	#exportar hash y reglas a formato clasp

if __name__ == "__main__":
    # execute only if run as a script
    main()