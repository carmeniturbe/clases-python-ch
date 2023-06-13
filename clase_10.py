# def nombre_funcion(param1, param2):
#     var1 = 5
    # ==================================
    # return
    # ==================================
    # return param1 + param2 + var1
    # ==================================
    # suma = param1 + param2 + var1
    # return suma
    # ==================================
    # suma = param1 + param2 + var1
    # if suma > 30:
    #     return 'Es mayor a 30'
    # else:
    #     return 'Es menor a 30'
    # ==================================
    # suma = param1 + param2 + var1
    # if suma > 30:
    #     return 'Es mayor a 30'
    # return 'Es menor a 30'


# print(nombre_funcion)
# print(nombre_funcion(5, 25))
# print(nombre_funcion(1, 21))

# ================================================================================
# ================================================================================

# Argumento y Parámetros

# def sumar(num1, num2):
#     return num1 + num2

# print(sumar(1, 5))
# print(sumar(5, 1))

# ================================================================================
# ================================================================================

# Argumentos x posición

# def restar(num1, num2):
#     return num1 - num2

# primera_ejecucion = restar(1, 5)
# print(f'Primera ejecución: {primera_ejecucion}')
# segunda_ejecucion = restar(5, 1)
# print(f'Segunda ejecución: {segunda_ejecucion}')

# ================================================================================
# ================================================================================

# Argumentos por nombre

# def restar(num1, num2):
#     return num1 - num2

# primera_ejecucion = restar(1, 5)
# print(f'Primera ejecución: {primera_ejecucion}')
# segunda_ejecucion = restar(num2=5, num1=1)
# print(f'Segunda ejecución: {segunda_ejecucion}')

# Otro ejemplo

# def devuelva_iterable(var1, var2, var3, var4, var5):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(4,3,1,5,2))
# print(devuelva_iterable(var4=4,var3=3,var1=1,var5=5,var2=2))
# print(devuelva_iterable(1,2,3,var5=5,var4=4))
# print(devuelva_iterable(var2=2,var4=4,3,1,5))
# print(devuelva_iterable(var2=2,3,4,var1=1,5))
# print(devuelva_iterable(1,2,4,var3=3))

# ================================================================================
# ================================================================================

# Llamadas sin argumentos

# Parámetros por defecto

# def devuelva_iterable(var1=1, var2=2, var3=3, var4=4, var5=5):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5))
# # print(devuelva_iterable(1,2,3,4,7))
# print(devuelva_iterable(1,2,3,4))
# print(devuelva_iterable(1,2,3))
# print(devuelva_iterable(1,2))
# print(devuelva_iterable(1))
# print(devuelva_iterable())
# print(devuelva_iterable(5))
# print(devuelva_iterable(5,15))
# print(devuelva_iterable(var3=5,var5=15))
# print(devuelva_iterable(5,var5=15))
# print(devuelva_iterable(var5=15))



# def restar(num1, num2):
#     return num1 - num2
# primera_ejecucion = restar(15, 1)
# print(primera_ejecucion)

# def restar(num1=5, num2=1):
#     return num1 - num2
# primera_ejecucion = restar()
# print(primera_ejecucion)

# def restar(num1, num2=1):
#     return num1 - num2
# primera_ejecucion = restar(15,5)
# print(primera_ejecucion)

# # Acomodar lo de la recomendacion
# def restar(num1=5, num2=1):
#     return num1 - num2
#     # print(num1 - num2)
    
# # restar(num2=10,num1=4)
# primera_ejecucion = restar(num2=10,num1=4)
# print(primera_ejecucion)
# print(restar(num2=10,num1=4))

# Ejemplo


# print('pepe fort se fue de viaje')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('pepe', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end='( estoy al final de mi print )')
# print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('ricardo', 'fort', 'se', 'fue', 'de', 'viaje', end='))))((((')

# ================================================================================
# ================================================================================

# break

# ================================================================================
# ================================================================================

# Argumentos x valor y referencia


# conjunto1 = {1, 'conjunto1', (1, True)}

# Recordatorio
# posiciones en disco |L15|L25|L14|L10|   |
#                     |   |   |   |   |   |

