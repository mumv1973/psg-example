"""  Escribe un programa en Python que convierta las siguientes # temperaturas de grados Celsius a Fahrenheit.  

 Formula base 
fahrenheit = (celsius * 9/5) + 32 """ 

# temperaturas expresadas en Grados centigrados. 
temp_1 = 30
temp_2 = -273.99 
temp_3 = 100 

resultado_1 = ( temp_1 * (9/5)) + 32

resultado_2 = ( temp_2 * (9/5)) + 32

resultado_3 = ( temp_3 * (9/5)) + 32


print (str(temp_1) + " Grados Centigrados a Fahrenheit son: " + str(resultado_1 ) )

print (str(temp_2) + " Grados Centigrados a Fahrenheit son: " + str(resultado_2 ))

print (str(temp_3) + " Grados Centigrados a Fahrenheit son: " + str(resultado_3 ) )
