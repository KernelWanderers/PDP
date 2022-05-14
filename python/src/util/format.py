def format_data(data):
    if type(data) != dict:
        return []

    to_format = [x + ' ' for x in list(data.values())]

    index = to_format.index(to_format[-1])
    to_format.append(to_format[-1])
    to_format[index] = (' ' * 5 \
        if len(data.get('acpi').split('.')) < 4 \
        else '') + \
        ' = '

    return to_format
