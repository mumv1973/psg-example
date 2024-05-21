''' Imprime una tabla de verdad para la siguiente afirmación: "Una puerta tiene dos interruptores que controlan dos luces la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas, caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?'''


print(not (True ^ True))
print(not (True ^ False))
print(not (False ^ True))
print(not (False ^ False))
print('******************************')
print("Cuando ambos resultados son True, la puerta se abre")