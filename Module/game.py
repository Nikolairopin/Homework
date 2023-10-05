"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


# делим число на 2 сравниваем по половинам и так пока не найдется нужное число
def random_predict(number: int = 1) -> int:
    # диапазон случайного числа
    low = 0
    high = 100
    # счетчик попыток
    count = 0

    while low <= high:
        # переменная хранящще предполагаемое число 
        guess = (low + high) // 2
        count += 1
        # меняем диапазон загаданного числа
        if guess == number:
            return count
        elif guess < number:
            low = guess + 1
        else:
            high = guess - 1


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
