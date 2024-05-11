""" print("Tipos de booleanos")
print(type(True))
print(type(False))
print(True)
print(False)

var_bool = bool(0)
var_bool2 = bool(1)

print(var_bool)
print(var_bool2)

var_bool3 = bool (-15)
print(var_bool3)

print(10 is 10)
print(10 is not 10)
print(10 == 10)
print(10 > 10)

print(10 is 10.0)
print(10 is not 10.0)

print("Asignacion de variables")
x = 10
y = x > 0
print(y)
dif_10 = x != 10
print(dif_10)


print("Operadores lógicos")

print("And")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print("Or")
print(True or True)
print(True or False)
print(False or True)
print(False or False)



print('Not')
print(not True)
print(not False)

print("**********")
print("Operadores lógicos y prioridad")
print(False and False or True)
print(False and (False or True))
print(not True and False or True)
print(not (True and False or False))
print(not True and (False or False))
print(not True and False or False)

 


print("Tablas de verdad de NAND")

print(not (True and True))

print ("Operador AND")
print (True and True)
print (True and False)
print (False and True)
print (False and False)

print ("Operador OR")
print (True or True)
print (True or False)
print (False or True)
print (False or False)

print ("Operador NAND")
print (not (True and True))
print (not (True and False))
print (not (False and True))
print (not (False and False))

print ("Operador NOR")
print (not (True or True))
print (not (True or False))
print (not (False or True))
print (not (False or False))


print("Ejemplo de uso Sensor y Batería")
sensor = True
bateria = True
print(sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print(sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print(sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print(sensor, "and", bateria, "=", sensor and bateria)""" 


# Determinar si el número 20 está en el rango 0 a 100

print('--------------------------------')
num1 = 20
num2 = 0
num3 = 100

print(num1 > num2 and num1 < num3)


print('--------------------------------')

print((20+15+16) > 50 )

print(15 % 3 == 0 and 15 % 5 == 0 and 15 % 2 == 1)

print (15 % 2) 
print('--------------------------------')

print("Cortocircuito con operador or")
x = 1
y = 0
print(x > 0 or (x/y) > 0)
print(x > 2 or (x/y) > 2) 
