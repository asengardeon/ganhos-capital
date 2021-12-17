import json
import sys

from capital.service.process_capital import ProcessCapital

def read_stin():
    process = ProcessCapital()
    print("Insira o json de entrada ou então 'sair' para sair ")
    for line in sys.stdin:
        if line.strip().lower() == 'sair':
            sys.exit(0)
        else:
            return process.execute(line)

def by_file(file: str):
    process = ProcessCapital()
    f = open(file, "r")
    value = json.dumps(json.load(f))
    return process.execute(value)


if __name__ == '__main__':
    mode = sys.argv[1]
    result = ""
    if mode == "--interactive" or mode == "":
        result = read_stin()
    elif mode == '--server':
        pass
    elif "--file":
        result = by_file(sys.argv[2])
    sys.stdout.write(result)





