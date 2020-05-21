
#Ejercicio1
def SumaDeLista(array):
	    result=0
	    for i in range (len(array)):
	        result += array[i]
	        print(result)
	    return result

a=(SumaDeLista([1,2,3]))

#Ejercicio2
def Elmina(lista):
   lista=[1,3,4,5,6,7]
   del lista[0]
   del lista[-1]
   return lista
print(lista)



#Ejercicio4
def Elimina_duplicados (lista1):
   lista1=[3,3,4,1,1,1]
   listsindup=list(set(lista1))
   return listsindup
print(listsindup)

#Ejercicio5
def EliminaDuplicados (lista1):
lista1=[3,4,1,1,1]
listsindup=list(set(lista1))
valor= True
if len(lista1) != len(listsindup):
   valor = True
else:
   valor = False
print(valor)






#Ejercicio3
def ListaOrdenada(array):
lista=[1,2,3,5,4]
a = lista
a.sort()
valor=True
if lista != a:
   valor = False
else:
   valor = True
print(valor)
