def run():

    # lista = [1,2,3,4,5,6,7,8,9,10]
    # numero_veces = lista.count(5) #La funcion count contabiliza cuantas veces hay un numero en una lista
    # print(numero_veces)

    # indice = lista.index(4) #Index, me devuelve el contenido de una posicion en especifico
    # print(indice)

    # lista = [3,4,7,9,1,8,2,10]
    # lista.sort() #Metodo SORT(), sirve para ordenar los elementos de una lista de mayor a menor
    # print(lista)

    productos = [
        ('Producto1', 20),
        ('Producto2', 40),
        ('Producto3', 5),
    ]

    def ordena_items(item):
        return item[1]

    # La funcion SORT(), me ordena una lista de menor a mayor una tupla, haciendo uso de una funcion ordena_items()
    productos.sort(key=ordena_items)
    print(productos)


if __name__ == '__main__':
    run()
