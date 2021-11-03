#Implementacion de break and continue en ciclos

def run():
    for contador in range(1000):
        if contador % 2 != 0:
            continue #A partir de continue no se ejecutara en el programa
        print(contador)

    for i in range(10000):
        print(i)
        if i == 5:
            break #break sirve para que se detenga el ciclo cuando se cumpla la condicion del IF
        
    texto = input('Ingresa un texto: ')
    for letra in texto:
        if letra == 'o':
            break
        print(letra)
            

if __name__ == "__main__":
    run()