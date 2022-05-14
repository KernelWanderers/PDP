import os
import re

def find_dev_ids(dev_path):
    try:
        return re.search(
            '(?<=PCI_ID=)(.+)(?=\n|$)',
            open(os.path.join(dev_path, 'uevent'), 'r').read()
        )[0]
    except Exception:
        return
