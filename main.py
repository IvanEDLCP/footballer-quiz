import random

# Futbolistas
footballers = [
    {
        'name': 'Lionel Messi',
        'country': 'Argentina',
        'age': 36,
        'position': 'Delantero',
        'club': 'Inter Miami'
    },
    {
        'name': 'Cristiano Ronaldo',
        'country': 'Portugal',
        'age': 37,
        'position': 'Delantero',
        'club': 'Al Nassr'
    },
    {
        'name': 'James Rodriguez',
        'country': 'Colombia',
        'age': 32,
        'position': 'Mediapunta',
        'club': 'Al-Rayyan'
    },
    {
        'name': 'Neymar',
        'country': 'Brasil',
        'age': 30,
        'position': 'Extremo',
        'club': 'Paris Saint-Germain'
    },
    {
        'name': 'Kylian Mbappe',
        'country': 'Francia',
        'age': 23,
        'position': 'Extremo',
        'club': 'Paris Saint-Germain'
    }    
]

# Crear pista
def createClue(key, clue):

    match key:
        case 'country':
            print(f'Es de {clue}')
        case 'age':
            print(f'Tiene {clue} años')
        case 'position':
            print(f'Su posición es {clue}')
        case 'club':
            print(f'Juega en el {clue}')

# Escoger jugador
def choiceKey():

    footballer = random.choice(footballers)
    key = random.choice(list(footballer.keys()))
    name = footballer['name']

    if key != 'name':
        value = footballer[key]
        return (key, value, name)
        # createClue(key, value)

# Iniciar juego
def startGame():
    attemps = 3
    key, value, name = choiceKey()
    name = name.lower()
    print(f'Key: {key}, Value: {value}, Name: {name}')
    createClue(key, value)

    print(f'Intentos: {attemps}')
    userAnswer = input('Cual jugador crees que es? \n => ').lower()


    while attemps > 0:
        if name == userAnswer:
            print('====' * 6)
            print(f'Intentos: {attemps}')
            print(f'FELICIDADES, Si es {name.title()}')
            reset()
        elif userAnswer == '+pista':
            print('====' * 6)
            createClue(key, value)
            print(f'Intentos: {attemps}')
            userAnswer = input('Cual jugador crees que es? \n => ').lower()
        else:
            print('====' * 6)
            attemps -=1
            print('Intenta de nuevo')
            print(f'Intentos: {attemps}')
            userAnswer = input('Cual jugador crees que es? \n => ').lower()

        if attemps == 0:
            print('====' * 6)
            print(f'Intentos: {attemps}')
            print(f'Se te acabaron los intentos... \nEl jugador es {name.title()}, será pa la proxima Paí...');
            reset()

# Desplegar menu
def mainMenuGame():
    abstract = '''
    <=== ADIVINA EL JUGADOR ===>

    INSTRUCCIONES:

    Te dare una pista sobre un jugador de futbol y deberás escribir cual crees que es,
    si necesitas ayuda escribe "+pista" y te dare otra pista, tienes 3 intentos.
    Disfrutalo!

    Pdta: En el ultimo intento no podras obtener pistas.

    '''

    print(abstract)

    userOption = input('Iniciamos? \n => ').lower()

    if userOption == 'si':
        startGame()
        
    else:
        print('Ok, regresa cuando quieras!')

# Reiniciar juego
def reset():

    userOption = input('Quieres volver a jugar? \n=> ').lower()
    
    if userOption == 'si':
        mainMenuGame()
    else:
        print('Ok, regresa cuando quieras!')


mainMenuGame()