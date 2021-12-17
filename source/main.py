import sys

from source.capital.service.process_capital import ProcessCapital

def read_stin():
    process = ProcessCapital()
    print("Insira o json de entrada ou então 'sair' para sair ")
    for line in sys.stdin:
        if line.strip().lower() == 'sair':
            sys.exit(0)
        else:
            print(process.execute(line))


if __name__ == '__main__':
   read_stin()


