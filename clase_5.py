# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# else:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# else:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo

# if True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# elif True:
#     ... # Bloque de codigo
# else:
#     ... # Bloque de codigo

# if <condicion>: ... # Linea de codigo

# if <condicion>: ... # Linea de codigo
# else: ... # Linea de codigo

# ... if <condicion> else ... 

# =============================================================
# =============================================================

# While ( no se conoce cantidad de iteraciones )

# while <condicion>:
#     <bloque de codigo>

# while True:
#     print('Se ejecuto el print')

# while False:
#     print('No salimos mas de aca...')

# ejecucion_nro = 0
# while True:
#     ejecucion_nro += 1
#     print('Se ejecuto el print nro:', ejecucion_nro)

# =============================================================
# =============================================================

# Ejemplo 1

# repetir_menu = True # bandera/flag
# while repetir_menu:
#     print('''
# ==============
#      Menu
# ==============
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir
# ''')
#     opcion_elegida = input('Ingrese la operacion a realizar: ')
#     if opcion_elegida == '1':
#         print('Retiro efectivo.')
#     elif opcion_elegida == '2':
#         print('Cambio la contraseña.')
#     elif opcion_elegida == '3':
#         repetir_menu = False
#         print('Hasta luego!')
#     else:
#         print('Vuelva a intentar con una opcion valida.')


# =============================================================
# =============================================================

# Ejemplo 2

# numeros = [14, 45, 5, 1234, 1, 4, 9, 15, 25]
# # # numeros = [14, 45, 1234, 1, 4, 9, 15, 25]
# valor_extraido = 0
# while valor_extraido != 5:
#     valor_extraido = numeros.pop()
#     print(valor_extraido)


# =============================================================
# =============================================================

# Ejemplo 3

# hasta = int(input('Ingrese un numero hasta donde quiere sumar: '))
# suma = 0
# while hasta:
#     suma += hasta
#     hasta -= 1

# print(f'La suma es {suma}')

# =============================================================
# =============================================================

# Numeros! (10 min)
# Escribir un programa que le pregunte al usuario números hasta que ingrese el 0, 
# cuando lo haga mostrar por pantalla la suma de todos los números ingresados.

# bandera = True
# suma = 0
# while bandera:
#     valor = int(input('Ingresa un numero (0 para sumar todos los anteriores): '))
#     if valor == 0:
#         bandera = False
#     else:
#         suma += valor

# print('La suma de los valores ingresdos seria', suma)

# =============================================================
# =============================================================

# iteraciones = int(input('Ingrese cantidad de numeros a ingresar: '))

# suma = 0
# while iteraciones:
#     valor = int(input('Ingresa un numero: '))
#     suma += valor
#     iteraciones -= 1

# print('La suma de los valores ingresdos seria', suma)

# =============================================================
# =============================================================

# Break


# iteraciones = int(input('Ingrese cantidad de numeros a ingresar: '))

# suma = 0
# while iteraciones:
#     valor = int(input('Ingresa un numero: '))
#     suma += valor
#     if suma >= 100:
#         break
#     iteraciones -= 1
# else:
#     print('Pase por el else')

# print('La suma de los valores ingresdos seria', suma)




# edad_perro = 1
# while True:
#     print('Guaua!')
#     if edad_perro < 5:
#         edad_perro += 1
#     else:
#         break
#     print('mas valores')
# print('estoy fuera')

# edad_perro = 0
# while edad_perro != 5:
#     print('Guaua!')
#     edad_perro += 1
#     print('mas valores')
# print('estoy fuera')


# =============================================================
# =============================================================

# Continue

# numero = 0
# while numero < 10:
#     numero += 1
#     if numero % 2 == 0:
#         continue
#     print(numero)
    
# print('sali del while')


# =============================================================
# =============================================================

# Pass

# edad_perro = 0
# edad_gato = 0
# if edad_perro == edad_gato:
#     pass # ...
# pass
# print('estoy fuera del if')
# pass


# Usos del pass

# if True:
#     pass # ...

# nombre = input('Ingrese nombre')
# if nombre == '****':
#     pass

# bandera = False
# while bandera:
#     ...


# numero = 0
# while numero < 10:
#     numero += 1
#     if numero % 2 == 0:
#         pass
#     print(numero)
    
# print('sali del while')

# =============================================================
# =============================================================

# While - Else

# condicion = 10
# while condicion:
#     valor1 = 10
#     suma = valor1 + condicion
#     # if suma == 20:
#     #     break
#     print(f'La suma dio de resultado {suma}')
#     condicion -= 1
# else: # nunca pasa por este bloque de codigo porque se corta el while con el break
#     print('pase por el else')

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)


# =============================================================
# =============================================================

# For ( se conoce cantidad de iteraciones )

# for <variable> in <coleccion>:
#     <bloque de codigo>


# Ejemplo 1

# lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# for numero in lista:
#     print('Primer print del bucle')
#     print('Dato de la lista', numero)
#     print('Ultimo print del bucle\n')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 2

