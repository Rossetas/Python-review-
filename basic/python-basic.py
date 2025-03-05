# Mi primer **Hello World en Python**
print("Hello World in Python")
print("")

# **Ejercicio #1** Definir una función **num_max( )** que reciba como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que Python tiene una funcion *max( )* pero hacerla nosotros mismos es un buen ejercicio para iniciar).
def num_max(a=0, b=0):
  if (a > b):
    return a
  else:
    return b
  
print(num_max(2,5))
print(num_max(8,3))
print(num_max(0,-2))
print(num_max(5.5,1.1))
print("")

# **Ejercicio #2** Definir una función **num_max3( )** que reciba como argumento tres números y devuelva el mayor de ellos.
def num_max3(a=0, b=0, c=0):
  if (a > b) & (a > c):
    return a
  elif (b > a) & (b > c):
    return b
  else:
    return c
  
print(num_max3(1,2,3))
print(num_max3(10,9,8))
print(num_max3(2.5,8.8,4.8))
print("")

# **Ejercicio #3** Definir una función que calcula la longitud de una lista o de una cadena dada. 
# (Es cierto que Python tiene la función *len( )* incorporada, pero escribirla por nosotros mismos resulta en un muy buen ejercicio)
def calc_longitud(lista):
  long=0
  for i in lista:
    long+=1
    
  return long
  
print(calc_longitud([0,2,4,6,8]))
print(calc_longitud(["Ana", "Maria", "Jose"]))
print(calc_longitud(["Luis", 15, "Daniela", 55, "Mercedez", 24]))
print("")

# *Forma alternativa con la función len( )*
def calc_long(lista):
  long=len(lista)
  return long

print(calc_long([1,2,3,4]))
print(calc_long(["Pedro", 5, "Mario"]))
print("")

# **Ejercicio #4** Escribir una función que reciba un carácter y devuelva **True** si es una vocal o de lo contrario devuelva **False** si no lo es.
def is_vocal(char):
  vocales=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  if char in vocales:
    return True
  else:
    return False

print(is_vocal('a'))
print(is_vocal('b'))
print(is_vocal('3'))
print(is_vocal('E'))
print(is_vocal('M'))
print("")

# **Ejercicio #5** Escribir una función **sum( )** y una funcion **mult( )** que suman y multiplican respectivamente todos los números de una lista. 
# Por ejemplo *sum([1,2,3,4])* debe devolver 10 y *mult([1,2,3,4])* debe devolver 24
def sum(lista_sum):
  result_sum=0
  for i in lista_sum:
    result_sum += i
    
  return result_sum

def mult(lista_mult):
  result_mult = lista_mult[0]
  i=1
  while i in range(1,len(lista_mult)):
    result_mult = result_mult * lista_mult[i]
    i+=1
    
  return result_mult

print(sum([1,2,3,4]))
print(mult([1,2,3,4]))
print("")

# **Ejercicio #6** Escribir una función **inversa( )** que calcule la forma inversa de una cadena. 
# Por ejemplo la cadena *"estoy probando"* debe devolver la cadena *"odnaborp yptse"*
def inversa(cadena):
  longitud = len(cadena)
  new_cadena = str()
  for i in range(longitud-1,-1,-1):
    new_cadena += cadena[i]
    
  return new_cadena

print(inversa("estoy probando"))
print(inversa("python"))
print("")

# *Forma alternativa simplificada*
def inverse(string):
  return string[::-1]

print(inverse("Estoy Probando"))
print(inverse("Python"))
print("")

# **Ejercicio #7** Escribir una función **palindromo( )** que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), por ejemplo *palindromo("radar")* debe devolver **True**
def palindromo(cadena):
  cadena_reverse = str()
  for n in cadena:
    cadena_reverse = n + cadena_reverse
  if cadena == cadena_reverse:
    return True
  else:
    return False
  
print(palindromo("radar"))
print(palindromo("casa"))
print(palindromo("ala"))
print("")

# *Forma alternativa simplificada*
def is_palindromo(palabra):
  return palabra == palabra[::-1]

print(is_palindromo("radar"))
print(is_palindromo("casa"))
print(is_palindromo("ala"))
print("")

# **Ejercicio #8** Definir una función **superposicion( )** que tome dos listas y devuelva **True** si tienen 
# al menos 1 miembro en común o devuelva **False** de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(listaA, listaB):
  for elemt1 in listaA:
    for elemt2 in listaB:
      if elemt1 == elemt2:
        return True
      
  return False
      
print(superposicion([1,2,3],[4,5,6]))
print(superposicion([0,5,10],[1,5,8]))
print(superposicion([1,3,7],[2,7,9]))
print("")

#*Forma alternativa simplificada*
def superposicion(list1, list2):
  for elemt in list1:
    if elemt in list2:
      return True
    
  return False

print(superposicion([1,2,3],[4,5,6]))
print(superposicion([0,5,10],[1,5,8]))
print(superposicion([1,3,7],[2,7,9]))
print("")

# **Ejercicio #9** Definir una función **generar_n_caracteres( )** que tome un entero **n** 
# y devuelva el carácter multiplicado por n. Por ejemplo *generar_n_caracteres(5, 'x')* debe devolver
# "xxxxx"
def generar_n_char(n, char):
  for i in char:
    return (n * char)
  
print(generar_n_char(5, 'x'))
print(generar_n_char(3, 'abc'))
print(generar_n_char(6, '1'))
print(generar_n_char(0, 'A')) # try case
print("")

# **Ejercicio #10** Definir una función **histograma( )** que tome una lista de números enteros 
# e imprima un histograma en la pantalla. Ejemplo *histograma([4,9,7])*

# ****
# *********
# *******

def histograma(lista):
  print("Histograma:")
  for i in lista:
    histograma_result = "*" * i
    print(histograma_result)

histograma([4,9,7])
histograma([5,10,5])
print("")