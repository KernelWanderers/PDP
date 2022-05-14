def get_domain(dev_path):
    if not ':' in dev_path:
        return

    domain = hex(
        int(
            dev_path.split(':')[0],
            16
        )
    )

    return f'PciRoot({domain})'