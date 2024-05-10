# Convertir a cuantos dias, horas y minutos corresponden la siguiente cantidad de segundos:# 

segundos_total = 288325

print(segundos_total)

# Calcular cantidad de segundos que tiene 1  dia y obtener cantidad de dias.#

segundos_dia = 60 * 60 * 24

print("Un dia tiene: " + str(segundos_dia) + " segundos")

calculo_dias_enteros = segundos_total / segundos_dia

print("De: " + str(calculo_dias_enteros) + " Solo tomamos los dias enteros ")

print("Total segundos en 3 dias: " + str (3 * 86400))

# Del saldo de segundos calcular cantidad de horas posibles y saber segundos restantes. 

saldo1_segundos = segundos_total - ((3 * segundos_dia) )

print("Saldo 1: " + str( saldo1_segundos) + " segundos")


print ("**************")
segundos_en_1_hora = 60 * 60


print ("Una hora tiene: " + str( segundos_en_1_hora) + " segundos")

calculo_horas_enteros = saldo1_segundos / segundos_en_1_hora
print ("De: " + str(calculo_horas_enteros) + " Solo tomamos las horas enteras" )

print("Total segundos en 8 horas: " + str(8 * segundos_en_1_hora ))



total_segundos_ocho_horas = 8 * segundos_en_1_hora


saldo2_segundos = saldo1_segundos - total_segundos_ocho_horas

print("Saldo 2:" + str (saldo2_segundos) + "  segundos")

# calculo minutos y saldo segundos. 
print ("**************")

print("Un minuto tiene: 60 segundos")

calculo_minutos = saldo2_segundos / 60

print("De: " + str(calculo_minutos) + " Solo tomamos los minutos enteros")

total_minutos = 5 * 60 

saldo3_segundos = saldo2_segundos - total_minutos

print("Saldo segundos: " + str(saldo3_segundos))

print(str(segundos_total) + " segundos, Son: 3 Dias, 8 horas, 5 minutos y 25 segundos " )











