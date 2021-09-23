import numpy as np
from scipy.linalg import solve

class Reticulado(object):
    """Define un reticulado"""
    __NNodosInit__ = 100

    #constructor
    def __init__(self):
        super(Reticulado, self).__init__()
        
        #print("Constructor de Reticulado")
        
        self.xyz = np.zeros((Reticulado.__NNodosInit__,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
    
    def agregar_nodo(self, x, y, z=0):
        #print(f"Quiero agregar un nodo en ({x} {y} {z})")
        numero_de_nodo_actual = self.Nnodos
        if self.Nnodos+1 > Reticulado.__NNodosInit__:
            self.xyz.resize((self.Nnodos+1,3))
            self.xyz[self.Nnodos,:] = [x, y, z]
            self.Nnodos += 1
            if z != 0.:
                self.Ndimensiones = 3
    
    def agregar_barra(self, barra):
        
        self.barras.append(barra)        
        
        return 0

    def obtener_coordenada_nodal(self, n):
        if n >= self.Nnodos:
            return 
        return self.xyz[n, :]
        return 0

    def calcular_peso_total(self):
        peso = 0.
        for b in self.barras:
            peso += b.calcular_peso(self)
            return peso 
        
        return 0

    def obtener_nodos(self):
        
        return self.xyz

    def obtener_barras(self):
        
        return self.barras



    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        if nodo not in self.restricciones:
            self.restricciones[nodo]
        
        self.restricciones[nodo].append(gdl,valor)    
        
        return 0

    def agregar_fuerza(self, nodo, gdl, valor):
        
        if nodo not in self.carga: 
            self.cargas[nodo]
        
        self.cargas[nodo].append(gdl,valor)  
        
        return 0


    def ensamblar_sistema(self):
        Ngdl = self.Nnodos * self.Ndimensiones
  
          self.K = np.zeros((Ngdl,Ngdl), dtype=np.double)
          self.f = np.zeros((Ngdl), dtype=np.double)
          self.u = np.zeros((Ngdl), dtype=np.double)
          
          for i,b in enumerate(self.barras):
              
              k_e = b.obtener_rigidez(self)
              f_e = tener_vector_de_cargas(self) 
              
              ni = b.tener_conectividad()
  			
              nj = b.obtener_conectividad()
              
              if self.Ndimensiones == 2:
                  d = [2*ni, 2*ni+1, 2*nj, 2*nj+1]
              else:
  			  
  			  
                    d = [3*ni, 3*ni+1, 3*ni+2, 3*nj, 3*nj+1, 3*nj+2]
              for i in range(self.Ndimensiones*2):
                  p = d[i]
              for j in range(self.Ndimensiones*2):
                  q = d[j]
                      self.K[p,q] += k_e[i,j]
                  self.f[p] = f_e[i] + factor_peso_propio   
        
        return 0



    def resolver_sistema(self):
        
        #for e in self.barras:

        
        return 0

    def obtener_desplazamiento_nodal(self, n):
        
        """Implementar"""   
        
        return 0


    def obtener_fuerzas(self):
        
        """Implementar"""   
        
        return 0


    def obtener_factores_de_utilizacion(self, f):
        
        """Implementar"""   
        
        return 0

    def rediseñar(self, Fu, ϕ=0.9):
        
        """Implementar"""   
        
        return 0



    def chequear_diseño(self, Fu, ϕ=0.9):
        
        """Implementar"""   
        
        return 0


    def __str__(self):
        
        s = "nodos: \n"
        for i in range(len(self.xyz)):
            s+= f"\t {i}: ({self.obtener_coordenada_nodal(i)}) \n"
        
        s+="\n"
        s += "barras: \n"
        for i,j in enumerate(self.barras,start=0):
            s+= f"\t {i}: [{j.ni} {j.nj}] \n"
        
        s+="\n"
        
        return s
