# Utilities
from collections import deque

# Row to bank
row_deposit = deque([])
row_account = deque([])

# counter of turn
idx_deposit = 0
idx_account = 0


def add_deposit(client_deposit):
    # Add client to deposit row
    global idx_deposit

    idx_deposit += 1
    row_deposit.append('Turno ' + str(idx_deposit))
    print(' Ha sido agregado a la fila '.center(50, '='))

    print('')
    print('Turno | Nombre | Cedula |')
    print('')

    print('{uid_deposit} | {name} | {id} |'.format(

        uid_deposit=idx_deposit,
        name=client_deposit['name'],
        id=client_deposit['id'],

    ))


def add_account(new_account):
    # Add client to account row
    global idx_account

    idx_account += 1
    row_account.append('Turno: ' + str(idx_account))
    print(' Ha sido agregado a la fila '.center(50, '='))

    print('')
    print('Turno | Nombre | Cedula |')
    print('')

    print('{uid_account} | {name} | {id} |'.format(

        uid_account=idx_account,
        name=new_account['name'],
        id=new_account['id']
    ))


def serv_client():
    # Attend bank clients
    if row_account:
        print('Fila de APERTURA DE CUENTAS: {}'.format(
            row_account[0])
        )
        print('')

        print('El cliente debe ser atendido'.center(50, '='))
        row_account.popleft()
        run()

    elif row_deposit:
        print('Fila de DEPOSITO: {}'.format(
            row_deposit[0])
        )
        print('')

        print('El cliente debe ser atendido'.center(50, '='))
        row_deposit.popleft()
        run()

    else:
        print('NO HAY CLIENTES PARA ATENDER'.center(50, '='))
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


def _get_client_field(field_name, message='¿Cual es {} del cliente?: '):
    # Get client input
    field = None

    while not field:
        field = input(message.format(field_name))

    return field


def _get_client_from_user():
    #
    client = {
        'name': _get_client_field('el nombre'),
        'id': _get_client_field('la cedula')
    }
    return client


def run():

    while True:
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
            client_deposit = _get_client_from_user()
            type_row = 'Fila de deposito'

            add_deposit(client_deposit)

        elif command == '2':
            print('FILA PARA APERTURA DE CUENTAS'.center(50, '='))
            print('')
            new_account = _get_client_from_user()

            add_account(new_account)

        elif command == '3':
            print(' TURNO DEL CLIENTE POR ATENDER'.center(50, '='))
            print('')

            serv_client()

        elif command == '4':
            print(' LISTA DE CLIENTES EN LA FILA '.center(50, '='))
            print('')
            list_clients()

        elif command == 'S':
            print('! Gracias por usar Banplatzi ¡'.center(50, '-'))
            break

        else:
            print('Comando invalido')


if __name__ == '__main__':
    # Message welcome
    print('BIENVENIDO A BANPLATZI'.center(50, '='))
    run()
