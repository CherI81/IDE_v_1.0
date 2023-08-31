"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import random

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1  # присваиваем значение, соответствующее нижней границе диапазона поиска
    high = 101  # присваиваем значение, соответствующее верхней границе диапазона поиска

    while True:
        average_number = (low + high)//2 # ищем середину диапазона
        count += 1 # накапливаем попытки
        if average_number == number: # если середина диапазона (число) "вдруг" равна загаданному числу
            break  # выход из цикла если угадали
        elif number > average_number: # если загаданное число больше середины дипазона
            low = average_number  # присваиваем (перемещаем, сужаем) среднему числу НИЖНЕЕ значение
        else: # иначе если загаданное число ниже среднего
            high = average_number # присваиваем (перемещаем, сужаем) среднему числу ВЕРХНЕЕ значение

    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")

    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)