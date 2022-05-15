def longest_seq(data):
    longest = 0

    for item in data:
        pcid = item.get('PCI-Debug') + ' '
        dev_ven = item.get('Dev-Ven') + ' '
        acpi = item.get('ACPI-Plane') + ' '

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
    longest = longest_seq(data)

    for item in data:
        pcid = item.get('PCI-Debug') + ' '
        dev_ven = item.get('Dev-Ven') + ' '
        acpi = item.get('ACPI-Plane')

        current = len(pcid) + len(dev_ven) + len(acpi)

        to_format = to_format + [
            pcid,
            dev_ven,
            acpi,
            ' ' * (longest - current),
            '= ',
            item.get('PCI-Path'),
            '\n'
        ]

    return to_format


def format_data_linux(data):
    if type(data) != dict:
        return []

    to_format = [x + ' ' for x in list(data.values())]

    index = to_format.index(to_format[-1])
    to_format.append(to_format[-1])
    to_format[index] = (' ' * 5
                        if len(data.get('acpi').split('.')) < 4
                        else '') + \
        ' = '

    return to_format
