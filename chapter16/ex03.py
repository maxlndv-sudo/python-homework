def time_to_int(time):
    """Преобразует объект Time в целое число секунд с начала дня."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """Преобразует целое число секунд обратно в объект Time."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def add_time(t1, t2):
    """«Чистая» функция сложения двух объектов Time через секунды."""
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

