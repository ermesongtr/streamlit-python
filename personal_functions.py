def format_number(value, prefix= ''):
    if len(str(value)) <= 6:
        return f'{prefix} {value/1000:.3f} mil'
    else:
        return f'{prefix} {value/1000:.3f} milhões'
