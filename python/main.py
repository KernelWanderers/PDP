if __name__ == '__main__':
    import platform

    match platform.system().lower():
        case 'linux':
            from src.linux.find_pci_devices import find_pci_devices
            from src.linux.construct_pcip import construct_pcip

            for dev in find_pci_devices():
                data = construct_pcip(dev)

                print(
                    f'{data.get("dbf")} ' +
                    f'{data.get("dev-ven")} ' +
                    f'{data.get("acpi")} = ' +
                    f'{data.get("pcip")}'
                )