import os
import math
import sys
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
			#print('Afichas:',self.idfich,' ',fich.idfich)
			return True
		if (self.x==x4 and self.y==y4):
			#print('Bfichas:',self.idfich,' ',fich.idfich)
			return True
		if (x2==x4 and y2==y4):
			#print('Cfichas:',self.idfich,' ',fich.idfich)
			return True
		if (x2==fich.x and y2==fich.y):
			#print('Dfichas:',self.idfich,' ',fich.idfich)
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
class listaFichas():
		def __init__(self,n,maxx,maxy):
			self.numfichas=0
			self.maxx=maxx
			self.maxy=maxy
			self.lvalores=[]
			self.lposiciones=[]
			self.lreglas=[]
			for i in range((self.maxx+1)*(self.maxy+1)):
				self.lvalores.append([])
				self.lposiciones.append([])
				self.lposiciones[i]=[]
		def appendFicha(self,fich):
			self.lvalores[fich.val[0]].append(fich)
			self.lvalores[fich.val[1]].append(fich)
			self.lposiciones[self.maxx+((self.maxx+1)*fich.y)-(self.maxx-fich.x)].append(fich)
		def reglas(self):
			porcent=0
			for pos in self.lvalores:
				print(float(porcent/len(self.lvalores)*100),' ',porcent,'/',len(pos),'% \r',end='')
				porcent+=1
				for ficha1 in pos:
					r1=regla(ficha1)
					for ficha2 in self.lvalores[ficha1.val[0]]:
						if(ficha1.valEquals(ficha2) and not ficha1.equals(ficha2)):
							r1.lcancel.append(ficha2)
					for ficha2 in self.lvalores[ficha1.val[1]]:
						if(ficha1.valEquals(ficha2) and not ficha1.equals(ficha2)):
							r1.lcancel.append(ficha2)
					for i in range(ficha1.x-1,ficha1.x+1):
						for j in range(ficha1.y-1,ficha1.y+1):
							if(i>self.maxx or j> self.maxy or i<0 or j<0):
								continue
							#print('x: ',i,'y: ',j,'pos: ',self.maxx+((self.maxx+1)*ficha1.y)-(self.maxx-ficha1.x))	
							if (ficha1.incompatibles(self.lposiciones[self.maxx+((self.maxx+1)*ficha1.y)-(self.maxx-ficha1.x)][0])):
								r1.lincompat.append(self.lposiciones[self.maxx+((self.maxx+1)*ficha1.y)-(self.maxx-ficha1.x)][0])
							if (len(self.lposiciones[self.maxx+((self.maxx+1)*ficha1.y)-(self.maxx-ficha1.x)])>1):
								if (ficha1.incompatibles(self.lposiciones[self.maxx+((self.maxx+1)*ficha1.y)-(self.maxx-ficha1.x)][1])):
									r1.lincompat.append(self.lposiciones[self.maxx+((self.maxx+1)*ficha1.y)-(self.maxx-ficha1.x)][1])	
					self.lreglas.append(r1)
		def getfichasid(self):
			s=''
			i=0
			cont=0
			for pos in self.lposiciones:
				for fich in pos:
					s=s+' '+str(fich.idfich)
					cont+=1
			self.numfichas=cont
			return s
