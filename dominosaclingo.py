import os
import math
import sys
#clase salida
contreglas=0
class tile():
	def __init__(self,x,y,val):
		self.x=x
		self.y=y
		self.val=val
	def toClingo(self,salida):
		salida.storetail('tile('+str(self.x)+','+str(self.y)+','+str(self.val)+').\n')

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
#clase tabla
class tabla:
	def __init__(self,fichero):
		self.sol=[]
		self.lista=[]
		self.lfichas=[]
		self.lreglas=[]
		self.ltiles=[]
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
	def generateTiles(self):
		#genera toda las fichas
		i=0
		for i in range(0,(self.maxx+1)*(self.maxy+1)):
			self.ltiles.append(tile(math.floor(i/(self.maxx+1))+1,(i%(self.maxx+1))+1,self.lista[i]))
	def toClingo(self,salida):
		global contreglas
		#primera linea
		#declracion de variables (aka fichas)
		print('escribiendo clingo')
		i=0
		print('')
		for til in self.ltiles:
			print(int(i/len(self.ltiles)*100),'% \r',end='')
			til.toClingo(salida) 
			i+=1
def main():
	#Leer fichero
	t=tabla(sys.argv[1])
	s=salida('clingo.txt')
	t.generateTiles()
	t.toClingo(s)
	s.storehead('% Type declarations\n\
#show domino/5.\n\
#const n='+str(t.maxx)+'.\n\
\
column(1..n+1).\n\
row(1..n).\n\
value(0..n-1).\n\
\
left_of(C1,C2) :- column(C1), column(C2), C2-C1=1.\n\
above_of(R1,R2) :- row(R1), row(R2), R2-R1=1.\n\
\
same_as(R1,R2) :- row(R1), row(R2), R1=R2.\n\
same_as(C1,C2) :- column(C1), column(C2), C1=C2.\n\
\
orientation(O,R1,R2,C1,C2) :- same_as(R1,R2), O=h, left_of(C1,C2).\n\
orientation(O,R1,R2,C1,C2) :- same_as(C1,C2), O=v, above_of(R1,R2).\n\
\
n*(n+1)/2 { domino(R1,C1,V1,V2,O) : tile(R1,C1,V1), tile(R2,C2,V2),  orientation(O,R1,R2,C1,C2) } n*(n+1)/2.\n\
\
% Effect axioms\n\
%	Evitamos casillas de entrada no validas.\n\
:- tile(R,_,_), not row(R).\n\
:- tile(_,C,_), not column(C).\n\
:- tile(_,_,V), not value(V).\n\
	\
% No se puede repetir ficha formada con los mismos valores.\n\
%	Mismas posiciones.\n\
:- domino(R1,C1,V1,V2,O1), domino(R2,C2,V1,V2,O2), R1!=R2.\n\
:- domino(R1,C1,V1,V2,O1), domino(R2,C2,V1,V2,O2), C1!=C2.\n\
\
%	Diferentes posiciones.\n\
:- domino(R1,C1,V1,V2,O1), domino(R2,C2,V2,V1,O2), V2!=V1.\n\
\
%:- domino(R1,C1,V,V,O1), domino(R2,C2,V,V,O2), R1!=R2.\n\
%:- domino(R1,C1,V,V,O1), domino(R2,C2,V,V,O2), C1!=C2.\n\
\
%	Misma casilla no puede formar sus dos fichas posibles a la vez.\n\
:- domino(R,C,_,_,O1), domino(R,C,_,_,O2), O1!=O2.\n\
\
%	Misma casilla no puede formar ficha y que se forme ficha a partir de ella a la vez.\n\
:- domino(R1,C1,_,_,O1), domino(R2,C2,_,_,O2), R1=R2, C1+1=C2, O1=h. %, O2=v.\n\
\
:- domino(R1,C1,_,_,O1), domino(R2,C2,_,_,O2), R1+1=R2, C1=C2, O1=v. %, O2=h.\n\
\
:- domino(R1,C1,_,_,O1), domino(R2,C2,_,_,O2), R1=R2+1, C1+1=C2, O1=h, O2=v.\n\
\
')
	s.privado()
	
if __name__ == "__main__":
    # execute only if run as a script
    main()