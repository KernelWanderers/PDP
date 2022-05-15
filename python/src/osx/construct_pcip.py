from .ioreg import *

# Original source:
# https://github.com/dortania/OpenCore-Legacy-Patcher/blob/ca859c7ad7ac2225af3b50626d88f3bfe014eaa8/resources/device_probe.py#L67-L93
def construct_pcip(parent_entry):
    paths = []
    entry = parent_entry

    while entry:
        if IOObjectConformsTo(entry, b'IOPCIDevice'):
            try:
                bus, func = [
                    hex(int(i, 16)) for i in
                    ioname_t_to_str(
                        IORegistryEntryGetLocationInPlane(
                            entry, b'IOService', None
                        )[1]
                    ).split(',') + ['0']
                ]

                paths.append(
                    f'/Pci({bus},{func})'
                )
            except ValueError:
                break

        elif IOObjectConformsTo(entry, b'IOACPIPlatformDevice'):
            paths.append(f'PciRoot({hex(int(corefoundation_to_native(IORegistryEntryCreateCFProperty(entry, "_UID", kCFAllocatorDefault, kNilOptions)) or 0))})')
            break
        
        elif IOObjectConformsTo(entry, b'IOPCIBridge'):
            pass

        else:
            paths = []
            break

        parent = IORegistryEntryGetParentEntry(entry, b'IOService', None)[1]

        if entry != parent_entry:
            IOObjectRelease(entry)

        entry = parent

    return '/'.join(reversed(paths))