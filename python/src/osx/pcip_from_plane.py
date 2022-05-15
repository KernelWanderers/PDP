def pcip_from_plane(plane):
    pci_path = ''
    acpi_plane = ''

    for arg in plane.split('/'):
        if not '@' in arg:
            continue

        acpi, pci = arg.split('@')

        acpi_plane += f'/{acpi}@{pci}'
        
        if 'pci0' in acpi.lower():
            pci_path += f'PciRoot({hex(int(pci, 16))})'
            continue

        devs = [hex(int(x, 16)) for x in pci.split(',') + ['0']]

        if len(devs) == 3:
            devs = devs[:-1]

        dev, func = devs
        pci_path += f'/Pci({dev},{func})'

    return (acpi_plane, pci_path)