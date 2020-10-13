import sys
import heapq
from math import sqrt

def carga_int():
	return int(sys.stdin.readline())

def carga_floats():
	line = sys.stdin.readline()
	return list(map(float, line.split()))

def carga_casos():
	sys.stdin.readline()
	ncasos = carga_int()
    
	casos = []
	for n in range(ncasos):
		casos.append(tuple(carga_floats()))
	return casos

def ponto_dist(v1, v2):
	return sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)


def caminho_minimo(points):
	vertices = [0,] 
	arestas = []    
	Max = [(99999999999, i+1, 0) for i, v in enumerate(pontos[1:])]
    
	def atualizar(vertice):
		coordv = pontos[vertice]
		for i, f in enumerate(Max):
			dist, fvertice, _ = f 
			coordf = pontos[fvertice]
			ndist = ponto_dist(coordf, coordv)
			if ndist < dist:
				Max[i] = (ndist, fvertice, vertice)
		heapq.heapify(Max)
	atualizar(0)
   
	while Max:
		dist, fvertice, vertice = heapq.heappop(Max)
		vertices.append(fvertice)
		arestas.append((vertice, fvertice))
		atualizar(fvertice)
	return vertices, arestas
  
if __name__ == '__main__':
    
	ncasos = carga_int()
	for c in range(ncasos):
		pontos = carga_casos()
		vertices, arestas = caminho_minimo(pontos)
		tam = sum([ponto_dist(pontos[s], pontos[e]) for s, e in arestas])
		print("{0:.2f}".format(tam))
		if c+1 < ncasos:
			print('')
