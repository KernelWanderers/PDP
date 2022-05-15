def hex_no_x(value):
    return str(hex(int(value, 16))).replace('0x', '')

def format_pci_debug(bus, device, func):
    if not bus or \
        not device or \
            not func:
        return

    bus = hex_no_x(bus) if int(bus) > 9 else f'{bus:02d}'
    device = hex_no_x(device) if int(device) > 9 else f'{device:02d}'
    func = hex_no_x(func)

    return f'{bus}:{device}.{func}'

