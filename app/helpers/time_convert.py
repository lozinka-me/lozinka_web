def convert(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    return y, d, h, m, s


def convert_to_str(seconds):
    y, d, h, m, s = convert(seconds)

    time_string = ''

    if y > 0:
        time_string = '%d godina ' % y

        if y > 100:
            return 'Više od jednog vijeka'

    if d > 0:
        time_string = time_string + '%d dan(a) ' % d

    if h > 0:
        time_string = time_string + '%d sat(i) ' % h

    if m > 0:
        time_string = time_string + '%d minut(a) ' % m

    if s > 0:
        time_string = time_string + '%d sekund(i) ' % s

    if time_string == '':
        time_string = '0s'

    return time_string.strip()