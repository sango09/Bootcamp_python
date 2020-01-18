stack_dishes = []


def add_dish():
    stack_dishes.append('Plato')
    print('=' * 80)
    print('Se ha añadido un plato para lavar'.center(80))
    print('=' * 80)
    menu()


def add_amount(count):
    print('=' * 80)
    for i in range(count):
        stack_dishes.append('Plato')
    print('Se han añadido {} platos para lavar'.format(count).center(80))
    print('=' * 80)
    menu()


def wash_dish():
    print('=' * 80)
    if stack_dishes:
        print('Lavando plato', '.' * 30, '\nHe terminado')
        stack_dishes.pop()

        print('El numero de platos que hay para lavar es: {}'.format(
            str(len(stack_dishes))))
        print('=' * 80)
    else:
        return break_wash()
    menu()


def wash_dish_amount(count):
    for i in range(count):

        if stack_dishes:
            print('Lavando plato', '.' * 30, '\nHe terminado')
            stack_dishes.pop()

            print('El numero de platos que hay para lavar es: {}'.format(
                str(len(stack_dishes))))
            print('=' * 80)
        else:
            return break_wash()
    menu()


def list_dish():
    print('El numero de platos que hay para lavar es: {}'.format(
        str(len(stack_dishes))))
    menu()


def break_wash():
    print('''            
                        !SE HA ROTO EL LAVADO¡  
                     
                    MUCHAS GRACIAS POR ESCOGERNOS
                        Tenga un muy buen día''')
    print('')
    print('¡ APAGANDO ROBOT !'.center(65))
    print('/(-°-)\ '.center(65))


def menu():
    count = 0
    command = str(input("""
                    ¿Que deseas hacer?

                [1] Agregar plato al lavado
                [2] Agregar cantidad de platos al lavado
                [3] Lavar plato
                [4] Lavar cantidad de platos
                [5] Listar platos

                        [S]alir

    Ingresa una opcion: """))

    command = command.upper()

    if command == '1':
        add_dish()

    elif command == '2':
        while count <= 0:
            count = int(
                input('Ingresa el numero de platos que deseas agregar: '))
        add_amount(count)

    elif command == '3':
        wash_dish()

    elif command == '4':
        while count <= 0:
            count = int(
                input('Ingrese el numero de platos que desea lavar: '))
        wash_dish_amount(count)

    elif command == '5':
        list_dish()

    elif command == 'S':
        print('''    
                    MUCHAS GRACIAS POR ESCOGERNOS
                        Tenga un muy buen día''')
        print('')
        print('¡ APAGANDO ROBOT !'.center(70))
        print('/(-°-)\ '.center(70))

    else:
        print('')
        print('Comando invalido'.center(50, '='))
        menu()


if __name__ == '__main__':
    print('¡ Bienvenido a PlatziClean !'.center(100))
    print('')
    print('\(^~^)/'.center(100))
    menu()
