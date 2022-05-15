def longest_seq(data, keys=[]):
    longest = 0

    for item in data:
        pcid = item.get(keys[0]) + ' '
        dev_ven = item.get(keys[1]) + ' '
        acpi = item.get(keys[2]) + ' '

        current = len(pcid) + len(dev_ven) + len(acpi)

        if current > longest:
            longest = current

    return longest


def format_data_osx(data):
    if type(data) != list:
        return []

    # Weird bug with formatting..
    # Fix is to append an empty string.
    to_format = ['']
    longest = longest_seq(data, ['PCI-Debug', 'Dev-Ven', 'ACPI-Plane'])

    for item in data:
        pcid = item.get('PCI-Debug') + ' '
        dev_ven = item.get('Dev-Ven') + ' '
        acpi = item.get('ACPI-Plane')
        pcip = item.get('PCI-Path')

        current = len(pcid) + len(dev_ven) + len(acpi)

        to_format += [
            pcid,
            dev_ven,
            acpi,
            ' ' * (longest - current),
            '= ',
            pcip,
            '\n'
        ]

    return to_format


def format_data_linux(data):
    if type(data) != list:
        return []

    longest = longest_seq(data, keys=['desc', 'dev-ven', 'acpi'])
    to_format = ['']

    for item in data:
        pcid = item.get('desc') + ' '
        dev_ven = item.get('dev-ven') + ' '
        acpi = item.get('acpi') + ' '
        pcip = item.get('pcip')

        current = len(pcid) + len(dev_ven) + len(acpi)

        to_format += [
            pcid,
            dev_ven,
            acpi,
            ' ' * (longest - current),
            '= ',
            pcip,
            '\n'
        ]

    return to_format
