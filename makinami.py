oracion = input("Ingrese texto: ") #<- ingreso de texto

oracionS = oracion.split() #<- separacion de oracion por palabras

#ingreso al archivo historial para ingresar lo copiado
historial = open("historial.txt", "a")
historial.write(str("\n" + oracion))
historial.close()

# Abre el archivo "palabras.txt" en modo de lectura y escritura
with open("palabras.txt", "r+") as archivo:
  # Lee el contenido del archivo y almacena cada palabra en un diccionario
  palabras = {}
  for linea in archivo:
    palabra, identificador = linea.strip().split(": ")
    palabras[palabra] = int(identificador)

  # Obtiene el último identificador utilizado y lo incrementa en 1
  ultimo_identificador = max(palabras.values()) if palabras else 0
  nuevo_identificador = ultimo_identificador + 1

  # Recorre la lista de palabras y las agrega al diccionario si no están allí
  for palabra in oracionS:
    if palabra not in palabras:
      palabras[palabra] = nuevo_identificador
      nuevo_identificador += 1

  # Escribe las palabras y sus identificadores en el archivo "palabras.txt"
  archivo.seek(0)
  archivo.truncate()
  for palabra, identificador in palabras.items():
    archivo.write(f"{palabra}: {identificador}\n")

# Abre el archivo "palabras.txt" en modo de lectura y crea un diccionario con sus contenidos
with open("palabras.txt", "r") as archivo:
  palabras = {}
  for linea in archivo:
    palabra, identificador = linea.strip().split(": ")
    palabras[palabra] = int(identificador)

# Crea una nueva lista "oracionT" con los identificadores de las palabras de la lista "oracionS"
oracionT = []
for palabra in oracionS:
  identificador = palabras.get(palabra)
  if identificador is not None:
    oracionT.append(identificador)

# Convierte la lista "arregloT" en una cadena separada por comas
arregloT_str = ",".join(str(numero) for numero in oracionT)

# Abre el archivo "arregloT.txt" en modo de escritura y escribe la cadena "arregloT_str" seguida de un salto de línea
with open("oracionT.txt", "a") as archivo:
  archivo.write(arregloT_str + "\n")


#ARCHIVO QUE GUARDA LAS RELACIONES DE CADA TOKEN

# Crea un diccionario para almacenar las relaciones y sus frecuencias
relaciones = {}

# Abre el archivo si ya existe y actualiza las frecuencias de las relaciones
try:
    with open('relaciones.txt', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            relacion, frecuencia = linea.split(' : ')
            frecuencia = int(frecuencia)
            relacion = tuple(map(int, relacion.split(' , ')))
            relaciones[relacion] = frecuencia
except FileNotFoundError:
    pass

# Itera sobre el array y encuentra las relaciones
for i in range(1, len(oracionT)-1):
    # Encuentra las relaciones con el vecino anterior y siguiente
    relacion_anterior = (oracionT[i], oracionT[i-1])
    relacion_siguiente = (oracionT[i], oracionT[i+1])
    
    # Actualiza las frecuencias de las relaciones si ya existen
    if relacion_anterior in relaciones:
        relaciones[relacion_anterior] += 1
    else:
        relaciones[relacion_anterior] = 1
        
    if relacion_siguiente in relaciones:
        relaciones[relacion_siguiente] += 1
    else:
        relaciones[relacion_siguiente] = 1

# Crea un archivo .txt y escribe las relaciones y sus frecuencias
with open('relaciones.txt', 'w') as archivo:
    for relacion, frecuencia in relaciones.items():
        archivo.write(f'{relacion[0]} , {relacion[1]} : {frecuencia}\n')

#----------------------------SIGUENTE ES LIMPIAR LAS ORACIONES PARA QUITAR PALABRAS INESESARIAS-------------------------------------