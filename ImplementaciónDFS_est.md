# **Implementación de Depth-first search (DFS)**

## **Objetivo**

Implementar Depth-first search (DFS) para encontrar un camino desde un punto de inicio hasta una meta en un laberinto representado como una matriz.



**Nombres y Appellidos:**
Alfonso Chafla

**Fecha:**
02-04-2025


## **Paso 1: Representar el laberinto**

**Instrucciones:**

* Crear una matriz (de almenos 5 x 5) donde:

  * **0** representa camino libre

  * **1** representa una pared u obstáculo

* Definir el punto de **inicio** y el de **meta**

Use la siguiente matriz para comprobar su código:

maze = [
    
    [0, 1, 0, 0, 0],

    [0, 1, 0, 1, 0],

    [0, 0, 0, 1, 0],

    [1, 1, 0, 0, 0],

    [0, 0, 0, 1, 0]
]

start = (0, 0)

goal = (4, 4)


```python
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)
```

## **Paso 2: Validar Movimientos**

**Instrucciones**

Crear una función que verifique si una posición está dentro del laberinto y no es una pared.

**Pseudocódigo**


```python
Función es_valido(pos):
    x ← pos[0]
    y ← pos[1]

    Si x < 0 o x ≥ número de filas:
        retornar FALSO
    Si y < 0 o y ≥ número de columnas:
        retornar FALSO
    Si maze[x][y] == 1:
        retornar FALSO
```


      File "<ipython-input-2-81c0319c8eed>", line 2
        x ← pos[0]
          ^
    SyntaxError: invalid character '←' (U+2190)
    



```python
# Implemente su código aquí
def is_valid(pos):
  x=pos[0]
  y=pos[1]
  if(x<0 or x>=len(maze)):
    return False
  if(y<0 or y>=len(maze)):
    return False
  if(maze[x][y]==1):
    return False
  # si no cumple nada de lo anterior, debe ser que la posicion si es valida
  return True

```


```python
# Compruebe su función antes de seguir a la siguiente sección, ejecutando el siguiente código.

print(is_valid((0, 0)))  # True
print(is_valid((0, 1)))  # False
print(is_valid((5, 5)))  # False
```

    True
    False
    False
    

## **Paso 3: Generar Vecinos (Sucesores)**

**Instrucciones**

Crear una función que devuelva los vecinos válidos (arriba, abajo, izquierda, derecha).

**Pseudocódigo**


```python
Función obtener_vecinos(pos):
    x ← pos[0]
    y ← pos[1]

    vecinos ← [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    vecinos_validos ← []

    Para cada v en vecinos:
        Si es_valido(v):
            agregar v a vecinos_validos

    retornar vecinos_validos
```


```python
# Implemente su código aquí
def get_neighbors(pos):
  x=pos[0]
  y=pos[1]
  #Arriba, abajo, izquierada y derecha de donde estoy en ese momento
  vecinos=[(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
  vecinos_validos=[]
  for v in vecinos:
    if(is_valid(v)):
      vecinos_validos.append(v)
  return vecinos_validos

```


```python
# Compruebe su función antes de seguir a la siguiente sección, ejecutando el siguiente código.
print(get_neighbors((0, 0)))  # [(1, 0)]
print(get_neighbors((2, 2)))  # [(1,2), (3,2), (2,1)]
```

    [(1, 0)]
    [(1, 2), (3, 2), (2, 1)]
    

## **Paso 4: Implementar DFS**

**Instrucciones**

Usar una pila para explorar el laberinto con DFS y encontrar el camino al objetivo.

**Pseudocódigo**


```python
Función dfs(inicio, meta):
    pila ← [(inicio, [inicio])]
    visitados ← conjunto vacío

    Mientras pila no está vacía:
        (actual, camino) ← sacar el último de la pila

        Si actual está en visitados:
            continuar

        Agregar actual a visitados

        Si actual == meta:
            retornar camino

        Para cada vecino en obtener_vecinos(actual):
            Si vecino no está en visitados:
                agregar (vecino, camino + vecino) a la pila

    retornar NULO (no se encontró camino)
```


```python
# Implementar su código aquí
def dfs(inicio,meta):
  pila=[(inicio,[inicio])]
  visitados=[]
  while len(pila)!=0:
    print("buscando")
    actual,camino=pila.pop()
    print(str(actual)+"|"+str(camino))

    if actual in visitados:
      continue

    visitados.append(actual)

    if(actual==meta):
      return camino

    for vecino in get_neighbors(actual):
      if vecino  not in visitados:
        camino.append(vecino)
        pila.append((vecino,camino))
  return None


```


```python
# Compruebe su código antes de seguir a la siguiente sección, ejecutando el siguiente código.

path = dfs(start, goal)
print("Camino encontrado:", path)
```

    buscando
    (0, 0)|[(0, 0)]
    buscando
    (1, 0)|[(0, 0), (1, 0)]
    buscando
    (2, 0)|[(0, 0), (1, 0), (2, 0)]
    buscando
    (2, 1)|[(0, 0), (1, 0), (2, 0), (2, 1)]
    buscando
    (2, 2)|[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    buscando
    (3, 2)|[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (3, 2)]
    buscando
    (3, 3)|[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (3, 2), (4, 2), (3, 3)]
    buscando
    (3, 4)|[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (3, 2), (4, 2), (3, 3), (3, 4)]
    buscando
    (4, 4)|[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (3, 2), (4, 2), (3, 3), (3, 4), (2, 4), (4, 4)]
    Camino encontrado: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (3, 2), (4, 2), (3, 3), (3, 4), (2, 4), (4, 4)]
    

## **Paso 5: Visualizar el Camino**

**Instrucciones**

Crear una función para mostrar el laberinto, indicando el camino encontrado, el inicio y la meta.

**Pseudocódigo**


```python
Función imprimir_laberinto_con_camino(camino):
    Para cada fila i:
        Para cada columna j:
            Si (i,j) es inicio:
                imprimir "S"
            Sino si (i,j) es meta:
                imprimir "G"
            Sino si (i,j) está en camino:
                imprimir "*"
            Sino si maze[i][j] == 1:
                imprimir "#"
            Sino:
                imprimir "."
        Imprimir nueva línea
```


```python
# Implementar su código aquí
#hice que a cada row del arreglo se concatenen en un str que se imprime al final
def imprimir_laberinto_con_camino(camino):
  for i in range(0,len(maze)):
    row=""
    for j in range(0,len(maze)):
      if(i,j)==start:
        row=row+"s "
      elif (i,j)==goal:
        row=row+"g "
      elif (i,j) in camino:
        row=row+"* "
      elif maze[i][j]==1:
        row=row+"# "
      else:
        row=row+". "
    print(row)


```


```python
imprimir_laberinto_con_camino(path)
```

    s # . . . 
    * # * # . 
    * * * # * 
    # # * * * 
    . . * # g 
    

# **Pregunta**

**¿Usted cree que algoritmo de inteligencia artificial DFS, es un algoritmo inteligente (razona, aprende, optimiza)? Justifique su respuesta.**

No realmente, osea toda la logica matematica la desarrollaron humanos hace varios años, el algoritmo lo unico que hace es seguir instrucciones que se le dan y nada mas. El algoritmo no piensa tal cual.


