def run():

    print('¡Adivina en que año me gradue como ingeniero de sistemas!, solo tienes 2 intentos 😭')

    intentos = 0 

    while intentos < 2:
        año = int(input('¿En que año me gradue como ingeniero de sistemas? '))
        intentos += 1
        if año == 2022:
            print('¡Felicidades, acertaste el año en que me gradue!')
            break
        else:
            print('Perdiste!😭')
       
if __name__ == '__main__':
    run()
