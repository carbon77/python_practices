from pract4.fortik.VM import VM
from pract4.fortik.disasm import disasm

if __name__ == '__main__':
    byte_code = [31, 256, 129, 5, 8, 4, 16, 12, 24, 20, 2, 121, 26, 10, 121, 26, 18, 121, 26, 5,
 32, 4, 40, 12, 34, 2, 121, 26, 10, 121, 26, 5, 0, 27, 48, 4, 24, 35, 152, 43,
 42, 2, 121, 26, 5]
    # print(disasm(byte_code))
    vm = VM(byte_code)
    vm.run()

