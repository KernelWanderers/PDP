import os
from .gvp import get_valid_pcip

def find_pci_devices():
    devices = []
    pci_dev_path = '/sys/bus/pci/devices/'

    if not os.path.isdir(pci_dev_path):
        raise RuntimeError('"/sys/bus/pci/devices" is not a valid directory! This should not happen..')

    for path in os.listdir(pci_dev_path):
        slot, func = get_valid_pcip(path)

        if os.path.isdir(os.path.join(pci_dev_path, path, 'firmware_node')):
            acpi_path = open(os.path.join(pci_dev_path, path, 'firmware_node', 'path'), 'r').read().replace('\n', '')
        else:
            acpi_path = "ACPI_Path_Not_Found"

        devices.append({
            'path': os.path.join(pci_dev_path, path),
            'components': (slot, func),
            'acpi': acpi_path
        })
        
    return devices
