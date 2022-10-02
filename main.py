import string

#1)
numero1 = input('Introduce un numero: ')
print(type(numero1))
print("\n")
numero2 = int(input('introduce un numero: '))
print(type(numero2))
print("\n")
nunmero3 = float(input('introduce un numero: ' ))
print(type(nunmero3))
print("\n")
#2)
numero4 = int(input('introduce un numero: '))
print(str(numero4).zfill(6))
numero5 = float(input('introduce un numero: '))
print(str(numero5).zfill(7))
#3)
altura = 1.80
peso = 80.135
print('¿cuanto mides?', altura, 'm y ¿cuanto pesas?', peso, 'kg')
print (format('¿cuanto mides?'))
