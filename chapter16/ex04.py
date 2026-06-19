def mul_time(time, number):
    """Умножает время на число (например, для расчета интервалов)."""
    # Используем функции преобразования из Упражнения 3
    seconds = time_to_int(time) * number
    return int_to_time(int(seconds))

def find_average_pace(finish_time, distance):
    """Вычисляет средний темп (время на одну милю/километр).
    finish_time: объект Time (общее время гонки)
    distance: число (дистанция)
    """
    # Разделить время на дистанцию — это то же самое, что умножить на (1 / дистанция)
    return mul_time(finish_time, 1 / distance)

