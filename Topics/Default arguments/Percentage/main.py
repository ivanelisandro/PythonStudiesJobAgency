def get_percentage(number, round_digits=None):
    percent = number * 100
    return f'{round(percent, round_digits)}%'
