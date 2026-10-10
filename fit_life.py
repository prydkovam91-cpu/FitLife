# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30          # мл воды на 1 кг веса
ML_IN_LITER = 1000         # миллилитров в одном литре


# 1. Знакомство (с функцией исправления возможной ошибки).
user_name = input("Как Вас зовут? ")
while True:
    age_input = input("Введите ваш возраст: ")
    try:
        user_age = int(age_input)
        # Проверка ограничений по возрасту
        if user_age < 16:
            print("Пожалуйста, введите корректный возраст.")
        elif user_age > 100:
            print("Пожалуйста, проверьте данные.")
        else:
            break  # если возраст в допустимых пределах, выходим из цикла
    except ValueError:
        print("Пожалуйста, введите возраст цифрами.")


# 2. Сбор данных (с функцией исправления возможной ошибки).
while True:
    weight_input = input("Какой у Вас вес (в кг)? ")
    try:
        user_weight = float(weight_input)
        # Проверка ограничений по весу
        if user_weight < 30:
            print("Пожалуйста, введите реальный вес.")
        elif user_weight > 300:
            print("Пожалуйста, проверьте данные.")
        else:
            break  # если вес в допустимых пределах, выходим из цикла
    except ValueError:
        print("Пожалуйста, введите вес цифрами.")

while True:
    height_input = input("Какой у Вас рост (в метрах, например 1.60)? ")
    # Заменяем запятую на точку — так поддержим оба формата ввода
    height_input_fixed = height_input.replace(",", ".")
    try:
        user_height = float(height_input_fixed)
        if user_height < 1.0:
            print("Пожалуйста, введите реальный рост.")
        elif user_height > 2.5:
            print("Пожалуйста, проверьте данные.")
        else:
            break  # если рост в допустимых пределах, выходим из цикла
    except ValueError:
        print("Пожалуйста, используйте цифры и точку или запятую.")

# 3. Расчет ИМТ
bmi = user_weight / (user_height ** 2)
# Расчёт нормы воды через константу
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_IN_LITER   # переводим в литры


name_formatted = user_name.capitalize()  # имя с заглавной буквы

# Определение категории ИМТ
if bmi < 18.5:
    bmi_category = "недостаточный вес"
elif 18.5 <= bmi < 25:
    bmi_category = "нормальный вес"
elif 25 <= bmi < 30:
    bmi_category = "избыточный вес"
else:
    bmi_category = "ожирение"

# 4. Вывод красивого результата
print(
    "=" * 50,
    f"  Добрый день, {name_formatted}! Вам {user_age} лет.",
    "- " * 25,
    f"  Ваш Индекс Массы Тела: {bmi:.1f} ({bmi_category})",
    f"  Рекомендуемая норма воды: {water_l:.1f} л в день.",
    "=" * 50,
    "  Расчёт окончен. Будьте здоровы!",
    "=" * 50,
    sep="\n"
)
