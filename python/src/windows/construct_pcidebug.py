def construct_pcidebug(location):
    vals = [':', '.', '']

    return ''.join([
        hex(int(x.split(' ')[-1]))
        .zfill(4)
        .replace('0x', '') + vals[i]

        for (i, x) in enumerate(location.split(','))
    ])
