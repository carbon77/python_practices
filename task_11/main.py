import struct


def main(data):
    signature = b'\xe5\x53\x49\x53\x55'
    s = {}
    offset = len(signature)

    s['A1'], s['A2'] = struct.unpack_from("BB", data, offset)
    offset += 2
    s['A3'], offset = parse_struct_b(data, offset)

    a_size, a_offset, a5 = struct.unpack_from('HHf', data, offset)
    s['A4'] = list(struct.unpack_from(str(a_size) + 'H', data, a_offset))
    s['A5'] = a5

    return s


def parse_struct_b(data, offset):
    s = {}
    c_array = []

    for i in range(6):
        c, offset = parse_struct_c(data, offset)
        c_array.append(c)

    s['B1'] = c_array
    s['B2'], = struct.unpack_from('d', data, offset)
    offset += 8

    d_offset, = struct.unpack_from('I', data, offset)
    offset += 4

    s['B3'] = parse_struct_d(data, d_offset)
    return s, offset


def parse_struct_c(data, offset):
    s = {}
    s['C1'], s['C2'], c_size, c_offset = \
        struct.unpack_from('<hiIH', data, offset)
    offset += 2 + 4 + 4 + 2
    s['C3'] = list(struct.unpack_from(f'<{c_size}H', data, c_offset))
    return s, offset


def parse_struct_d(data, offset):
    s = {}
    s['D1'], s['D2'] = struct.unpack_from('fi', data, offset)
    offset += 4 + 4
    s['D3'] = []

    for i in range(5):
        d3_item, = struct.unpack_from('H', data, offset)
        offset += 2
        s['D3'].append(d3_item)

    return s


if __name__ == '__main__':
    import json

    x = b'\xe5SISU4\xaf\x02\xcf\xef^B\xfe\x04\x00\x00\x00c\x00<\x02\xa4j\x00\xb3\x03\x00\x00\x00k\x00_\x04\x92\xb6\x17=\x05\x00\x00\x00q\x00]iv\x85>+\x03\x00\x00\x00{\x00\xccW\xf6\xb8V\xf0\x03\x00\x00\x00\x81\x00h\nb\xe8\xb56\x03\x00\x00\x00\x87\x00|\x8f\xaf5?\x80\xd5\xbf\x8d\x00\x00\x00\x02\x00\x9f\x00\xefN\r?k\xb7\xec\x7f\xa2\xa4\xba\xd4DNcZ\xe3%\x0b\r\xc29\t]\xd9r\x87\x86`\xce4\xfaq\xcd\xa1\x13$c\xb0\x96O4\xfd[\xc1\xff\x86\x05\xd3\xbe\xd1\x14\xf5\xf6\xd0\x83.4\xef=\xf3\xcfm\xc8\xec\x08L\xb0'

    res = main(x)
    print(json.dumps(res, sort_keys=True, indent=4))
