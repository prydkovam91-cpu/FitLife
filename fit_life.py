# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30          # мл воды на 1 кг веса
ML_IN_LITER = 1000         # миллилитров в одном литре


# 1. Знакомство (с функцией исправления возможной ошибки).
user_name = input("Как Вас зовут? ")
while True:
    age_input = input("Введите ваш возраст: ")
    try:
        user_age = int(age_input)
        break  # если всё хорошо, выходим из цикла
    except ValueError:
        print("Пожалуйста, введите возраст цифрами.")


# 2. Сбор данных (с функцией исправления возможной ошибки).
user_weight = float(input("Какой у Вас вес (в кг)? "))

while True:
    height_input = input("Какой у Вас рост (в метрах, например 1.60)? ")
    # Заменяем запятую на точку — так поддержим оба формата ввода
    height_input_fixed = height_input.replace(',', '.')
    try:
        user_height = float(height_input_fixed)
        break  # если всё хорошо, выходим из цикла
    except ValueError:
        print("Пожалуйста, используйте цифры и точку или запятую).")

# 3. Расчет ИМТ
bmi = user_weight / (user_height ** 2)
# Расчёт нормы воды через константу
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER   # переводим в литры


name_formatted = user_name.capitalize()  # имя с заглавной буквы
# 4. Вывод красивого результата
print(f"Добрый день, {name_formatted}! Вам {user_age} лет.")
print(f"Ваш Индекс Массы Тела: {bmi:.1f}")
print(f"Рекомендуемая норма воды:  {water_l:.1f} л в день.")
# Округляем значения.
print("Расчёт окончен. Будьте здоровы!")
