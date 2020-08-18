def check(dict):
    strmas = []
    if dict['years']:
        if dict['years'] == 1:
            strmas.append(' year')
        else:
            strmas.append(' years')
    if dict['days']:
        if dict['days'] == 1:
            strmas.append(' day')
        else:
            strmas.append(' days')
    if dict['hours']:
        if dict['hours'] == 1:
            strmas.append((' hour'))
        else:
            strmas.append((' hours'))
    if dict['minutes']:
        if dict['minutes'] == 1:
            strmas.append((' minute'))
        else:
            strmas.append((' minutes'))
    if dict['seconds']:
        if dict['seconds'] == 1:
            strmas.append((' second'))
        else:
            strmas.append((' seconds'))
    return strmas


def format_duration(seconds):
    if seconds == 0:
        return 'now'
    else:
        years, seconds = divmod(seconds, 60 ** 2 * 24 * 365)
        days, seconds = divmod(seconds, 60 ** 2 * 24)
        hours, seconds = divmod(seconds, 60 ** 2)
        minutes, seconds = divmod(seconds, 60)
        r = ''
        dict = {'years':years, 'days':days, 'hours':hours, 'minutes':minutes, 'seconds':seconds}
        values = []
        for i in dict.values():
            if i != 0:
                values.append(i)
        strmas = check(dict)
        if len(values) >= 3:
            if len(values) == 3:
                r = ', '.join([str(values[0]) + strmas[0], str(values[1]) + strmas[1]])
                r += ' and ' + str(values[2]) + strmas[2]
            if len(values) == 4:
                r = ', '.join([str(values[0]) + strmas[0], str(values[1]) + strmas[1],
                               str(values[2]) + strmas[2]])
                r += ' and ' + str(values[3]) + strmas[3]
            if len(values) == 5:
                r = ', '.join([str(values[0]) + strmas[0], str(values[1]) + strmas[1],
                               str(values[2]) + strmas[2], str(values[3]) + strmas[3]])
                r += ' and ' + str(values[4]) + strmas[4]
        elif len(values) == 2:
            r = ' and '.join([str(values[0]) + strmas[0], str(values[1]) + strmas[1]])
        elif len(values) == 1:
            r = str(values[0]) + strmas[0]
        return r


#чел круто сделал..
"""times = [("year", 365 * 24 * 60 * 60), 
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds: 
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]"""









