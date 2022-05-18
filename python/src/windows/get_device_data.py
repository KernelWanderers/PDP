from .construct_pcip import construct_pcip
from .construct_pcidebug import construct_pcidebug

def get_device_data(entity):
    data = {
        'PCI-Debug': '',
        'Dev-Ven': '',
        'PCI-Path': '',
        'ACPI-Path': '',
    }

    try:
        device_info = entity.GetDeviceProperties([
            'DEVPKEY_Device_LocationInfo',
            'DEVPKEY_Device_LocationPaths'
        ])[0]

        data['PCI-Debug'] = construct_pcidebug(device_info[0].Data)

        dev_ven = entity.wmi_property('PNPDeviceID').value.split('\\')[1].split('&')[:2]

        data['Dev-Ven'] = ':'.join([dv.split('_')[1] for dv in dev_ven])
    
        pci, acpi = construct_pcip(*device_info[1].Data)

        data['PCI-Path'] = pci
        data['ACPI-Path'] = acpi

        return data
    except Exception:
        return {}