

print("hola")
print("adios")

#operadores aritméticos
1+1
print(2+1)
print(2-1)
print(2*2)
print(2/2)
#precendecia de operadores
print(5+8*(3+2))

#tipos de datos
print(type(2))
print(type(2.2))
print(type("texcto"))
print(type('textito'))
print(type("22222"))

##############################variables####################
mensaje = "Mensaje" 
print(mensaje)
mensaje = "mensaje 1"
print(mensaje)
print(type(mensaje))
mensaje = 2
print(mensaje)
print(type(mensaje))

########################################################

mis3animales = "perico, gallo, chivo"
print(mis3animales)
tresáñimales = "perico, gallo, chivo"
print(tresáñimales)

texto1 = "Primer texto"
texto11 = "Segundo texto"
print(texto1 + texto11)

#transforman str() int() float()
edad = 22
print("La edad es: " + str(edad))
print("El tipo de dato de edad es: " + str(type(edad)))

import math
#morado= funciones #amarillo= valores
grados = 45.0
radianes = (grados * math.pi)/ 180
seno = math.sin(radianes)
print("seno de 45° : " + str(seno))

def saludar(nombre): 
    print("Buenos dias" + nombre)
    print("mucho gusto")
    print("que tal?")

def despedir():
    print("hasta la protsima")
    print("adios")

def concatenar(parte1, parte2):
    return parte1 + parte2

print("adios")
saludar("gg")
despedir()

frase = concatenar("well play", " gg") 
print(frase)