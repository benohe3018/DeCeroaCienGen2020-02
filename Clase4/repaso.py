#1) Mete los valores del 1 al 100 en una lista.
#x = range(1,101)
lista = []

for i in range(1,101):
    lista.append(i)

print(lista)


#2) Pide un numero por teclado y guarda en una lista su tabla de multiplicar hasta el 10. Por ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

lista2 = []
numero = int(input("Dame un numero: "))

for i in range(1,11):
    lista2.append(numero * i)

print(lista2)

#3) Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
lista3 = []
entrada = True
while entrada:
    numero = int(input("Dame un número, puedes ingresar números hasta que ingreses 0 :"))
    if numero != 0:
        lista3.append(numero)
    else:
        entrada = False
print(sorted(lista3))

#4) Pide una cadena por teclado, mete los caracteres en una lista sin repetir caracteres.
lista4 = []
cadena = input("Ingresa una cadena: ")

for i in cadena:
    if i not in lista4:
        lista4.append(i)

print(lista4)

Opcion 2

lista44 = []
cadena = input("Ingresa una cadena: ")

lista44 = list(set(cadena))
print(lista44)

#5) Pide una cadena por teclado, mete los caracteres en una lista sin espacios.
lista5 = []
cadena = input("Ingresa una cadena: ")

for i in cadena:
    if i != " ":
        lista5.append(i)

print(lista5)


# 6) Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y
# muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

| Fruta | Precio|
|Plátano | 1.35 |
|Manzana | 0.80|
|Pera| 0.85|
|Naranja | 0.70|

dicfrutas = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
clave = input("Dime que fruta quieres comprar: ")
kilos = int(input("Dime cuantos kilos quieres comprar: "))

if clave in dicfrutas.keys():
    print(kilos * dicfrutas[clave])
else:
    print("No vendemos eso joven")
