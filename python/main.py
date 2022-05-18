if __name__ == '__main__':
    import platform
    from src.util.format import format_data_linux

    print()
    match platform.system().lower():
        case 'linux':
            from src.linux.find_pci_devices import find_pci_devices
            from src.linux.construct_pcip import construct_pcip

            _format_data = []
            for dev in find_pci_devices():
                data = construct_pcip(dev)

                _format_data.append(data)

            print(*format_data_linux(_format_data))
        
        case 'darwin':
            from src.osx.find_pci_devices import find_pci_devices
            from src.osx.construct_pcip import construct_pcip
            from src.osx.pcip_from_plane import pcip_from_plane
            from src.util.format import format_data_osx

            _format_data = []

            for dev in find_pci_devices():
                data = construct_pcip(dev.get('Device'))
                acpi_plane, pci = pcip_from_plane(dev.get('Plane'))

                if not data:
                    data = pci

                _format_data.append({
                    'PCI-Debug': dev.get('PCI-Debug'),
                    'Dev-Ven': dev.get('Dev-Ven'),
                    'ACPI-Plane': acpi_plane,
                    'PCI-Path': pci
                })

            print(*format_data_osx(_format_data))

        case 'windows':
            from src.windows.find_pci_devices import find_pci_devices
            from src.windows.get_device_data import get_device_data
            from src.util.format import format_data_win

            _format_data = []

            for device in find_pci_devices():
                device_data = get_device_data(device)

                if not device_data.get('ACPI-Path'):
                    continue

                _format_data.append(device_data)

            print(*format_data_win(_format_data))