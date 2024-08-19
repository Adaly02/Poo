def solicitar_textos():
    textos = []
    for i in range(3):
        texto = input(f"Ingrese el texto {i + 1}: ")
        textos.append(texto)
    return textos

def calcular_promedio_longitud(textos):
    total_longitud = sum(len(texto) for texto in textos)
    promedio = total_longitud / len(textos)
    return promedio

def concatenar_textos(textos):
    concatenado = ''.join(textos)
    longitud = len(concatenado)
    
    if longitud > 15:
        comparacion = "mayor que"
    elif longitud < 15:
        comparacion = "menor que"
    else:
        comparacion = "igual a"
    
    return concatenado, comparacion

def texto_mas_largo(textos):
    texto_max = max(textos, key=len)
    return texto_max

def contar_caracteres_numericos(texto):
    return sum(c.isdigit() for c in texto)

#corrida
textos = solicitar_textos()

#Promedio de las longitudes de los textos
promedio = calcular_promedio_longitud(textos)
print(f"El promedio de las longitudes de los textos es: {promedio:.2f}")

#Concatenar textos e indicar si el largo es mayor, menor o igual a 15
texto_concatenado, comparacion = concatenar_textos(textos)
print(f"El texto concatenado es: '{texto_concatenado}' y su longitud es {comparacion} 15.")

#Indicar cuál de los textos posee más caracteres
texto_mayor = texto_mas_largo(textos)
print(f"El texto con más caracteres es: '{texto_mayor}'")

#Concatenar textos e indicar la cantidad de caracteres numéricos existentes
numericos = contar_caracteres_numericos(texto_concatenado)
print(f"La cantidad de caracteres numéricos en el texto concatenado es: {numericos}")
