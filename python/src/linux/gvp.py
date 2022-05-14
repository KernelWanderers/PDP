def get_valid_pcip(slot):
    try:
        slot, func = [
            hex(int(n, 16)) for n in
            slot.split(':')[-1].split('.')
        ]
    except Exception:
        return (None, None)

    return (slot, func)