# guarda {1, 'conjunto1', (1, True)} en la posicion L15 de disco
# conjunto1 <--- posicion del disco L15

# ================================================================================
# ================================================================================

# Paso por valor

# def cambio(valor):
#     print(valor)
#     valor = 'otro valor'
#     print(valor)

# valor = 'pepe'
# cambio(valor)
# print(valor)

# ================================================================================
# ================================================================================

# Paso por referencia

# def agregar_valor(datos):
#     print(datos)
#     datos.append('Otro dato')
#     print(datos)

# datos = [1,2,3,4,5]
# agregar_valor(datos)
# print(datos)


# def agregar_valor(datos):
#     print(datos)
#     datos.append('Otro dato')
#     print(datos)

# datos = [1,2,3,4,5]
# agregar_valor(datos[:])
# print(datos)


# def agregar_valor(datos):
#     print(datos)
#     datos.append('Otro dato')
#     print(datos)

# datos = {1,2,3,4,5}
# agregar_valor(datos.copy())
# print(datos)


# def agregar_valor(datos):
#     print(datos)
#     datos[-1].append('Otro dato')
#     print(datos)

# datos = (1,2,3,4,5, ['otra', 'cosa'])
# agregar_valor(datos)
# print(datos)


# *args

# def mi_sum(*coleccion_de_valores):
#     print(coleccion_de_valores)
#     print(type(coleccion_de_valores))
    
#     suma = 0
#     for valor in coleccion_de_valores:
#         # print('Sumando el valor', valor)
#         suma += valor
#     return suma

# print(mi_sum(1,5,3,6))
# print(mi_sum(1,5))
# print(mi_sum(1,5,1,5,12,32,354,234))



# def sumar(num1, num2, num3):
#     return num1 + num2 + num3

# print(sumar(1, 2))


# **kwargs
# def mostrar_claves_y_valores(**claves_y_valores):
#     print(claves_y_valores)
#     print(type(claves_y_valores))
#     for clave, valor in claves_y_valores.items():
#         print(clave, valor)

# mostrar_claves_y_valores(pepe='nombre', apellido='Grillo', edad=24, atletista=True)
# mostrar_claves_y_valores(pepe='nombre', apellido='Grillo', edad=24)
# mostrar_claves_y_valores(pepe='nombre', apellido='Grillo', edad=24, arquero=False)


# *args, **kwargs
# def mostrar_claves_y_valores(*args, **claves_y_valores):
#     for valor in args:
#         print(valor)
#     print('=======================================================')
#     for clave, valor in claves_y_valores.items():
#         print(clave, valor)
# mostrar_claves_y_valores('ea ea', pepe='nombre', apellido='Grillo', edad=24, arquero=False)
















# def cambio(dato_compuesto):
#     dato_compuesto.pop()
#     # print(dato_compuesto)

# dato_compuesto = [15,True,'otro valor']
# cambio(dato_compuesto)
# print(dato_compuesto)
# datos_compuesto2 = dato_compuesto
# dato_compuesto2 = dato_compuesto[:]
# cambio(dato_compuesto2)
# print(dato_compuesto)

# ================================================================================
# ================================================================================

# ¿Es posible que de alguna forma le digamos a Python cuándo queremos pasar un argumento por referencia o por valor?

# ================================================================================
# ================================================================================

# def cambio():
#     global valor
#     valor = 'pepe'

# valor = 15
# cambio()
# print(valor)

# Simular uno con el otro

# def cambio(valor):
#     valor = 'otro valor'
#     return valor

# valor = 15
# valor = cambio(valor)
# print(valor)


# def cambio(dato_compuesto):
#     dato_compuesto += ['otro valor']

# dato_compuesto = [15,True]
# cambio(dato_compuesto)
# print(dato_compuesto)

# ================================================================================
# ================================================================================

# Argumentos indeterminados
# *args - **kwargs
 
# ================================================================================
# ================================================================================

# *args
# def sumar(num1, num2, num3, num4, num5, sum6):
#     return sum([num1, num2, num3, num4, num5, sum6])