# lista = ['pepe', 9, True, 7, 2.53, 5, 'otro dato', 3, ('soy', 'una', 'tupla'), 1]
# for dato_de_la_lista in lista:
#     print('Primer print del bucle')
#     print('Dato de la lista', dato_de_la_lista)
#     print('Ultimo print del bucle\n')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 3

# lista = [10,9,8,7,6,5,4,3,2,1]
# for numero in lista:
#     valor1 = 10
#     suma = valor1 + numero
#     print(f'La suma dio de resultado {suma}')

# print('Aca ya estamos fuera del bucle') 


# Ejemplo 4

# indice = 0
# lista = ['pepe', 9, True, 7, 2.53, 5, 'otro dato', 3, ('soy', 'una', 'tupla'), 1]
# for dato_de_la_lista in lista:
#     print(f'Indice: {indice}, valor: {dato_de_la_lista}')
#     indice += 1

# print('Aca ya estamos fuera del bucle')


# Ejemplo 5 ( Ejemplo 3 con modificacion de lista )

# indice = 0
# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista:
#     valor1 = 10
#     suma = valor1 + dato_de_la_lista
#     print(f'La suma dio de resultado {suma}')
#     lista[indice] = dato_de_la_lista * 2
#     indice += 1

# print(lista)


# =============================================================
# =============================================================

# Desfragmentar tuplas/listas

# Teniendo en cuenta que tenemos una tupla/lista se puede realizar una desfragmentacion
# de la misma para poder guardar cada valor de la misma de forma individual
# como se muestra a continuacion:

# Ejemplo con tupla

# tupla = ('ricado', 4, True)
# nombre, edad, pelado = tupla
# print(tupla)
# print(nombre)
# print(edad)
# print(pelado)

# Ejemplo con lista

# lista = ['ricado', 4, True]
# nombre, edad, pelado = lista
# print(lista)
# print(nombre)
# print(edad)
# print(pelado)


# =============================================================
# =============================================================

# Enumerate

# Devuelve una tupla de tuplas, donde estas ultimas contienen el indice y el valor 
# correspondiente a cada dato de la coleccion


# Ejemplo 1

# lista = [10,9,8,7,6,5,4,3,2,1]
# for valores_devueltos in enumerate(lista):
#     print(valores_devueltos)

# lista = [10,9,8,7,6,5,4,3,2,1]
# #   (  0  ,   10 )
# for indice, valor in enumerate(lista): # en este caso se usa la desfragmentacion
#     print(indice, valor)


# Ejemplo 2 ( version mejorada del ejemplo 4 del tema For )

# indice = 0
# lista = ['pepe', 9, True, 7, 2.53, 5, 'otro dato', 3, ('soy', 'una', 'tupla'), 1]
# for indice, dato_de_la_lista in enumerate(lista):
#     print(f'Indice: {indice}, valor: {dato_de_la_lista}')

# print('Aca ya estamos fuera del bucle')


# Ejemplo 3 ( version mejorada del ejemplo 5 del tema For )

# lista = [10,9,8,7,6,5,4,3,2,1]
# for indice, valor_de_la_lista in enumerate(lista):
#     valor1 = 10
#     suma = valor1 + valor_de_la_lista
#     print(indice, valor_de_la_lista)
#     print(f'La suma dio de resultado {suma}')
#     # lista[indice] = valor_de_la_lista * 2

# print(lista)


# =============================================================
# =============================================================

# Range

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for numero in lista:
#     print(numero)

# usando range
# for numero in range(10):
#     print(numero)

# range(<valor final sin incluirlo>)
# for numero in range(10):
#     print(numero)

# range(<valor incial incluido>, <valor final sin incluirlo>)
# for numero in range(4, 10):
#     print(numero)

# range(<valor incial incluido>, <valor final sin incluirlo>, <salto>)
# for numero in range(5, 12, 2):
#     print(numero)

# range pero del numero mas grande al mas chico
# for numero in range(12, 5, -2):
#     print(numero)

# print(list(range(10)))

# =============================================================
# =============================================================

# # For - For/Else - break/continue/pass
# Para la sentencia for... las funcionalidades de las instrucciones break/continue/pass
# son iguales a las que poseen para la sentencia while, al igual que la sentencia else.

# Descomenta y proba

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for numero in lista:
#     if numero == 5:
#         break
#     # if numero == 5:
#     #     continue
#     # if numero == 5:
#     #     pass
#     print(numero)
# else:
#     print('pase por el else')


# for numero in enumerate(range(1000, 0, -1)):
#     if numero % 2 == 1:
#         continue
#     print(numero)

# =============================================================
# =============================================================

# Ejercicio 2 (15 min)

# Haremos el siguiente listado de ejercicios:
# 1. Escribir un programa que enumere los países de la siguiente lista:

# paises = ['Canada', 'USA', 'Mexico', 'Australia', 'Argentina', 'China', 'India']
# for indice, pais in enumerate(paises):
#     print(f'{indice}: {pais}')
    
# 2. Crear un bucle que sume los pares del 0 al 100

