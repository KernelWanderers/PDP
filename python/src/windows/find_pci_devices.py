def find_pci_devices():
    import wmi

    _wmi = wmi.WMI()

    entities = []

    for entity in _wmi.instances("Win32_PnPEntity"):
        pnp_dev_id = entity.wmi_property("PNPDeviceID")

        if not pnp_dev_id:
            continue

        if 'pci' not in pnp_dev_id.value.lower():
            continue

        entities.append(entity)

    return entities