# suma = sumar(1,5,1,2,3)
# print(suma)

# def sumar(*args):
#     print(type(args))
#     print(args)
#     return sum(args)

# suma = sumar(1,5,1,2,3,13,12,41,1,2,3,4,5,67,5)
# print(suma)


# def unir(*valores):
#     print(' '.join(valores))
        
# unir('hola', 'pepe', 'como')

# def devuelva_iterable(*args):
#     # print(type(args))
#     return args[:15]

# # devuelva_iterable(1)
# print(devuelva_iterable(1,1,2,3,4,1,2,3,1,2,3,1,2,3,1,4,2,2,3,1,2,3,1,2,3,1,1))
# print(devuelva_iterable(1,1,2,3,2,3,1,2,3,1,1))

# ================================================================================
# ================================================================================

# **kwargs
# def generar_presentacion(nombre='Pepe', apellido='Grillo', edad=80, profesion='MIAAAAAMIIIIIIIIIIIIIII'):
#     return f'Buenas, soy {nombre} {apellido}. Tengo {edad} años. Mi profesion es {profesion}.'


# def generar_presentacion(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     presentacion = f'Buenas, soy {kwargs.get("nombre", "Pepe")} {kwargs.get("apellido", "Grillo")}. Tengo {kwargs.get("edad", "80")} años. Mi profesion es {kwargs.get("profesion", "grillo")}.'
#     # if 'pepe' in kwargs.keys():
#     #     presentacion += kwargs['pepe']
#     return presentacion

# # presentacion = generar_presentacion(apellido='Forti')
# presentacion = generar_presentacion(apellido='Forti', profesion1='MIAAAAAMIIIIIIIIIIIIIII', profesion2='MIAAAAAMIIIIIIIIIIIIIII', profesion='MIAAAAAMIIIIIIIIIIIIIII', profesion3='MIAAAAAMIIIIIIIIIIIIIII', profesion4='MIAAAAAMIIIIIIIIIIIIIII')
# print(presentacion)

# ================================================================================
# ================================================================================

# Ej reloj (sin tiempo asignado)

# Realiza una función que dependiendo de los parámetros que reciba: convierta a segundos o a horas.  
# 1- Si recibe un argumento, supone que son segundos y convierte a horas, minutos y segundos.
# 2- Si recibe 3 argumentos, supone que son hora, minutos y segundos y los convierte a segundos.

# def reloj(*args):
#     if len(args) == 1:
#         seg = args[0] % 60
#         min = args[0] // 60
#         hora = min // 60
#         min %= 60
#         return f'Los segundos {args[0]} equivalen a {hora} horas, {min} minutos y {seg} segundos'
#     elif len(args) == 3:
#         seg_totales = args[2]
#         seg_totales += args[1] * 60
#         seg_totales += args[0] * 60 * 60
#         return f'{args[0]}:{args[1]}:{args[2]} equivalen a {seg_totales} segundos.'
#     else:
#         return 'Solo acepto 1 o 3 valores'

# print(reloj(3600))
# print(reloj(1, 5, 5))

# version con **kwargs

# def reloj(**kwargs):
#     if len(kwargs.keys()) == 1:
#         seg = kwargs['seg'] % 60
#         min = kwargs['seg'] // 60
#         hora = min // 60
#         min %= 60
#         return f"Los segundos {kwargs['seg']} equivalen a {hora} horas, {min} minutos y {seg} segundos"
#     elif len(kwargs.keys()) == 3:
#         seg_totales = kwargs['seg']
#         seg_totales += kwargs['min'] * 60
#         seg_totales += kwargs['hs'] * 60 * 60
#         return f"{kwargs['hs']}:{kwargs['min']}:{kwargs['seg']} equivalen a {seg_totales} segundos."
#     else:
#         return 'Solo acepto 1 o 3 valores'

# print(reloj(seg=3600))
# print(reloj(hs=1, min=5, seg=5))

# ================================================================================
# ================================================================================

# Recursividad

# def funcion():
#     inicio bloque de codigo
#     funcion()
#     fin bloque de codigo


