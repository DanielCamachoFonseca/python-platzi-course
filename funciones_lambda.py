# Funciones lambda o anonimas
def run ():

    # Funcion normal
    def sumar(a,b):
        return a + b 
    print(sumar(4,2))


    # Funcion lambda con dos parametros - Example 1
    suma = lambda a,b : a+b #Las variables que esten antes de los dos puntos son los parametros de la funcion
    print(suma(4,2))


    # Ejemplo implemetando la funcion lambda - Example 2
    lista = [1,2,3,4,5,6,7,8,9,10]
    lista_filtrada = filter(lambda numero: numero % 2 == 0, lista)
    pares = list(lista_filtrada)
    print(pares)

    # Example 2
    productos = [
        ('producto1', 10),
        ('producto2', 20),
        ('producto3', 30),
        ('producto4', 40),
    ]

    # La funcion MAP(), toma una funcion y una lista y aplica esa funcion a cada elemento de esta lista
    precios = list(map(lambda producto: producto[1], productos))
    print(precios)


    #Ejemplo reduccion de uso de funciones de python
    productos = [
        ('producto1', 100),
        ('producto2', 10),
        ('producto3', 12),
        ('producto4', 500),
    ]

    #Filtrados
    productos_filtrados = list(filter(lambda item: item[1] >= 100, productos))
    print(f'productos_filtrados {productos_filtrados}')

    #mapeados
    productos_mapeados = list(map(lambda producto: producto[1], productos))
    print(f'productos_mapeados {productos_mapeados}')

    #Reduccion
    prod_fil_comprimidos = [item for item in productos if item[1]>=100 ]
    print(prod_fil_comprimidos)
    
    prod_map_comprimidos = [item[1] for item in productos]
    print(prod_map_comprimidos)

if __name__ == '__main__':
    run()
   