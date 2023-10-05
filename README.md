# Homework assignment 📜
1. ### Description 
   Welcome, this is a github homework assignment it implements a guess the number game in the range from 1 to 100
2. ### What was done
   - [x] A repository has been created in "homework" in github 
   - [x] An algorithm for finding a number from 1 to 100 has been written for a maximum of 7 attempts
   - [x] Gitignore and requirements created

 Below you can see the main function [This is a link to the source file](https://github.com/Nikolairopin/Homework/blob/main/Module/game.py) 
 ```python
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
```
