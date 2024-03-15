u = "BCC-2215"
c = "225125"
#Registro para el usuario y la contraseña
while True:
    print("Ingrese su usuario:")
    u1 = input()
    print("Ingresa la contraseña:")
    c1 = input()
    if c == c1 and u1 == u:
        print("Contraseña correcta y usuario correcto. Bienvenido.")
        break
    else:
        print("Contraseña incorrecta y/o usuario incorrecto. Intenta de nuevo.")
    #Cuando inicia sesion de manera adecuada manda las opciones disponibles    
print("Seleccione una acción:")
print("1) Retirar")
print("2) Depositar")
print("3) Realizar una transferencia")
print("4) Estado de la cuenta")
print("5) Cancelar operación")
r = input()
#al seleccionar una operacion en este caso el de retirar le dara dos opciones retiro monetario y de monto variable 
if r == "1":
    print("¿Qué desea retirar?")
    print("1) Monetario")
    print("2) Monto variable")
    val = input()

    if val == "1":
        print("¿Cuánto desea retirar?")
        print("1) 100")
        print("2) 200")
        print("3) 300")
        print("4) 1000")
        v2 = input()
        if v2 == "1":
            print("Su retiro es exitoso")
            print("Se le acreditan: Q100")
        elif v2 == "2":
            print("Su retiro es exitoso")
            print("Se le acreditan: Q200")
        elif v2 == "3":
            print("Su retiro es exitoso")
            print("Se le acreditan: Q300")
        elif v2 == "4":
            print("Su retiro es exitoso")
            print("Se le acreditan: Q1000")
#aqui inicia el monto variable
    if val == "2":
        print("Ingrese el monto que desea")
        v = input()
        print("Su retiro es exitoso")
        print("Se le acreditan: Q", v)
# iniciamos con los datos para realizar el deposito
if r=="2":
    print("¿Cuanto desea depositar?")
    r1=input()
def convertir_a_letras(numero):
    unidades = ['', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve']
    decenas = ['', 'Diez', 'Veinte', 'Treinta', 'Cuarenta', 'Cincuenta', 'Sesenta', 'Setenta', 'Ochenta', 'Noventa']
    centenas = ['', 'Ciento', 'Doscientos', 'Trescientos', 'Cuatrocientos', 'Quinientos', 'Seiscientos', 'Setecientos', 'Ochocientos', 'Novecientos', 'Mil']

    numero_entero = int(numero)
    texto = ''
    if numero_entero == 0:
        texto = 'Cero'
    elif numero_entero < 10:
        texto = unidades[numero_entero]
    elif numero_entero < 100:
        decena = numero_entero // 10
        unidad = numero_entero % 10
        if unidad == 0:
            texto = decenas[decena]
        else:
            texto = decenas[decena] + ' y ' + unidades[unidad]
    elif numero_entero < 1000:
        centena = numero_entero // 100
        resto = numero_entero % 100
        if resto == 0:
            texto = centenas[centena]
        else:
            texto = centenas[centena] + ' ' + convertir_a_letras(resto)
    else:
        texto = 'Número demasiado grande para convertir a letras'

    return texto

numero = input("Ingrese un número: ")
print(convertir_a_letras(numero))
