import binascii


def extract_id(data):
    try:
        return (
            binascii.b2a_hex(
                bytes(reversed(data))
            ).decode()[4:]
        )
    except Exception:
        return