# funcion()

# ================================================================================
# ================================================================================

# Sin retorno
# def cuenta_regresiva(numero):
#     print(numero)
#     numero -= 1
#     if numero > 0:
#         cuenta_regresiva(numero)
#     else:
#         print("Boooooooom!")
#     print("Fin de la función",numero)

# cuenta_regresiva(5)

# ================================================================================
# ================================================================================

# Con retorno
# def factorial(numero):
#     print("Valor inicial ->",numero)
#     if numero > 1:
#         numero *= factorial(numero -1)
#     print("valor final ->",numero)
#     return numero

# print(factorial(5))

# ================================================================================
# ================================================================================

# Funciones integradas (built-in)

# int
# print(int('1'))

# float
# print(float('1.5'))
# print(float(True))

# str
# print(type(str(1)))

# round
# print(round(1.5))
# print(round(1.4))
# print(round(1.6))

# help()
# help(print)
# help(len)

# ================================================================================
# ================================================================================

# Revisión del desafio

'''Realiza una funcion llamada area_rectangulo() que devuelva el area del rectangulo a partir de una base
y una altura. Calcular el área de un rectángulo de 15 de base y 10 de atura'''

# def area_rectangulo(base, altura):
#     return base * altura

# # Solicitar al usuario la base y la altura del rectángulo
# base = int(input("Ingrese la base del rectángulo: "))
# altura = int(input("Ingrese la altura del rectángulo: "))

# # Calcular el área del rectángulo con la función area_rectangulo()
# rectangulo = area_rectangulo(base, altura)

# # Imprimir el resultado
# print("El área del rectángulo es:", rectangulo)

'''Realiza una funcion llamada area_circulo() que devuelva el area de un circulo a partir de un radio
. Calcular el área de un circulo de 5 de radio'''

# def area_circulo(radio, pi=3.14159):
#     return (radio ** 2) * pi

# # Solicitar al usuario el radio del circulo

# radio = int(input("Ingrese el radio del circulo: "))

# # Calcular el area del circulo con la funsion area_circulo()

# circulo = area_circulo(radio)

# # Imprimir el resultado

# print("El área del circulo es:", circulo)

'''Realiza una funcion llamada relacion() que a partir de dos números cumpla lo siguiente:

1-) Si el primer numero es mayor que el segundo, debe devolver 1
2-) Si el primer numero es menor que el segundo, debe devolver -1
3-) Si ambos numeros son iguales, debe devolver un 0'''

# def relacion(num1, num2):
#     if num1 > num2:
#         return "1"
#     elif num1 < num2:
#         return "-1"
#     else:
#         return "0"

# # Solicitar al usuario el num1 y num2

# num1 = int(input("Ingrese el primer numero: "))
# num2 = int(input("Ingrese el segundo numero: "))

# # comparar los numeros con la funsion relacion()

# comparacion = relacion(num1, num2)

# # Imprimir el resultado

# print(comparacion)

"""Realiza una funcion llamada recortar() que reciba tres parametros. El primero es el número a recortar, 
el segundo es el limite inferior y el tercero el limite superior. La función tendrá que cumplir lo siguiente:

1-) Devolver el limite inferior si el numero es menor que este
2-) Devolver el limite superior si el numero es mayor que este
3-) Devolver el numero sin cambios si no se supera ningún limite

compruebe el resultado de recortar 15 entre los limites 0 y 10"""

# def recortar(num, linferior, lsuperior):
#     if num < linferior:
#         return linferior
#     elif num > lsuperior:
#         return lsuperior
#     else:
#         return num

# print(recortar(15,0,10))

"""realiza una funcion llamada separar() que tome una lista de numeros enteros y devuelva dos listas ordenadas.
La primera con los numeros pares, y la segunda con los numeros impares:"""

# def separar(lista):
#     pares = []
#     impares = []
#     for num in lista:
#         if num % 2 == 0:
#             pares.append(num)
#         else:
#             impares.append(num)
#     pares.sort()
#     impares.sort()
#     return pares, impares

# lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# pares, impares = separar(lista)
# print(pares)
# print(impares)

