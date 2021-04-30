import sqlite3
import readline
from os import system, name
from completer import Completer


def main():
    clear_terminal()
    print('Welcome to easy_use V ALPHA')
    print('.help for help')
    data_base_name = input('Data-base-name:')
    conection = sqlite3.connect(f'{data_base_name}.db')
    cursor = conection.cursor()

    completion = ["SELECT", "FROM", "CREATE", "TABLE",
                  "INSERT", 'INTO', 'VALUES', 'WHERE',
                  ".help", "UPDATE", "DELETE", "ALTER",
                  "DATABASE", "DROP", "INDEX", "clear",
                  ".exit", ".list"]

    completer = Completer(completion)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    while True:
        Command = str(input(">>>"))
        if Command == '.exit':
            conection.close()
            exit()

        elif Command == '.help':
            print('hola mi amigo!')

        elif Command == 'clear':
            clear_terminal()

        elif Command == '.list':
            print("All the commands are : ")
            for command in completion:
                print("                      " + command)

        else:
            try:
                cursor.execute(Command)
                conection.commit()

            except Exception as error:
                print(error)

        if 'SELECT' in Command.upper():
            for row in cursor.fetchall():
                print(row)


def clear_terminal():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    main()

