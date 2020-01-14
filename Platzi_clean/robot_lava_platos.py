from collections import deque

washing_dishes = deque([])


def run():
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
            while count <=0:
                count = int(
                    input('Ingresa el numero de platos que deseas agregar: ')
            add_ammount_dish(count)
                )

        elif command == '3':
            


if __name__ == '__main__':
    print('¡ Bienvenido a PlatziClean !'.center(100))
    print('')
    print('\(^~^)/'.center(100))
    run()
