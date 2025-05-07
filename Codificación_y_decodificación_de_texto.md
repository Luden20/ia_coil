# Generacion de diccionarios para codificar y decodificar
Por Alfonso Chafla :D
Aqui genero una lista con las letras y iterando guardo como corresponde en forma de que pueda codificar y decodificar

Use diccionarios porque de esta forma me era mucha mas facil empatar que dato va con que dato, ademas lleno los diccionarios recorriendo la lista de letras y llenado de tal manera que x y son las claves, y recorro la lista con un i que sumo en cada bucle interno

Hay que saber bien la forma en la que se llena la matriz para el for porque me paso que al no poner los for adecuadamente letras no se guardaban


```python
letras=['A','B','C','D','E','F','G','H','IJ','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
i=0
decod={}
cod={}
for x in range(9,4,-1):
  for y in range(0,5):
    decod[x,y]=letras[i]
    cod[letras[i]]=(x,y)
    i=i+1
print(decod)
print(cod)
```

    {(9, 0): 'A', (9, 1): 'B', (9, 2): 'C', (9, 3): 'D', (9, 4): 'E', (8, 0): 'F', (8, 1): 'G', (8, 2): 'H', (8, 3): 'IJ', (8, 4): 'K', (7, 0): 'L', (7, 1): 'M', (7, 2): 'N', (7, 3): 'O', (7, 4): 'P', (6, 0): 'Q', (6, 1): 'R', (6, 2): 'S', (6, 3): 'T', (6, 4): 'U', (5, 0): 'V', (5, 1): 'W', (5, 2): 'X', (5, 3): 'Y', (5, 4): 'Z'}
    {'A': (9, 0), 'B': (9, 1), 'C': (9, 2), 'D': (9, 3), 'E': (9, 4), 'F': (8, 0), 'G': (8, 1), 'H': (8, 2), 'IJ': (8, 3), 'K': (8, 4), 'L': (7, 0), 'M': (7, 1), 'N': (7, 2), 'O': (7, 3), 'P': (7, 4), 'Q': (6, 0), 'R': (6, 1), 'S': (6, 2), 'T': (6, 3), 'U': (6, 4), 'V': (5, 0), 'W': (5, 1), 'X': (5, 2), 'Y': (5, 3), 'Z': (5, 4)}
    

# Funciones
Estas son las funciones para codificar y decodificar, usando el diccionario apropiado busca el valor o el par de claves y devuelve el contenido.
Ambas funciones reciben como parametro el correspondiente diccionario


```python
#Funcion para eliminar espacios intermedios, y ajustar el formato
def trabajar_cadena(mensaje):
  mensaje=mensaje.strip()
  mensaje=mensaje.upper()
  res=""
  for char in mensaje:
    if(char!=' '):
      res=res+char
  return res
```


```python
def codifica(mensaje,cod):
  res=""
  mensaje=trabajar_cadena(mensaje)
  for x in mensaje:
    aux1,aux2=cod[x]
    res=res+str(aux1)+str(aux2)
  return res
print(codifica("hola mundo",cod))
```

    827370907164729373
    


```python
def decodifica(codificado,decod):
  res=""
  i=0
  while(True):
    if(i>=len(codificado)):
      break
    aux1=int(codificado[i])
    aux2=int(codificado[i+1])
    res=res+decod[aux1,aux2]
    i=i+2
  return res
decodifica("827370907164729373",decod)

```




    'HOLAMUNDO'


