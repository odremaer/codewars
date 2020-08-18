def make_readable(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

print(make_readable(359999))