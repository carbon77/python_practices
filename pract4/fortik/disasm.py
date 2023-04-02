from pract4.fortik.kernel import OP_NAMES, LIB


def disasm(byte_code):
    code = 'entry: ' + str(byte_code[0])
    i = 0

    for byte in byte_code[1:]:
        command = OP_NAMES[byte % 8]
        arg = byte >> 3

        if command == 'push' or command == 'exit' or command == 'call' or command == 'to' or command == 'is':
            code += f'\n\t{i}: {command} {arg}'
        elif command == 'op':
            code += f'\n\t{i}: op \'{list(LIB.keys())[arg]}\''

        i += 1

    return code
