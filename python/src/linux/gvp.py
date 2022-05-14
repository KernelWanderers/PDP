def get_valid_pcip(slot):
    try:
        return tuple([
            hex(int(n, 16)) for n in
            slot.split(':')[-1].split('.')
        ])
    except Exception:
        return (None, None)