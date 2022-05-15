import binascii
from .ioreg import *
from .extract_id import extract_id

def find_pci_devices():
    devices = []
    device_desc = {
        "IOProviderClass": "IOPCIDevice",
    }

    # Obtain generator instance, whose values are of type `CFDictionary`
    interface = ioiterator_to_list(
        IOServiceGetMatchingServices(
            kIOMasterPortDefault, device_desc, None
        )[1]
    )

    for i in interface:
        data = {}

        # Obtain CFDictionaryRef of the current PCI device.
        device = corefoundation_to_native(
            IORegistryEntryCreateCFProperties(
                i, None, kCFAllocatorDefault, kNilOptions
            )
        )[1]

        try:
            data['Plane'] = ioname_t_to_str(
                IORegistryEntryGetPath(i, b'IOService', None)[1]
            )
        except Exception:
            continue

        # God have mercy.
        PCI_DEBUG = device.get('pcidebug')

        pcid = PCI_DEBUG.split('(')[0]

        val = ':'.join([hex(int(x)).zfill(4).replace('0x', '')
                       for x in pcid.split(':')])
        split = val.split(':')
        val = ':'.join(split)
        f = len(split[0])
        s = len(split[1])
        val = list(val.replace('0x', ''))
        val[f + s + 1] = '.'
        val[f + s + 2] = val[f + s + 3]
        val = val[:f + s + 3]
        PCI_DEBUG = ''.join(val)

        if PCI_DEBUG:
            data['PCI-Debug'] = PCI_DEBUG

        dev_id = extract_id(device.get('device-id'))
        ven_id = extract_id(device.get('vendor-id'))

        if dev_id and ven_id:
            data['Dev-Ven'] = f'{ven_id}:{dev_id}'

        data['Device'] = i

        devices.append(data)

    return devices