# suma = 0
# for numero in range(0, 101, 2):
#     suma += numero
# print(suma)

# 3. Imprimir por pantalla los números del 1 al 10 al revés
# Nota:
# Para imprimir por pantalla al reves se debe usar el mayor número, luego el menor, 
# y el paso sería con -1 range(mayor, menor, -1)

# for numero in range(10, 0, -1):
    # print(numero)

# 4. Pedirle a un usuario que ingrese un número, y devolver los dígitos totales del número
# Por ejemplo, si el número es 75869, la salida debería ser 5.

# numero = input('Ingrese un numero: ')
# print(len(numero))


# =============================================================
# =============================================================

# Revisar Entregable

# =============================================================
# =============================================================

# Escribí un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética:

# v1
# cant_numeros = int(input('Cuantos numeros vas a ingresar?'))
# valores = []

# for numero_iteracion in range(cant_numeros):
#     valores.append(int(input('Ingrese un valor: ')))

# print(f'El promedio de los valores ingresados es: { sum(valores) / cant_numeros}')


# v2
# cant_numeros = int(input('Cuantos numeros vas a ingresar? '))
# suma = 0
# for numero_iteracion in range(cant_numeros):
#     suma += int(input(f'Ingrese el valor numero {numero_iteracion}: '))

# print(f'El promedio de los valores ingresados es: { suma / cant_numeros}')




# lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
# lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
# lista_3 = []

# for elemento in lista_1:
#     # if lista_2.count(elemento) and not lista_3.count(elemento):
#     if lista_2.count(elemento) and lista_3.count(elemento) == 0:
#         lista_3.append(elemento)
# print(lista_3)

#EJERCICIOS HECHOS POR CARMEN:

#EJERCICIO 1: Escribe un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

# numero_1 = int(input('Ingresa primer número: '))
# numero_2 = int(input('Ingresa segundo número: '))

# repetir_menu = True

# while repetir_menu:
#     print('''Menú:
# 1) Mostrar una suma de los dos números
# 2) Mostrar una resta de los dos números (el primero menos el segundo)
# 3) Mostrar una multiplicación de los dos números
# 4) Salir
# ''')
#     opcion_elegida = input('Ingrese la opción a realizar: ')

#     if opcion_elegida == '1':
#         print('La suma de los dos números es:', numero_1 + numero_2)
#     elif opcion_elegida == '2':
    #     print('La resta de los dos números es:', numero_1 - numero_2)
    # elif opcion_elegida == '3':
    #     print('La multiplicación de los dos números es:', numero_1 * numero_2)
    # elif opcion_elegida == '4':
    #     print('Hasta luego!')
    #     repetir_menu = False
    # else:
    #     print('La opción seleccionada no es correcta. Vuelva a intentarlo!\n')

#EJERCICIO 2: Escribe un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

# numero_1 = int(input('Ingresa numero impar: '))

# while numero_1 % 2 == 0:
#         print('Este no es un numero impar. Vuelva a intentalo!')
#         numero_1 = int(input('Ingresa numero impar: '))
# print(numero_1)

#EJERCICIO 3: Escribe un programa que sume todos los números enteros impares desde el 0 hasta el 100:
#Ayuda: Puedes utilizar la funciones sum() y range() para hacerlo más fácil. El tercer parámetro en la función range(inicio, fin, salto) indica un salto de números.

# suma = sum(range(1, 101, 2))
# print(suma)

#EJERCICIO 4: Escribe un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética.

# cantidad_numeros = int(input("¿Cuántos números quieres introducir? "))
# numeros = []
# for i in range(cantidad_numeros):
#     numeros.append(float(input(f"Introduce el número {i+1}: ")))
# media = sum(numeros) / len(numeros)
# print(f"La media aritmética es: {media}")

#EJERCICIO 5: Escribe un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
#🖐 Ayuda: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False).

# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# numero_usuario = int(input('escribe un numero entero del 0 al 9: '))

# while numero_usuario < 0 or numero_usuario > 9:
#     numero_usuario = int(input("El número introducido no es válido. Introduce un número entero del 0 al 9: "))
    
# if numero_usuario in numeros:
#     print(f"El número {numero_usuario} está en la lista.")

# else:
#     print(f"El número {numero_usuario} no está en la lista.")

# EJERCICIO 6: Utilizando la función range() y la conversión a listas, genera las siguientes listas dinámicamente:
# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
# 🖐 Ayuda: la conversión de listas es mi_lista=list(range(inicio,fin,salto))

# # Todos los números del 0 al 10
# lista1 = list(range(11))
# print(lista1)

# # Todos los números del -10 al 0
# lista2 = list(range(-10, 1))
# print(lista2)

# # Todos los números pares del 0 al 20
# lista3 = list(range(0, 21, 2))
# print(lista3)

# # Todos los números impares entre -20 y 0
# lista4 = list(range(-19, 0, 2))
# print(lista4)

# # Todos los números múltiples de 5 del 0 al 50
# lista5 = list(range(0, 51, 5))
# print(lista5)

