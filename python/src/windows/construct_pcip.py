def _convert(digit):
    return (hex(int(digit[:2], 16)), hex(int(digit[2:], 16)))


def _construct_acpi(acpi):
    path = ''

    for value in acpi.split('#'):
        if 'usb' in acpi.lower():
            path = None
            break

        if '_sb_' in value.lower():
            path += '\_SB'
            continue

        try:
            _acpi, val = value[:-1].split('(')
        except Exception:
            path = None
            break

        if _acpi.lower() == 'pci':
            path = None
            break

        path += '.' + val

    return path


def _construct_pci(pci):
    path = ''

    for value in pci.split('#'):
        digit = value[:-1].split('(')[1]

        if not digit:
            path = None
            break

        if 'pciroot' in value.lower():
            path += f'PciRoot({hex(int(digit, 16))})'
            continue

        converted = ','.join(_convert(digit))
        path += f'/Pci({converted})'

    return path


def construct_pcip(pci, acpi):
    return (
        _construct_pci(pci),
        _construct_acpi(acpi)
    )
