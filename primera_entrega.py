
users = {'lilo': '12345', 'angel': '6789'}

def create_user():
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    users.update({username:password})
    return "El nuevo usuario ha sido creado"

def show_username_and_password():
    for key, value in users.items():
        print(key, value)
    return " "

def login():
    username = input("Ingrese su usuario: ")
    password = input("Ingrese su contraseña: ")
    if username in users and users[username] == password:
        print("Has iniciado sesión exitosamente.")
    else:
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")
    return " "   

repetir_menu = True # bandera/flag
while repetir_menu:
    print('''
==============
    Menu
==============
1. Crear un usuario.
2. Mostrar usuarios y contraseñas.
3. login
4. Salir
''')
    opcion_elegida = input('Ingrese la operacion a realizar: ')
    if opcion_elegida == '1':
        print(create_user())
    elif opcion_elegida == '2':
        print(show_username_and_password())
    elif opcion_elegida == '3':
        print(login())
    elif opcion_elegida == '4':
        repetir_menu = False
        print('Hasta luego!')
    else: 
        print('Vuelva a intentar con una opcion valida.')












