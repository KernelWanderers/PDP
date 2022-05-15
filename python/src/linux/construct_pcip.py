import os
from math import floor
from .find_dev_ids import find_dev_ids
from .find_pcie import find_pcie
from .get_domain import get_domain


def construct_pcip(device):
    if not device or \
            not device.get('path') or \
            not device.get('components') or \
            not device.get('acpi'):
        return

    path = device.get('path')
    slot, func = device.get('components')
    acpi = device.get('acpi')

    amount = floor(
        len(device.get('acpi', '').split('.')) / 2
    )

    domain = get_domain(device.get('path').split('/')[-1])

    if not domain:
        return

    child_slot, child_func = find_pcie(path)

    pcip = f'{domain}/Pci({slot},{func})'

    if amount == 2 and child_slot != '' and child_func != '':
        pcip_div = pcip.split('/')

        pcip_div.append(pcip_div[1])
        pcip_div[1] = f'Pci({child_slot},{child_func})'

        pcip = '/'.join(pcip_div)

    return {
        'desc': path.split('/')[-1].split(':')[1:],
        'pcip': pcip,
        'dev-ven': find_dev_ids(path),
        'acpi': acpi
    }