#clase regla
class regla():
	def __init__(self,fich):
		self.creaFicha=fich
		self.lcancel=[]
		self.lincompat=[]
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
		self.sol=[]
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
		self.listanueva=listaFichas(self.maxx,self.maxx,self.maxy)
		
	def generatefichas(self):
		#genera toda las fichas
		idf=1
		i=0
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			#print(i)
			if not self.maxx==(i%(self.maxx+1)) :
				#self.lfichas.append(ficha(idf,i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+1]),'HORIZONTAL'))				
				self.listanueva.appendFicha(ficha(idf,i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+1]),'HORIZONTAL'))
				idf+=1
			if not self.maxy==math.floor((i/(self.maxx+1))):
				#self.lfichas.append(ficha(idf,i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+self.maxx+1]),'VERTICAL'))
				self.listanueva.appendFicha(ficha(idf,i%(self.maxx+1),math.floor(i/(self.maxx+1)),(self.lista[i],self.lista[i+self.maxx+1]),'VERTICAL'))
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
		self.listanueva.reglas()
		self.lreglas=self.listanueva.lreglas
	# 	print('creando reglas')
	# 	contporcentaje=0
	# 	print('')
	# 	for fi1 in self.lfichas:
	# 		print('')
	# 		print(int(contporcentaje/len(self.lfichas)*100),'% \r',end='')
	# 		contporcentaje+=1
	# 		r1=regla(fi1)
	# 		port2=0
	# 		for fi2 in self.lfichas:
	# 			print('\t',int(port2/len(self.lfichas)*100),'% \r',end='')
	# 			port2+=1
	# 			if not fi1.equals(fi2):
	# 				if fi1.incompatibles(fi2):
	# 					r1.addCancel(fi2)
	# 		self.lreglas.append(r1)
	def showReglas(self):
		print('Reglas')
		for reg in self.lreglas:
			reg.toString()
		print('--------------------------')
	def toClasp(self,salida):
		global contreglas
		#primera linea
		#declracion de variables (aka fichas)
		# print('escribiendo hash')
		# sf='c'
		# for fich in self.lfichas:
		# 	sf=sf+' '+'['+str(fich.idfich)+']-'+fich.hash() 
		# salida.storetail (sf+' 0\n')
		print('escribiendo id')
		# sfid=''
		# for fich in self.lfichas:
		# 	sfid=sfid+' '+str(fich.idfich) 
		salida.storetail(self.listanueva.getfichasid()+' 0\n')
		contreglas+=1
		sr=''
		contporcentaje=0
		print('calculando reglas')
		for rgl in self.lreglas:
			sr=sr+'\n'+rgl.toString()+''
			print(int(contporcentaje/len(self.lreglas))*100,'%\r', end='')
			contporcentaje+=1
		salida.storetail (sr)
		#declaracion de reglas
		sh=('p cnf '+str(self.listanueva.numfichas)+' '+str(contreglas)+'\n')
		salida.storehead(sh)
	def findFichaId(self,id):
		for pos in self.listanueva.lposiciones:
			for ficha in pos:
				if ficha.idfich==id:
					return ficha

	def readSol(self):
		f=open('resultado.txt','r')
		linea=' '
		while linea!='':
			linea=f.readline()
			lineaspl=linea.split(' ')
			if lineaspl[0]=='v':
				for i in range(1,len(lineaspl)):
					if (not (lineaspl[i].startswith('-'))) and (not (int(lineaspl[i])==0)):
						#print ('>',lineaspl[i])
						self.sol.append(self.findFichaId(int(lineaspl[i])))#buscar id en la lista y append a soluciones		
	def showSol(self):
		solx=salida('solx.txt')
		print('SOLUCION :')
		#inicializar 
		listatabla=[]
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			listatabla.append('0')
		for ficha in self.sol:
			print('>',ficha.idfich,len(self.sol))
			if(ficha.direc=='HORIZONTAL'):
				listatabla[self.maxx+((self.maxx+1)*ficha.y)-(self.maxx-ficha.x)]='>'
				listatabla[(self.maxx+((self.maxx+1)*ficha.y)-(self.maxx-ficha.x))+1]='<'
			if(ficha.direc=='VERTICAL'):
				listatabla[self.maxx+((self.maxx+1)*ficha.y)-(self.maxx-ficha.x)]='v'
				listatabla[(self.maxx+((self.maxx+1)*ficha.y)-(self.maxx-ficha.x))+self.maxx+1]='^'
		print('',end='\n')
		for i in range(0,len(listatabla)):
			if (i % (self.maxx+1)==0) and i!=0:
				solx.storetail('\n')
			solx.storetail(listatabla[i])
		solx.storetail('\n')
		solx.privado()
def main():
	#Leer fichero
	t=tabla(sys.argv[1])
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
		#negar fichas superpuestas (que compatan (x,y) o alrededores)
	#exportar hash y reglas a formato clasp
	os.system('clasp salida.txt > resultado.txt')
	t.readSol()
	t.showSol()
if __name__ == "__main__":
    # execute only if run as a script
    main()