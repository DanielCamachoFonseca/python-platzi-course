#Implementacion de los diccionarios
def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }

    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_pais = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }

    print(poblacion_pais['Colombia'])

    for pais in poblacion_pais.keys(): #recorre el diccionario y me imprime los nombres de las llaves
        print(pais)

    for pais in poblacion_pais.values(): #recorre el diccionario y me imprime el contenido de las llaves
        print(pais)

    for pais, poblacion in poblacion_pais.items(): #recorre el diccionario y me imprime todo el contenido total del mismo, es decir, las llaves y su contenido
        print(pais + ' tiene ' + str(poblacion) + ' habitantes')


if __name__ == "__main__":
    run()