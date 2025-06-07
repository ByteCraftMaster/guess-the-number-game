import random

min_number=1
max_number=100
number = random.randint(min_number,max_number)
attempts_left = 7
print(f"Вітаю! Я загадав число від {min_number} до {max_number}. Спробуйте вгадати його за {attempts_left} спроб.")

while attempts_left>0:
    try:
        attemp = int(input("Введіть ваше припущення:"))
    except ValueError:
        print("Введіть ціле число.")
        continue
    
    if attemp<number:
        print("Занадто маленьке!")
    elif attemp>number:
        print("Занадто велике!")
    else:
        print(f"Ви вгадали! Це число {number}.")
        break
    attempts_left-=1
else:
    print(f"Ви використали всі спроби! Загадане число {number}.")