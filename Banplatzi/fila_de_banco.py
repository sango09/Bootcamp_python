# Utilities
from collections import deque

# Row to bank
row_deposit = deque([])
row_account = deque([])

# counter of turn
COUNT_DEP = 0
COUNT_ACC = 0


def add_row(client_deposit):
    print(' Ha sido agregado a la fila '.center(50, '='))
    print('')
    print('Turno | Nombre | Cedula |')
    print('')
    print('{uid_deposit} | {name} | {id} |'.format(
            uid_deposit=client_deposit['turn'],
            name=client_deposit['name'],
            id=client_deposit['id'],))
    run()


def serv_client():
    # Attend bank clients
    if row_account:
        client = row_account.popleft()
        print('Fila de APERTURA DE CUENTAS: Turno: {} , Cliente: {}'.format(
            client['turn'], client['name']))
        print('')
        print('El cliente debe ser atendido'.center(50, '='))
        run()

    elif row_deposit:
        client = row_deposit.popleft()
        print('Fila de DEPOSITO: Turno: {} , Cliente: {}'.format(
            client['turn'], client['name']))
        print('')
        print('El cliente debe ser atendido'.center(50, '='))
        run()

    else:
        print('NO HAY CLIENTES PARA ATENDER'.center(50, '='))
        print(''.center(50, '*'))
        run()


def list_clients():
    # All clients in the rows
    total = (row_account + row_deposit)
    print('El banco tiene {} clientes por atender'.format(
        len(total)).center(50)
    )

    print('')
    print('Fila de DEPOSITO tiene: {} clientes'.format(
        len(row_deposit))
    )
    print('')
    print('Fila de APERTURA DE CUENTA tiene: {} clientes'.format(
        len(row_account))
    )
    run()


def _get_client_field(field_name, message='¿Cual es {} del cliente?: '):
    # Get client input
    field = None
    while not field:
        field = input(message.format(field_name))
    return field


def _get_client_from_user(pas):
    client = {
        'name': _get_client_field('el nombre'),
        'id': _get_client_field('la cedula'),
        'turn': assign_shift(pas)
    }
    return client


def assign_shift(pas):
    
    if pas == 'd':
        global COUNT_DEP
        COUNT_DEP += 1
        return str("DP - " + str(COUNT_DEP))
    else:
        global COUNT_ACC
        COUNT_ACC += 1
        return str("ACC - " + str(COUNT_ACC))


def run():
    # commands for services
    command = str(input("""
        ¿Que deseas hacer hoy?

    [1] Agregar cliente a fila de depositos
    [2] Agregar cliente a fila de apertura de cuenta
    [3] Atender cliente
    [4] Listar clientes en fila

            [S]alir
    : """))
    command = command.upper()

    if command == '1':
        print('FILA PARA DEPÓSITO'.center(50, '='))
        print('')
        client_deposit = _get_client_from_user("d")
        row_deposit.append(client_deposit)
        add_row(client_deposit)

    elif command == '2':
        print('FILA PARA APERTURA DE CUENTAS'.center(50, '='))
        print('')
        new_account = _get_client_from_user("a")
        row_account.append(new_account)
        add_row(new_account)

    elif command == '3':
        print(' TURNO DEL CLIENTE POR ATENDER'.center(50, '='))
        print('')
        serv_client()

    elif command == '4':
        print(' LISTA DE CLIENTES EN LA FILA '.center(50, '='))
        print('')
        list_clients()

    elif command == 'S':
        print('¡ Gracias por usar Banplatzi !'.center(50, '-'))
        return 1

    else:
        print('Comando invalido')


if __name__ == '__main__':
    # Message welcome
    print(' BIENVENIDO A BANPLATZI '.center(50, '='))
    run()
